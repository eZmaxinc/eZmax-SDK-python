# CommonResponse

All API response will inherit this based Response

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.common_response import CommonResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CommonResponse from a JSON string
common_response_instance = CommonResponse.from_json(json)
# print the JSON string representation of the object
print CommonResponse.to_json()

# convert the object into a dict
common_response_dict = common_response_instance.to_dict()
# create an instance of CommonResponse from a dict
common_response_form_dict = common_response.from_dict(common_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


