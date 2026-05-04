from typing import TypedDict, List


class AgentState(TypedDict):
    image_path: str
    raw_description: str
    is_relevant: bool
    structured_data: dict
    history: List[str]
