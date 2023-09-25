# GlobalEzmaxclientVersionV1Response

Response for GET /1/ezmaxclient/{pksEzmaxclientOs}/version

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s_ezmaxclient_version** | **str** | The version on the store | 

## Example

```python
from eZmaxApi.models.global_ezmaxclient_version_v1_response import GlobalEzmaxclientVersionV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of GlobalEzmaxclientVersionV1Response from a JSON string
global_ezmaxclient_version_v1_response_instance = GlobalEzmaxclientVersionV1Response.from_json(json)
# print the JSON string representation of the object
print GlobalEzmaxclientVersionV1Response.to_json()

# convert the object into a dict
global_ezmaxclient_version_v1_response_dict = global_ezmaxclient_version_v1_response_instance.to_dict()
# create an instance of GlobalEzmaxclientVersionV1Response from a dict
global_ezmaxclient_version_v1_response_form_dict = global_ezmaxclient_version_v1_response.from_dict(global_ezmaxclient_version_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


