# ApikeyEditObjectV1Response

Response for PUT /1/object/apikey/{pkiApikeyID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.apikey_edit_object_v1_response import ApikeyEditObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApikeyEditObjectV1Response from a JSON string
apikey_edit_object_v1_response_instance = ApikeyEditObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(ApikeyEditObjectV1Response.to_json())

# convert the object into a dict
apikey_edit_object_v1_response_dict = apikey_edit_object_v1_response_instance.to_dict()
# create an instance of ApikeyEditObjectV1Response from a dict
apikey_edit_object_v1_response_from_dict = ApikeyEditObjectV1Response.from_dict(apikey_edit_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


