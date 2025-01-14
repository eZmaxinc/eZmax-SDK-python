# EzsigntemplatesignatureEditObjectV2Request

Request for PUT /2/object/ezsigntemplatesignature/{pkiEzsigntemplatesignatureID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigntemplatesignature** | [**EzsigntemplatesignatureRequestCompoundV2**](EzsigntemplatesignatureRequestCompoundV2.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatesignature_edit_object_v2_request import EzsigntemplatesignatureEditObjectV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatesignatureEditObjectV2Request from a JSON string
ezsigntemplatesignature_edit_object_v2_request_instance = EzsigntemplatesignatureEditObjectV2Request.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatesignatureEditObjectV2Request.to_json())

# convert the object into a dict
ezsigntemplatesignature_edit_object_v2_request_dict = ezsigntemplatesignature_edit_object_v2_request_instance.to_dict()
# create an instance of EzsigntemplatesignatureEditObjectV2Request from a dict
ezsigntemplatesignature_edit_object_v2_request_from_dict = EzsigntemplatesignatureEditObjectV2Request.from_dict(ezsigntemplatesignature_edit_object_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


