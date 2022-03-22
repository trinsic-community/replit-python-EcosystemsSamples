import asyncio

from trinsic.account_service import AccountService

async def sign_in_demo():
    account_service = AccountService()
    account = await account_service.sign_in()

if __name__ == "__main__":
    asyncio.run(sign_in_demo())