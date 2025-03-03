from typing import Dict, Any
from data.Service import Service

service = Service()

def get_events(
        location: str,
        page: int = 1,
        actual_since: int = 1
) -> Dict[str, Any]:
    """Returns all events from the database"""

    return service.get(
        "events",
        {
            "location": location,
            "page": page,
            "actual_since": actual_since,
            "fields": "id,title,short_title,images,dates"
        }
    )

def get_event_detail(event_id: int) -> Dict[str, Any]:
    """Returns detailed event information"""

    return service.get(f"events/{event_id}")

def get_event_comments(event_id: int) -> Dict[str, Any]:
    """Returns comments on an event"""

    return service.get(f"events/{event_id}/comments")
