# EzsigntemplatepackagemembershipDeleteObjectV1Response

Response for DELETE /1/object/ezsigntemplatepackagemembership/{pkiEzsigntemplatepackagemembershipID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_debug_payload** | [**CommonResponseObjDebugPayload**](CommonResponseObjDebugPayload.md) |  | 
**obj_debug** | [**CommonResponseObjDebug**](CommonResponseObjDebug.md) |  | [optional] 

## Example

```python
from eZmaxApi.models.ezsigntemplatepackagemembership_delete_object_v1_response import EzsigntemplatepackagemembershipDeleteObjectV1Response

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatepackagemembershipDeleteObjectV1Response from a JSON string
ezsigntemplatepackagemembership_delete_object_v1_response_instance = EzsigntemplatepackagemembershipDeleteObjectV1Response.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatepackagemembershipDeleteObjectV1Response.to_json())

# convert the object into a dict
ezsigntemplatepackagemembership_delete_object_v1_response_dict = ezsigntemplatepackagemembership_delete_object_v1_response_instance.to_dict()
# create an instance of EzsigntemplatepackagemembershipDeleteObjectV1Response from a dict
ezsigntemplatepackagemembership_delete_object_v1_response_from_dict = EzsigntemplatepackagemembershipDeleteObjectV1Response.from_dict(ezsigntemplatepackagemembership_delete_object_v1_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


