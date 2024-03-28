# EzsigntemplatedocumentRequest

A Ezsigntemplatedocument Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigntemplatedocument_id** | **int** | The unique ID of the Ezsigntemplatedocument | [optional] 
**fki_ezsigntemplate_id** | **int** | The unique ID of the Ezsigntemplate | 
**fki_ezsigndocument_id** | **int** | The unique ID of the Ezsigndocument | [optional] 
**fki_ezsigntemplatesigner_id** | **int** | The unique ID of the Ezsigntemplatesigner | [optional] 
**s_ezsigntemplatedocument_name** | **str** | The name of the Ezsigntemplatedocument. | 
**e_ezsigntemplatedocument_source** | **str** | Indicates where to look for the document binary content. | 
**e_ezsigntemplatedocument_format** | **str** | Indicates the format of the template. | [optional] 
**s_ezsigntemplatedocument_base64** | **bytearray** | The Base64 encoded binary content of the document.  This field is Required when eEzsigntemplatedocumentSource &#x3D; Base64. | [optional] 
**s_ezsigntemplatedocument_url** | **str** | The url where the document content resides.  This field is Required when eEzsigntemplatedocumentSource &#x3D; Url. | [optional] 
**b_ezsigntemplatedocument_forcerepair** | **bool** | Try to repair the document or flatten it if it cannot be used for electronic signature. | [optional] 
**e_ezsigntemplatedocument_form** | **str** | If the document contains an existing PDF form this property must be set.  **Keep** leaves the form as-is in the document.  **Convert** removes the form and convert all the existing fields to Ezsigntemplateformfieldgroups and assign them to the specified **fkiEzsigntemplatesignerID**  **Discard** removes the form from the document | [optional] 
**s_ezsigntemplatedocument_password** | **str** | If the source template is password protected, the password to open/modify it. | [optional] [default to '']

## Example

```python
from eZmaxApi.models.ezsigntemplatedocument_request import EzsigntemplatedocumentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigntemplatedocumentRequest from a JSON string
ezsigntemplatedocument_request_instance = EzsigntemplatedocumentRequest.from_json(json)
# print the JSON string representation of the object
print(EzsigntemplatedocumentRequest.to_json())

# convert the object into a dict
ezsigntemplatedocument_request_dict = ezsigntemplatedocument_request_instance.to_dict()
# create an instance of EzsigntemplatedocumentRequest from a dict
ezsigntemplatedocument_request_form_dict = ezsigntemplatedocument_request.from_dict(ezsigntemplatedocument_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


