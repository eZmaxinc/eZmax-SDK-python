# DocumentationSubscribeV1Response

Request for POST /1/module/ezmaxmaillinglist/subscribe

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_external_id** | **str** |  | 

## Example

```python
from eZmaxApi.models.documentation_subscribe_v1_response import DocumentationSubscribeV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentationSubscribeV1Response from a JSON string
documentation_subscribe_v1_response_instance = DocumentationSubscribeV1Response.from_json(json)
# print the JSON string representation of the object
print(DocumentationSubscribeV1Response.to_json())

# convert the object into a dict
documentation_subscribe_v1_response_dict = documentation_subscribe_v1_response_instance.to_dict()
# create an instance of DocumentationSubscribeV1Response from a dict
documentation_subscribe_v1_response_from_dict = DocumentationSubscribeV1Response.from_dict(documentation_subscribe_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


