import asyncio

async def post_api_create():
    print(f'Execution Started:: POST - Create')
    await asyncio.sleep(1.5)
    print(f'Execution Finished:: POST - Create')
    return 'CreateResponse'

async def get_api_read():
    print(f'Execution Started:: GET - Read')
    await asyncio.sleep(1.0)
    print(f'Execution Finished:: GET - Read')
    return 'ReadResponse'

async def put_api_update():
    print(f'Execution Started:: PUT - Update')
    await asyncio.sleep(2.0)
    print(f'Execution Finished:: PUT - Update')

async def main():
    print('Starting API calls (POST, GET, PUT)')
    async_result = await asyncio.gather(post_api_create(),
                         get_api_read(),
                         put_api_update())
    print(f'All API calls completed: {async_result}')

asyncio.run(main())