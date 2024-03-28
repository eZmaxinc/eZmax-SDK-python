# EzsigntemplatesignerEditObjectV1Request

Request for PUT /1/object/ezsigntemplatesigner/{pkiEzsigntemplatesignerID}

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**obj_ezsigntemplatesigner** | [**EzsigntemplatesignerRequestCompound**](EzsigntemplatesignerRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatesigner_edit_object_v1_request import EzsigntemplatesignerEditObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatesignerEditObjectV1Request from a JSON string
ezsigntemplatesigner_edit_object_v1_request_instance = EzsigntemplatesignerEditObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatesignerEditObjectV1Request.to_json())

# convert the object into a dict
ezsigntemplatesigner_edit_object_v1_request_dict = ezsigntemplatesigner_edit_object_v1_request_instance.to_dict()
# create an instance of EzsigntemplatesignerEditObjectV1Request from a dict
ezsigntemplatesigner_edit_object_v1_request_form_dict = ezsigntemplatesigner_edit_object_v1_request.from_dict(ezsigntemplatesigner_edit_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


