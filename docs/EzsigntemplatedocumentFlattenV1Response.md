# EzsigntemplatedocumentFlattenV1Response

Response for POST /1/object/ezsigntemplatedocument/{pkiEzsigntemplatedocument}/flatten

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsigntemplatedocument_flatten_v1_response import EzsigntemplatedocumentFlattenV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatedocumentFlattenV1Response from a JSON string
ezsigntemplatedocument_flatten_v1_response_instance = EzsigntemplatedocumentFlattenV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatedocumentFlattenV1Response.to_json())

# convert the object into a dict
ezsigntemplatedocument_flatten_v1_response_dict = ezsigntemplatedocument_flatten_v1_response_instance.to_dict()
# create an instance of EzsigntemplatedocumentFlattenV1Response from a dict
ezsigntemplatedocument_flatten_v1_response_from_dict = EzsigntemplatedocumentFlattenV1Response.from_dict(ezsigntemplatedocument_flatten_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


