# EzmaxmaillinglistSubscribeV1Request

Request for POST /1/module/ezmaxmaillinglist/subscribe

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_pki_ezmaxmaillinglist_id** | **List[int]** |  | 

## Example

```python
from eZmaxApi.models.ezmaxmaillinglist_subscribe_v1_request import EzmaxmaillinglistSubscribeV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzmaxmaillinglistSubscribeV1Request from a JSON string
ezmaxmaillinglist_subscribe_v1_request_instance = EzmaxmaillinglistSubscribeV1Request.from_json(json)
# print the JSON string representation of the object
print(EzmaxmaillinglistSubscribeV1Request.to_json())

# convert the object into a dict
ezmaxmaillinglist_subscribe_v1_request_dict = ezmaxmaillinglist_subscribe_v1_request_instance.to_dict()
# create an instance of EzmaxmaillinglistSubscribeV1Request from a dict
ezmaxmaillinglist_subscribe_v1_request_from_dict = EzmaxmaillinglistSubscribeV1Request.from_dict(ezmaxmaillinglist_subscribe_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


