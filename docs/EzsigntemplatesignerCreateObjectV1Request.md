# EzsigntemplatesignerCreateObjectV1Request

Request for POST /1/object/ezsigntemplatesigner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigntemplatesigner** | [**List[EzsigntemplatesignerRequestCompound]**](EzsigntemplatesignerRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatesigner_create_object_v1_request import EzsigntemplatesignerCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatesignerCreateObjectV1Request from a JSON string
ezsigntemplatesigner_create_object_v1_request_instance = EzsigntemplatesignerCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatesignerCreateObjectV1Request.to_json())

# convert the object into a dict
ezsigntemplatesigner_create_object_v1_request_dict = ezsigntemplatesigner_create_object_v1_request_instance.to_dict()
# create an instance of EzsigntemplatesignerCreateObjectV1Request from a dict
ezsigntemplatesigner_create_object_v1_request_form_dict = ezsigntemplatesigner_create_object_v1_request.from_dict(ezsigntemplatesigner_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


