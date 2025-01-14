# EzsigntemplateCreateObjectV3Request

Request for POST /3/object/ezsigntemplate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigntemplate** | [**List[EzsigntemplateRequestCompoundV3]**](EzsigntemplateRequestCompoundV3.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplate_create_object_v3_request import EzsigntemplateCreateObjectV3Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplateCreateObjectV3Request from a JSON string
ezsigntemplate_create_object_v3_request_instance = EzsigntemplateCreateObjectV3Request.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplateCreateObjectV3Request.to_json())

# convert the object into a dict
ezsigntemplate_create_object_v3_request_dict = ezsigntemplate_create_object_v3_request_instance.to_dict()
# create an instance of EzsigntemplateCreateObjectV3Request from a dict
ezsigntemplate_create_object_v3_request_from_dict = EzsigntemplateCreateObjectV3Request.from_dict(ezsigntemplate_create_object_v3_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


