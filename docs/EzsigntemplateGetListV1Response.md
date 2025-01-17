# EzsigntemplateGetListV1Response

Response for GET /1/object/ezsigntemplate/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplateGetListV1ResponseMPayload**](EzsigntemplateGetListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplate_get_list_v1_response import EzsigntemplateGetListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateGetListV1Response from a JSON string
ezsigntemplate_get_list_v1_response_instance = EzsigntemplateGetListV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateGetListV1Response.to_json())

# convert the object into a dict
ezsigntemplate_get_list_v1_response_dict = ezsigntemplate_get_list_v1_response_instance.to_dict()
# create an instance of EzsigntemplateGetListV1Response from a dict
ezsigntemplate_get_list_v1_response_from_dict = EzsigntemplateGetListV1Response.from_dict(ezsigntemplate_get_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


