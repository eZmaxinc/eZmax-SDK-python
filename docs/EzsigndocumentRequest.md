# EzsigndocumentRequest

An Ezsigndocument Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pki_ezsigndocument_id** | **int** | The unique ID of the Ezsigndocument | [optional] 
**fki_ezsignfolder_id** | **int** | The unique ID of the Ezsignfolder | 
**fki_ezsigntemplate_id** | **int** | The unique ID of the Ezsigntemplate | [optional] 
**fki_ezsignfoldersignerassociation_id** | **int** | The unique ID of the Ezsignfoldersignerassociation | [optional] 
**fki_language_id** | **int** | The unique ID of the Language.  Valid values:  |Value|Description| |-|-| |1|French| |2|English| | 
**e_ezsigndocument_source** | **str** | Indicates where to look for the document binary content. | 
**e_ezsigndocument_format** | **str** | Indicates the format of the document. | [optional] 
**s_ezsigndocument_base64** | **bytearray** | The Base64 encoded binary content of the document.  This field is Required when eEzsigndocumentSource &#x3D; Base64. | [optional] 
**s_ezsigndocument_url** | **str** | The url where the document content resides.  This field is Required when eEzsigndocumentSource &#x3D; Url. | [optional] 
**b_ezsigndocument_forcerepair** | **bool** | Try to repair the document or flatten it if it cannot be used for electronic signature.  | [optional] [default to True]
**s_ezsigndocument_password** | **str** | If the source document is password protected, the password to open/modify it. | [optional] 
**e_ezsigndocument_form** | **str** | If the document contains an existing PDF form this property must be set.  **Keep** leaves the form as-is in the document.  **Convert** removes the form and convert all the existing fields to Ezsignformfieldgroups and assign them to the specified **fkiEzsignfoldersignerassociationID**  **Discard** removes the form from the document. | [optional] 
**dt_ezsigndocument_duedate** | **str** | The maximum date and time at which the Ezsigndocument can be signed. | 
**s_ezsigndocument_name** | **str** | The name of the document that will be presented to Ezsignfoldersignerassociations | 
**s_ezsigndocument_externalid** | **str** | This field can be used to store an External ID from the client&#39;s system.  Anything can be stored in this field, it will never be evaluated by the eZmax system and will be returned AS-IS.  To store multiple values, consider using a JSON formatted structure, a URL encoded string, a CSV or any other custom format.  | [optional] 

## Example

```python
from eZmaxApi.models.ezsigndocument_request import EzsigndocumentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EzsigndocumentRequest from a JSON string
ezsigndocument_request_instance = EzsigndocumentRequest.from_json(json)
# print the JSON string representation of the object
print(EzsigndocumentRequest.to_json())

# convert the object into a dict
ezsigndocument_request_dict = ezsigndocument_request_instance.to_dict()
# create an instance of EzsigndocumentRequest from a dict
ezsigndocument_request_form_dict = ezsigndocument_request.from_dict(ezsigndocument_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


