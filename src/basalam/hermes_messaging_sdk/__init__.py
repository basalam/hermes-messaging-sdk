"""
Hermes SDK - Lightweight Python client for triggering Hermes workflows

Sync Usage:
    from basalam.hermes_messaging_sdk import HermesClient

    # Initialize client with access token
    client = HermesClient(
        access_token="your-access-token"
    )

    # Trigger a single workflow
    trigger_uuid = client.trigger_workflow(
        workflow_id=123,
        data={"user_id": 456, "action": "purchase"}
    )
    print(trigger_uuid)

    # Trigger workflow in bulk
    trigger_uuids = client.bulk_trigger_workflow(
        workflow_id=123,
        triggers=[
            {"user_id": 456, "action": "purchase"},
            {"user_id": 789, "action": "signup"}
        ]
    )
    print(trigger_uuids)

Async Usage:
    from basalam.hermes_messaging_sdk import AsyncHermesClient
    import asyncio

    async def main():
        client = AsyncHermesClient(
            access_token="your-access-token"
        )
        trigger_uuid = await client.trigger_workflow(
            workflow_id=123,
            data={"user_id": 456}
        )
        print(trigger_uuid)
        await client.close()

    asyncio.run(main())
"""

from .client import HermesClient
from .exceptions import HermesError, HermesAPIError, HermesConnectionError, HermesAuthorizationError

# Async client is optional (requires httpx)
try:
    from .async_client import AsyncHermesClient
    __all__ = [
        "HermesClient",
        "AsyncHermesClient",
        "HermesError",
        "HermesAPIError",
        "HermesConnectionError",
        "HermesAuthorizationError"
    ]
except ImportError:
    __all__ = [
        "HermesClient",
        "HermesError",
        "HermesAPIError",
        "HermesConnectionError",
        "HermesAuthorizationError"
    ]

__version__ = "0.1.0"