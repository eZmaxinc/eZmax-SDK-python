# EzsigntemplatedocumentpagerecognitionDeleteObjectV1Response

Response for DELETE /1/object/ezsigntemplatedocumentpagerecognition/{pkiEzsigntemplatedocumentpagerecognitionID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsigntemplatedocumentpagerecognition_delete_object_v1_response import EzsigntemplatedocumentpagerecognitionDeleteObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatedocumentpagerecognitionDeleteObjectV1Response from a JSON string
ezsigntemplatedocumentpagerecognition_delete_object_v1_response_instance = EzsigntemplatedocumentpagerecognitionDeleteObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatedocumentpagerecognitionDeleteObjectV1Response.to_json())

# convert the object into a dict
ezsigntemplatedocumentpagerecognition_delete_object_v1_response_dict = ezsigntemplatedocumentpagerecognition_delete_object_v1_response_instance.to_dict()
# create an instance of EzsigntemplatedocumentpagerecognitionDeleteObjectV1Response from a dict
ezsigntemplatedocumentpagerecognition_delete_object_v1_response_from_dict = EzsigntemplatedocumentpagerecognitionDeleteObjectV1Response.from_dict(ezsigntemplatedocumentpagerecognition_delete_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


