# EzsigntemplateCreateObjectV1Request

Request for POST /1/object/ezsigntemplate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigntemplate** | [**List[EzsigntemplateRequestCompound]**](EzsigntemplateRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplate_create_object_v1_request import EzsigntemplateCreateObjectV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateCreateObjectV1Request from a JSON string
ezsigntemplate_create_object_v1_request_instance = EzsigntemplateCreateObjectV1Request.from_json(json)
# print the JSON string representation of the object
print EzsigntemplateCreateObjectV1Request.to_json()

# convert the object into a dict
ezsigntemplate_create_object_v1_request_dict = ezsigntemplate_create_object_v1_request_instance.to_dict()
# create an instance of EzsigntemplateCreateObjectV1Request from a dict
ezsigntemplate_create_object_v1_request_form_dict = ezsigntemplate_create_object_v1_request.from_dict(ezsigntemplate_create_object_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


