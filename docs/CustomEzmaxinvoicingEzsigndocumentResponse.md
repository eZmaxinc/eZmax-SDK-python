# CustomEzmaxinvoicingEzsigndocumentResponse

An EzmaxinvoicingEzsigndocument object containing information about the Ezmaxinvoicing for an Ezsigndocument

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fki_ezsignfolder_id** | **int** | The unique ID of the Ezsignfolder | 
**fki_billingentityinternal_id** | **int** | The unique ID of the Billingentityinternal. | [optional] 
**s_name** | **str** |  | 
**s_ezsignfolder_description** | **str** | The description of the Ezsignfolder | 
**s_ezsigndocument_name** | **str** | The name of the document that will be presented to Ezsignfoldersignerassociations | 
**b_ezsignfolder_allowed** | **bool** | Whether you have access to the Ezsignfolder or not | 

## Example

```python
from eZmaxApi.models.custom_ezmaxinvoicing_ezsigndocument_response import CustomEzmaxinvoicingEzsigndocumentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomEzmaxinvoicingEzsigndocumentResponse from a JSON string
custom_ezmaxinvoicing_ezsigndocument_response_instance = CustomEzmaxinvoicingEzsigndocumentResponse.from_json(json)
# print the JSON string representation of the object
print CustomEzmaxinvoicingEzsigndocumentResponse.to_json()

# convert the object into a dict
custom_ezmaxinvoicing_ezsigndocument_response_dict = custom_ezmaxinvoicing_ezsigndocument_response_instance.to_dict()
# create an instance of CustomEzmaxinvoicingEzsigndocumentResponse from a dict
custom_ezmaxinvoicing_ezsigndocument_response_form_dict = custom_ezmaxinvoicing_ezsigndocument_response.from_dict(custom_ezmaxinvoicing_ezsigndocument_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


