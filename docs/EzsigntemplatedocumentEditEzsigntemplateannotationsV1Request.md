# EzsigntemplatedocumentEditEzsigntemplateannotationsV1Request

Request for PUT /1/object/ezsigntemplatedocument/{pkiEzsigntemplatedocumentID}/editEzsigntemplateannotations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a_obj_ezsigntemplateannotation** | [**List[EzsigntemplateannotationRequestCompound]**](EzsigntemplateannotationRequestCompound.md) |  | 

## Example

```python
from eZmaxApi.models.ezsigntemplatedocument_edit_ezsigntemplateannotations_v1_request import EzsigntemplatedocumentEditEzsigntemplateannotationsV1Request

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatedocumentEditEzsigntemplateannotationsV1Request from a JSON string
ezsigntemplatedocument_edit_ezsigntemplateannotations_v1_request_instance = EzsigntemplatedocumentEditEzsigntemplateannotationsV1Request.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatedocumentEditEzsigntemplateannotationsV1Request.to_json())

# convert the object into a dict
ezsigntemplatedocument_edit_ezsigntemplateannotations_v1_request_dict = ezsigntemplatedocument_edit_ezsigntemplateannotations_v1_request_instance.to_dict()
# create an instance of EzsigntemplatedocumentEditEzsigntemplateannotationsV1Request from a dict
ezsigntemplatedocument_edit_ezsigntemplateannotations_v1_request_from_dict = EzsigntemplatedocumentEditEzsigntemplateannotationsV1Request.from_dict(ezsigntemplatedocument_edit_ezsigntemplateannotations_v1_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


