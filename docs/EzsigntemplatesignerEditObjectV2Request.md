# EzsigntemplatesignerEditObjectV2Request

Request for PUT /2/object/ezsigntemplatesigner/{pkiEzsigntemplatesignerID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigntemplatesigner** | [**EzsigntemplatesignerRequestCompoundV2**](EzsigntemplatesignerRequestCompoundV2.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatesigner_edit_object_v2_request import EzsigntemplatesignerEditObjectV2Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatesignerEditObjectV2Request from a JSON string
ezsigntemplatesigner_edit_object_v2_request_instance = EzsigntemplatesignerEditObjectV2Request.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatesignerEditObjectV2Request.to_json())

# convert the object into a dict
ezsigntemplatesigner_edit_object_v2_request_dict = ezsigntemplatesigner_edit_object_v2_request_instance.to_dict()
# create an instance of EzsigntemplatesignerEditObjectV2Request from a dict
ezsigntemplatesigner_edit_object_v2_request_from_dict = EzsigntemplatesignerEditObjectV2Request.from_dict(ezsigntemplatesigner_edit_object_v2_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


