from datetime import timezone, datetime
from typing import List

from banyan.api.base import ServiceBase, InfoObjectOrName
from banyan.core.exc import BanyanError
from banyan.model import BanyanApiObject
from banyan.model.shield import Shield, ShieldConfig


class ShieldAPI(ServiceBase):
    class Meta:
        data_class = Shield
        info_class = None
        arg_type = str
        list_uri = '/shield_config'
        delete_uri = None
        insert_uri = None
        uri_param = None
        obj_name = 'shield'

    def __init__(self, client):
        self._config: ShieldConfig = ShieldConfig()
        super().__init__(client)

    def list(self) -> List[Shield]:
        response_json = self._client.api_request('GET', self.Meta.list_uri)
        self._config = ShieldConfig.Schema().load(response_json)
        self._build_cache(self._config.shields)
        return self._config.shields

    def active(self) -> List[Shield]:
        shields = self.list()
        return [x for x in shields if x.name]  # what defines a shield as "enabled"?

    def create(self, obj: BanyanApiObject):
        raise BanyanError('Shields cannot be created via API')

    def delete(self, obj: InfoObjectOrName):
        raise BanyanError('Shields cannot be deleted via API')

    def update(self, obj: BanyanApiObject):
        raise BanyanError('Shields cannot be updated via API')

    def find(self, obj: InfoObjectOrName) -> Shield:
        return super().find(obj)

    def status(self, shield_name_or_id: str) -> str:
        shield = self.find(shield_name_or_id)
        activity = self.config.last_activity_map[str(shield.id)]
        now = datetime.now(tz=timezone.utc)
        age = now - activity.last_activity_time
        return 'INACTIVE' if age.total_seconds() >= 900 else 'REPORTING'

    @property
    def config(self) -> ShieldConfig:
        self._ensure_cache()
        return self._config
