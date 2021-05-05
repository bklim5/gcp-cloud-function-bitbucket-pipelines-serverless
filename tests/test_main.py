import pytest
from main import handler


class MockRequest():
    def __init__(self, mock_req, mock_args):
        self.req_json = mock_req
        self.args = mock_args

    def get_json(self):
        return self.req_json


@pytest.mark.parametrize('mock_request, expected', [
    (MockRequest(None, {'message': 'Hello args'}), 'Hello args'),
    (MockRequest({'message': 'Hello json'}, None), 'Hello json'),
    (MockRequest(None, None), 'Hello Bitbucket Pipelines with GCP Cloud Function + Serverless!!!!')
])
def test_handler(mock_request, expected):
    assert handler(mock_request) == expected
