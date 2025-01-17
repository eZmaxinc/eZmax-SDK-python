# EzsignsigningreasonGetListV1Response

Response for GET /1/object/ezsignsigningreason/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**EzsignsigningreasonGetListV1ResponseMPayload**](EzsignsigningreasonGetListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignsigningreason_get_list_v1_response import EzsignsigningreasonGetListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignsigningreasonGetListV1Response from a JSON string
ezsignsigningreason_get_list_v1_response_instance = EzsignsigningreasonGetListV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsignsigningreasonGetListV1Response.to_json())

# convert the object into a dict
ezsignsigningreason_get_list_v1_response_dict = ezsignsigningreason_get_list_v1_response_instance.to_dict()
# create an instance of EzsignsigningreasonGetListV1Response from a dict
ezsignsigningreason_get_list_v1_response_from_dict = EzsignsigningreasonGetListV1Response.from_dict(ezsignsigningreason_get_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


