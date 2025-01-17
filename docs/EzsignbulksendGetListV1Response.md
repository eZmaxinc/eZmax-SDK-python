# EzsignbulksendGetListV1Response

Response for GET /1/object/ezsignbulksend/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**m_payload** | [**EzsignbulksendGetListV1ResponseMPayload**](EzsignbulksendGetListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsignbulksend_get_list_v1_response import EzsignbulksendGetListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsignbulksendGetListV1Response from a JSON string
ezsignbulksend_get_list_v1_response_instance = EzsignbulksendGetListV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsignbulksendGetListV1Response.to_json())

# convert the object into a dict
ezsignbulksend_get_list_v1_response_dict = ezsignbulksend_get_list_v1_response_instance.to_dict()
# create an instance of EzsignbulksendGetListV1Response from a dict
ezsignbulksend_get_list_v1_response_from_dict = EzsignbulksendGetListV1Response.from_dict(ezsignbulksend_get_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


