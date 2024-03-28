# CommonResponseGetList

All API response will inherit this based Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayloadGetList**](CommonResponseObjDebugPayloadGetList.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.common_response_get_list import CommonResponseGetList

# TODO update the JSON string below
json = "{}"
# create an instance of CommonResponseGetList from a JSON string
common_response_get_list_instance = CommonResponseGetList.from_json(json)
# print the JSON string representation of the object
print(CommonResponseGetList.to_json())

# convert the object into a dict
common_response_get_list_dict = common_response_get_list_instance.to_dict()
# create an instance of CommonResponseGetList from a dict
common_response_get_list_form_dict = common_response_get_list.from_dict(common_response_get_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


