import asyncio
from unittest import IsolatedAsyncioTestCase

from asgiref.testing import ApplicationCommunicator

from opentelemetry.test.test_base import TestBase


def setup_testing_defaults(scope):
    scope.update(
        {
            "client": ("127.0.0.1", 32767),
            "headers": [],
            "http_version": "1.0",
            "method": "GET",
            "path": "/",
            "query_string": b"",
            "scheme": "http",
            "server": ("127.0.0.1", 80),
            "type": "http",
        }
    )


class AsyncAsgiTestBase(TestBase, IsolatedAsyncioTestCase):
    def setUp(self):
        super().setUp()

        self.scope = {}
        setup_testing_defaults(self.scope)
        self.communicator = None

    def tearDown(self):
        if self.communicator:
            asyncio.get_event_loop().run_until_complete(
                self.communicator.wait()
            )

    def seed_app(self, app):
        self.communicator = ApplicationCommunicator(app, self.scope)

    async def send_input(self, message):
        await self.communicator.send_input(message)

    async def send_default_request(self):
        await self.send_input({"type": "http.request", "body": b""})

    async def get_output(self, timeout=1):
        return await self.communicator.receive_output(timeout)

    async def get_all_output(self, timeout=1):
        outputs = []
        while True:
            try:
                outputs.append(await self.communicator.receive_output(timeout))
            except asyncio.TimeoutError:
                break
        return outputs
