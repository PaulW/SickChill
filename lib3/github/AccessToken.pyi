from typing import Any, Dict

from github.GithubObject import NonCompletableGithubObject

class AccessToken(NonCompletableGithubObject):
    def __repr__(self) -> str: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    @property
    def token(self) -> str: ...
    @property
    def type(self) -> str: ...
    @property
    def scope(self) -> str: ...