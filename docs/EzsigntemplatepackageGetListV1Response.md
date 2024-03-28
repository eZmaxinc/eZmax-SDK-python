# EzsigntemplatepackageGetListV1Response

Response for GET /1/object/ezsigntemplatepackage/getList

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 
**m_payload** | [**EzsigntemplatepackageGetListV1ResponseMPayload**](EzsigntemplatepackageGetListV1ResponseMPayload.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackage_get_list_v1_response import EzsigntemplatepackageGetListV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackageGetListV1Response from a JSON string
ezsigntemplatepackage_get_list_v1_response_instance = EzsigntemplatepackageGetListV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepackageGetListV1Response.to_json())

# convert the object into a dict
ezsigntemplatepackage_get_list_v1_response_dict = ezsigntemplatepackage_get_list_v1_response_instance.to_dict()
# create an instance of EzsigntemplatepackageGetListV1Response from a dict
ezsigntemplatepackage_get_list_v1_response_form_dict = ezsigntemplatepackage_get_list_v1_response.from_dict(ezsigntemplatepackage_get_list_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


