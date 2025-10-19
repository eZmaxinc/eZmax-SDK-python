# EzsigntemplatesignatureEditObjectV3Request

Request for PUT /3/object/ezsigntemplatesignature/{pkiEzsigntemplatesignatureID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigntemplatesignature** | [**EzsigntemplatesignatureRequestCompoundV2**](EzsigntemplatesignatureRequestCompoundV2.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatesignature_edit_object_v3_request import EzsigntemplatesignatureEditObjectV3Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatesignatureEditObjectV3Request from a JSON string
ezsigntemplatesignature_edit_object_v3_request_instance = EzsigntemplatesignatureEditObjectV3Request.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatesignatureEditObjectV3Request.to_json())

# convert the object into a dict
ezsigntemplatesignature_edit_object_v3_request_dict = ezsigntemplatesignature_edit_object_v3_request_instance.to_dict()
# create an instance of EzsigntemplatesignatureEditObjectV3Request from a dict
ezsigntemplatesignature_edit_object_v3_request_from_dict = EzsigntemplatesignatureEditObjectV3Request.from_dict(ezsigntemplatesignature_edit_object_v3_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


