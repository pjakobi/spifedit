# ./xmlspif.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:08e2cf040babe8a56e872a5bcd494d0d5a961ddf
# Generated 2018-09-01 12:35:40.238672 by PyXB version 1.2.6 using Python 2.7.5.final.0
# Namespace http://www.xmlspif.org/spif

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six
import pyxb.namespace
# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:c4bfe2ec-add2-11e8-90f0-4851b76b36db')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# A holder for module-level binding classes so we can access them from
# inside class definitions where property names may conflict.
_module_typeBindings = pyxb.utils.utility.Object()

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.xmlspif.org/spif', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {http://www.xmlspif.org/spif}version
class version (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'version')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 52, 2)
    _Documentation = '\n        \n      '
version._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=version, enum_prefix=None)
version.n1_0 = version._CF_enumeration.addEnumeration(unicode_value='1.0', tag='n1_0')
version.n2_0 = version._CF_enumeration.addEnumeration(unicode_value='2.0', tag='n2_0')
version.n2_1 = version._CF_enumeration.addEnumeration(unicode_value='2.1', tag='n2_1')
version._InitializeFacetMap(version._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'version', version)
_module_typeBindings.version = version

# Atomic simple type: {http://www.xmlspif.org/spif}oid
class oid (pyxb.binding.datatypes.string):

    """
        
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'oid')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 97, 2)
    _Documentation = '\n        \n      '
oid._CF_pattern = pyxb.binding.facets.CF_pattern()
oid._CF_pattern.addPattern(pattern='[0-2](\\.[0-9]+)+')
oid._InitializeFacetMap(oid._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'oid', oid)
_module_typeBindings.oid = oid

# Atomic simple type: {http://www.xmlspif.org/spif}lacvInt
class lacvInt (pyxb.binding.datatypes.integer):

    """
        
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'lacvInt')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 115, 2)
    _Documentation = '\n        \n      '
lacvInt._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'lacvInt', lacvInt)
_module_typeBindings.lacvInt = lacvInt

# Atomic simple type: {http://www.xmlspif.org/spif}lacvString
class lacvString (pyxb.binding.datatypes.string):

    """
        
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'lacvString')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 126, 2)
    _Documentation = '\n        \n      '
lacvString._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'lacvString', lacvString)
_module_typeBindings.lacvString = lacvString

# Atomic simple type: {http://www.xmlspif.org/spif}selectionInt
class selectionInt (pyxb.binding.datatypes.integer):

    """
        
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'selectionInt')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 154, 2)
    _Documentation = '\n        \n      '
selectionInt._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'selectionInt', selectionInt)
_module_typeBindings.selectionInt = selectionInt

# Atomic simple type: {http://www.xmlspif.org/spif}selectionString
class selectionString (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'selectionString')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 164, 2)
    _Documentation = '\n        \n      '
selectionString._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=selectionString, enum_prefix=None)
selectionString.unbounded = selectionString._CF_enumeration.addEnumeration(unicode_value='unbounded', tag='unbounded')
selectionString._InitializeFacetMap(selectionString._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'selectionString', selectionString)
_module_typeBindings.selectionString = selectionString

# Atomic simple type: {http://www.xmlspif.org/spif}equivalencyAction
class equivalencyAction (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'equivalencyAction')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 189, 2)
    _Documentation = '\n        \n      '
equivalencyAction._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=equivalencyAction, enum_prefix=None)
equivalencyAction.discard = equivalencyAction._CF_enumeration.addEnumeration(unicode_value='discard', tag='discard')
equivalencyAction._InitializeFacetMap(equivalencyAction._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'equivalencyAction', equivalencyAction)
_module_typeBindings.equivalencyAction = equivalencyAction

# Atomic simple type: {http://www.xmlspif.org/spif}operation
class operation (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'operation')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 207, 2)
    _Documentation = '\n        \n      '
operation._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=operation, enum_prefix=None)
operation.onlyOne = operation._CF_enumeration.addEnumeration(unicode_value='onlyOne', tag='onlyOne')
operation.oneOrMore = operation._CF_enumeration.addEnumeration(unicode_value='oneOrMore', tag='oneOrMore')
operation.all = operation._CF_enumeration.addEnumeration(unicode_value='all', tag='all')
operation._InitializeFacetMap(operation._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'operation', operation)
_module_typeBindings.operation = operation

# Atomic simple type: {http://www.xmlspif.org/spif}userInput
class userInput (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'userInput')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 230, 2)
    _Documentation = '\n        \n      '
userInput._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=userInput, enum_prefix=None)
userInput.string = userInput._CF_enumeration.addEnumeration(unicode_value='string', tag='string')
userInput.integer = userInput._CF_enumeration.addEnumeration(unicode_value='integer', tag='integer')
userInput.date = userInput._CF_enumeration.addEnumeration(unicode_value='date', tag='date')
userInput._InitializeFacetMap(userInput._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'userInput', userInput)
_module_typeBindings.userInput = userInput

# Atomic simple type: {http://www.xmlspif.org/spif}hierarchy
class hierarchy (pyxb.binding.datatypes.integer):

    """
        
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'hierarchy')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 253, 2)
    _Documentation = '\n        \n      '
hierarchy._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'hierarchy', hierarchy)
_module_typeBindings.hierarchy = hierarchy

# Atomic simple type: {http://www.xmlspif.org/spif}className
class className (pyxb.binding.datatypes.string):

    """
        
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'className')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 269, 2)
    _Documentation = '\n        \n      '
className._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(256))
className._InitializeFacetMap(className._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'className', className)
_module_typeBindings.className = className

# Atomic simple type: {http://www.xmlspif.org/spif}policyName
class policyName (pyxb.binding.datatypes.string):

    """
        
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'policyName')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 294, 2)
    _Documentation = '\n        \n      '
policyName._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(256))
policyName._InitializeFacetMap(policyName._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'policyName', policyName)
_module_typeBindings.policyName = policyName

# Atomic simple type: {http://www.xmlspif.org/spif}markingPhrase
class markingPhrase (pyxb.binding.datatypes.string):

    """
        
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'markingPhrase')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 308, 2)
    _Documentation = '\n        \n      '
markingPhrase._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(256))
markingPhrase._InitializeFacetMap(markingPhrase._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'markingPhrase', markingPhrase)
_module_typeBindings.markingPhrase = markingPhrase

# Atomic simple type: {http://www.xmlspif.org/spif}tagSetName
class tagSetName (pyxb.binding.datatypes.string):

    """
        
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tagSetName')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 322, 2)
    _Documentation = '\n        \n      '
tagSetName._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(256))
tagSetName._InitializeFacetMap(tagSetName._CF_maxLength)
Namespace.addCategoryObject('typeBinding', 'tagSetName', tagSetName)
_module_typeBindings.tagSetName = tagSetName

# Atomic simple type: {http://www.xmlspif.org/spif}genTime
class genTime (pyxb.binding.datatypes.string):

    """
        
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'genTime')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 335, 2)
    _Documentation = '\n        \n      '
genTime._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'genTime', genTime)
_module_typeBindings.genTime = genTime

# Atomic simple type: {http://www.xmlspif.org/spif}markingCode
class markingCode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'markingCode')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 353, 2)
    _Documentation = '\n        \n      '
markingCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=markingCode, enum_prefix=None)
markingCode.pageTop = markingCode._CF_enumeration.addEnumeration(unicode_value='pageTop', tag='pageTop')
markingCode.pageBottom = markingCode._CF_enumeration.addEnumeration(unicode_value='pageBottom', tag='pageBottom')
markingCode.pageTopBottom = markingCode._CF_enumeration.addEnumeration(unicode_value='pageTopBottom', tag='pageTopBottom')
markingCode.documentStart = markingCode._CF_enumeration.addEnumeration(unicode_value='documentStart', tag='documentStart')
markingCode.documentEnd = markingCode._CF_enumeration.addEnumeration(unicode_value='documentEnd', tag='documentEnd')
markingCode.noNameDisplay = markingCode._CF_enumeration.addEnumeration(unicode_value='noNameDisplay', tag='noNameDisplay')
markingCode.noMarkingDisplay = markingCode._CF_enumeration.addEnumeration(unicode_value='noMarkingDisplay', tag='noMarkingDisplay')
markingCode.suppressClassName = markingCode._CF_enumeration.addEnumeration(unicode_value='suppressClassName', tag='suppressClassName')
markingCode.firstLineOfText = markingCode._CF_enumeration.addEnumeration(unicode_value='firstLineOfText', tag='firstLineOfText')
markingCode.lastLineOfText = markingCode._CF_enumeration.addEnumeration(unicode_value='lastLineOfText', tag='lastLineOfText')
markingCode.subject = markingCode._CF_enumeration.addEnumeration(unicode_value='subject', tag='subject')
markingCode.xHeader = markingCode._CF_enumeration.addEnumeration(unicode_value='xHeader', tag='xHeader')
markingCode.portionMarking = markingCode._CF_enumeration.addEnumeration(unicode_value='portionMarking', tag='portionMarking')
markingCode.inputTitle = markingCode._CF_enumeration.addEnumeration(unicode_value='inputTitle', tag='inputTitle')
markingCode.waterMark = markingCode._CF_enumeration.addEnumeration(unicode_value='waterMark', tag='waterMark')
markingCode.replacePolicy = markingCode._CF_enumeration.addEnumeration(unicode_value='replacePolicy', tag='replacePolicy')
markingCode._InitializeFacetMap(markingCode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'markingCode', markingCode)
_module_typeBindings.markingCode = markingCode

# Atomic simple type: {http://www.xmlspif.org/spif}tagType
class tagType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tagType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 413, 2)
    _Documentation = '\n        \n      '
tagType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=tagType, enum_prefix=None)
tagType.notApplicable = tagType._CF_enumeration.addEnumeration(unicode_value='notApplicable', tag='notApplicable')
tagType.restrictive = tagType._CF_enumeration.addEnumeration(unicode_value='restrictive', tag='restrictive')
tagType.enumerated = tagType._CF_enumeration.addEnumeration(unicode_value='enumerated', tag='enumerated')
tagType.permissive = tagType._CF_enumeration.addEnumeration(unicode_value='permissive', tag='permissive')
tagType.tagType7 = tagType._CF_enumeration.addEnumeration(unicode_value='tagType7', tag='tagType7')
tagType._InitializeFacetMap(tagType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'tagType', tagType)
_module_typeBindings.tagType = tagType

# Atomic simple type: {http://www.xmlspif.org/spif}enumType
class enumType (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'enumType')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 438, 2)
    _Documentation = '\n        \n      '
enumType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=enumType, enum_prefix=None)
enumType.restrictive = enumType._CF_enumeration.addEnumeration(unicode_value='restrictive', tag='restrictive')
enumType.permissive = enumType._CF_enumeration.addEnumeration(unicode_value='permissive', tag='permissive')
enumType._InitializeFacetMap(enumType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'enumType', enumType)
_module_typeBindings.enumType = enumType

# Atomic simple type: {http://www.xmlspif.org/spif}tag7Encoding
class tag7Encoding (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tag7Encoding')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 457, 2)
    _Documentation = '\n        \n      '
tag7Encoding._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=tag7Encoding, enum_prefix=None)
tag7Encoding.bitSetAttributes = tag7Encoding._CF_enumeration.addEnumeration(unicode_value='bitSetAttributes', tag='bitSetAttributes')
tag7Encoding.securityAttributes = tag7Encoding._CF_enumeration.addEnumeration(unicode_value='securityAttributes', tag='securityAttributes')
tag7Encoding._InitializeFacetMap(tag7Encoding._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'tag7Encoding', tag7Encoding)
_module_typeBindings.tag7Encoding = tag7Encoding

# Atomic simple type: {http://www.xmlspif.org/spif}qualifierCode
class qualifierCode (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'qualifierCode')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 477, 2)
    _Documentation = '\n        \n      '
qualifierCode._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=qualifierCode, enum_prefix=None)
qualifierCode.prefix = qualifierCode._CF_enumeration.addEnumeration(unicode_value='prefix', tag='prefix')
qualifierCode.suffix = qualifierCode._CF_enumeration.addEnumeration(unicode_value='suffix', tag='suffix')
qualifierCode.separator = qualifierCode._CF_enumeration.addEnumeration(unicode_value='separator', tag='separator')
qualifierCode._InitializeFacetMap(qualifierCode._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'qualifierCode', qualifierCode)
_module_typeBindings.qualifierCode = qualifierCode

# Atomic simple type: {http://www.xmlspif.org/spif}applied
class applied (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'applied')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 498, 2)
    _Documentation = '\n        \n      '
applied._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=applied, enum_prefix=None)
applied.encrypt = applied._CF_enumeration.addEnumeration(unicode_value='encrypt', tag='encrypt')
applied.decrypt = applied._CF_enumeration.addEnumeration(unicode_value='decrypt', tag='decrypt')
applied.both = applied._CF_enumeration.addEnumeration(unicode_value='both', tag='both')
applied._InitializeFacetMap(applied._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'applied', applied)
_module_typeBindings.applied = applied

# Atomic simple type: {http://www.xmlspif.org/spif}colorW3C
class colorW3C (pyxb.binding.datatypes.string, pyxb.binding.basis.enumeration_mixin):

    """
        
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'colorW3C')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 519, 2)
    _Documentation = '\n        \n      '
colorW3C._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=colorW3C, enum_prefix=None)
colorW3C.aqua = colorW3C._CF_enumeration.addEnumeration(unicode_value='aqua', tag='aqua')
colorW3C.black = colorW3C._CF_enumeration.addEnumeration(unicode_value='black', tag='black')
colorW3C.blue = colorW3C._CF_enumeration.addEnumeration(unicode_value='blue', tag='blue')
colorW3C.fuschia = colorW3C._CF_enumeration.addEnumeration(unicode_value='fuschia', tag='fuschia')
colorW3C.gray = colorW3C._CF_enumeration.addEnumeration(unicode_value='gray', tag='gray')
colorW3C.green = colorW3C._CF_enumeration.addEnumeration(unicode_value='green', tag='green')
colorW3C.lime = colorW3C._CF_enumeration.addEnumeration(unicode_value='lime', tag='lime')
colorW3C.maroon = colorW3C._CF_enumeration.addEnumeration(unicode_value='maroon', tag='maroon')
colorW3C.navy = colorW3C._CF_enumeration.addEnumeration(unicode_value='navy', tag='navy')
colorW3C.olive = colorW3C._CF_enumeration.addEnumeration(unicode_value='olive', tag='olive')
colorW3C.purple = colorW3C._CF_enumeration.addEnumeration(unicode_value='purple', tag='purple')
colorW3C.red = colorW3C._CF_enumeration.addEnumeration(unicode_value='red', tag='red')
colorW3C.silver = colorW3C._CF_enumeration.addEnumeration(unicode_value='silver', tag='silver')
colorW3C.teal = colorW3C._CF_enumeration.addEnumeration(unicode_value='teal', tag='teal')
colorW3C.white = colorW3C._CF_enumeration.addEnumeration(unicode_value='white', tag='white')
colorW3C.yellow = colorW3C._CF_enumeration.addEnumeration(unicode_value='yellow', tag='yellow')
colorW3C._InitializeFacetMap(colorW3C._CF_enumeration)
Namespace.addCategoryObject('typeBinding', 'colorW3C', colorW3C)
_module_typeBindings.colorW3C = colorW3C

# Atomic simple type: {http://www.xmlspif.org/spif}colorRGB
class colorRGB (pyxb.binding.datatypes.string):

    """
        
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'colorRGB')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 547, 2)
    _Documentation = '\n        \n      '
colorRGB._CF_pattern = pyxb.binding.facets.CF_pattern()
colorRGB._CF_pattern.addPattern(pattern='#[0-9a-fA-F]{6}')
colorRGB._InitializeFacetMap(colorRGB._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'colorRGB', colorRGB)
_module_typeBindings.colorRGB = colorRGB

# Union simple type: {http://www.xmlspif.org/spif}lacv
# superclasses pyxb.binding.datatypes.anySimpleType
class lacv (pyxb.binding.basis.STD_union):

    """
        
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'lacv')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 140, 2)
    _Documentation = '\n        \n      '

    _MemberTypes = ( lacvInt, lacvString, )
lacv._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=lacv)
lacv._CF_pattern = pyxb.binding.facets.CF_pattern()
lacv._InitializeFacetMap(lacv._CF_enumeration,
   lacv._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'lacv', lacv)
_module_typeBindings.lacv = lacv

# Union simple type: {http://www.xmlspif.org/spif}selection
# superclasses pyxb.binding.datatypes.anySimpleType
class selection (pyxb.binding.basis.STD_union):

    """
        
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'selection')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 179, 2)
    _Documentation = '\n        \n      '

    _MemberTypes = ( selectionInt, selectionString, )
selection._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=selection)
selection._CF_pattern = pyxb.binding.facets.CF_pattern()
selection.unbounded = 'unbounded'                 # originally selectionString.unbounded
selection._InitializeFacetMap(selection._CF_enumeration,
   selection._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'selection', selection)
_module_typeBindings.selection = selection

# Union simple type: {http://www.xmlspif.org/spif}color
# superclasses pyxb.binding.datatypes.anySimpleType
class color (pyxb.binding.basis.STD_union):

    """
        
      """

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'color')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 560, 2)
    _Documentation = '\n        \n      '

    _MemberTypes = ( colorW3C, colorRGB, )
color._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=color)
color._CF_pattern = pyxb.binding.facets.CF_pattern()
color.aqua = 'aqua'                               # originally colorW3C.aqua
color.black = 'black'                             # originally colorW3C.black
color.blue = 'blue'                               # originally colorW3C.blue
color.fuschia = 'fuschia'                         # originally colorW3C.fuschia
color.gray = 'gray'                               # originally colorW3C.gray
color.green = 'green'                             # originally colorW3C.green
color.lime = 'lime'                               # originally colorW3C.lime
color.maroon = 'maroon'                           # originally colorW3C.maroon
color.navy = 'navy'                               # originally colorW3C.navy
color.olive = 'olive'                             # originally colorW3C.olive
color.purple = 'purple'                           # originally colorW3C.purple
color.red = 'red'                                 # originally colorW3C.red
color.silver = 'silver'                           # originally colorW3C.silver
color.teal = 'teal'                               # originally colorW3C.teal
color.white = 'white'                             # originally colorW3C.white
color.yellow = 'yellow'                           # originally colorW3C.yellow
color._InitializeFacetMap(color._CF_enumeration,
   color._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'color', color)
_module_typeBindings.color = color

# Complex type {http://www.xmlspif.org/spif}updateInfo with content type EMPTY
class updateInfo_ (pyxb.binding.basis.complexTypeDefinition):
    """
        
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'updateInfo')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 659, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.updateInfo_ = updateInfo_
Namespace.addCategoryObject('typeBinding', 'updateInfo', updateInfo_)


# Complex type {http://www.xmlspif.org/spif}equivalentPolicies with content type ELEMENT_ONLY
class equivalentPolicies_ (pyxb.binding.basis.complexTypeDefinition):
    """
        
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'equivalentPolicies')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 743, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xmlspif.org/spif}equivalentPolicy uses Python identifier equivalentPolicy
    __equivalentPolicy = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'equivalentPolicy'), 'equivalentPolicy', '__httpwww_xmlspif_orgspif_equivalentPolicies__httpwww_xmlspif_orgspifequivalentPolicy', True, pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 733, 2), )

    
    equivalentPolicy = property(__equivalentPolicy.value, __equivalentPolicy.set, None, '\n        \n      ')

    _ElementMap.update({
        __equivalentPolicy.name() : __equivalentPolicy
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.equivalentPolicies_ = equivalentPolicies_
Namespace.addCategoryObject('typeBinding', 'equivalentPolicies', equivalentPolicies_)


# Complex type {http://www.xmlspif.org/spif}privacyMark with content type ELEMENT_ONLY
class privacyMark_ (pyxb.binding.basis.complexTypeDefinition):
    """
        
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'privacyMark')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 769, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xmlspif.org/spif}markingData uses Python identifier markingData
    __markingData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'markingData'), 'markingData', '__httpwww_xmlspif_orgspif_privacyMark__httpwww_xmlspif_orgspifmarkingData', True, pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 862, 2), )

    
    markingData = property(__markingData.value, __markingData.set, None, '\n        \n      ')

    
    # Element {http://www.xmlspif.org/spif}markingQualifier uses Python identifier markingQualifier
    __markingQualifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'markingQualifier'), 'markingQualifier', '__httpwww_xmlspif_orgspif_privacyMark__httpwww_xmlspif_orgspifmarkingQualifier', True, pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1095, 2), )

    
    markingQualifier = property(__markingQualifier.value, __markingQualifier.set, None, '\n        \n      ')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_xmlspif_orgspif_privacyMark__name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 790, 4)
    __name._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 790, 4)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute obsolete uses Python identifier obsolete
    __obsolete = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'obsolete'), 'obsolete', '__httpwww_xmlspif_orgspif_privacyMark__obsolete', pyxb.binding.datatypes.boolean, unicode_default='false')
    __obsolete._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 791, 4)
    __obsolete._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 791, 4)
    
    obsolete = property(__obsolete.value, __obsolete.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        __markingData.name() : __markingData,
        __markingQualifier.name() : __markingQualifier
    })
    _AttributeMap.update({
        __name.name() : __name,
        __obsolete.name() : __obsolete
    })
_module_typeBindings.privacyMark_ = privacyMark_
Namespace.addCategoryObject('typeBinding', 'privacyMark', privacyMark_)


# Complex type {http://www.xmlspif.org/spif}securityClassifications with content type ELEMENT_ONLY
class securityClassifications_ (pyxb.binding.basis.complexTypeDefinition):
    """
        
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'securityClassifications')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 915, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xmlspif.org/spif}markingData uses Python identifier markingData
    __markingData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'markingData'), 'markingData', '__httpwww_xmlspif_orgspif_securityClassifications__httpwww_xmlspif_orgspifmarkingData', True, pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 862, 2), )

    
    markingData = property(__markingData.value, __markingData.set, None, '\n        \n      ')

    
    # Element {http://www.xmlspif.org/spif}securityClassification uses Python identifier securityClassification
    __securityClassification = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'securityClassification'), 'securityClassification', '__httpwww_xmlspif_orgspif_securityClassifications__httpwww_xmlspif_orgspifsecurityClassification', True, pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 905, 2), )

    
    securityClassification = property(__securityClassification.value, __securityClassification.set, None, '\n        \n      ')

    
    # Element {http://www.xmlspif.org/spif}markingQualifier uses Python identifier markingQualifier
    __markingQualifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'markingQualifier'), 'markingQualifier', '__httpwww_xmlspif_orgspif_securityClassifications__httpwww_xmlspif_orgspifmarkingQualifier', True, pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1095, 2), )

    
    markingQualifier = property(__markingQualifier.value, __markingQualifier.set, None, '\n        \n      ')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_xmlspif_orgspif_securityClassifications__name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 938, 4)
    __name._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 938, 4)
    
    name = property(__name.value, __name.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        __markingData.name() : __markingData,
        __securityClassification.name() : __securityClassification,
        __markingQualifier.name() : __markingQualifier
    })
    _AttributeMap.update({
        __name.name() : __name
    })
_module_typeBindings.securityClassifications_ = securityClassifications_
Namespace.addCategoryObject('typeBinding', 'securityClassifications', securityClassifications_)


# Complex type {http://www.xmlspif.org/spif}securityCategoryTagSets with content type ELEMENT_ONLY
class securityCategoryTagSets_ (pyxb.binding.basis.complexTypeDefinition):
    """
        
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'securityCategoryTagSets')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1218, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xmlspif.org/spif}securityCategoryTagSet uses Python identifier securityCategoryTagSet
    __securityCategoryTagSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'securityCategoryTagSet'), 'securityCategoryTagSet', '__httpwww_xmlspif_orgspif_securityCategoryTagSets__httpwww_xmlspif_orgspifsecurityCategoryTagSet', True, pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1173, 2), )

    
    securityCategoryTagSet = property(__securityCategoryTagSet.value, __securityCategoryTagSet.set, None, '\n        \n      ')

    _ElementMap.update({
        __securityCategoryTagSet.name() : __securityCategoryTagSet
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.securityCategoryTagSets_ = securityCategoryTagSets_
Namespace.addCategoryObject('typeBinding', 'securityCategoryTagSets', securityCategoryTagSets_)


# Complex type {http://www.xmlspif.org/spif}extensions with content type ELEMENT_ONLY
class extensions_ (pyxb.binding.basis.complexTypeDefinition):
    """
        
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'extensions')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1286, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
_module_typeBindings.extensions_ = extensions_
Namespace.addCategoryObject('typeBinding', 'extensions', extensions_)


# Complex type {http://www.xmlspif.org/spif}optionalCategoryGroup with content type ELEMENT_ONLY
class optionalCategoryGroup (pyxb.binding.basis.complexTypeDefinition):
    """
        
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'optionalCategoryGroup')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 629, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xmlspif.org/spif}categoryGroup uses Python identifier categoryGroup
    __categoryGroup = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'categoryGroup'), 'categoryGroup', '__httpwww_xmlspif_orgspif_optionalCategoryGroup_httpwww_xmlspif_orgspifcategoryGroup', True, pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 610, 2), )

    
    categoryGroup = property(__categoryGroup.value, __categoryGroup.set, None, '\n        \n      ')

    
    # Attribute operation uses Python identifier operation
    __operation = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'operation'), 'operation', '__httpwww_xmlspif_orgspif_optionalCategoryGroup_operation', _module_typeBindings.operation, required=True)
    __operation._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 646, 4)
    __operation._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 646, 4)
    
    operation = property(__operation.value, __operation.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        __categoryGroup.name() : __categoryGroup
    })
    _AttributeMap.update({
        __operation.name() : __operation
    })
_module_typeBindings.optionalCategoryGroup = optionalCategoryGroup
Namespace.addCategoryObject('typeBinding', 'optionalCategoryGroup', optionalCategoryGroup)


# Complex type {http://www.xmlspif.org/spif}equivalentClassification with content type ELEMENT_ONLY
class equivalentClassification_ (pyxb.binding.basis.complexTypeDefinition):
    """
        
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'equivalentClassification')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 670, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xmlspif.org/spif}requiredCategory uses Python identifier requiredCategory
    __requiredCategory = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'requiredCategory'), 'requiredCategory', '__httpwww_xmlspif_orgspif_equivalentClassification__httpwww_xmlspif_orgspifrequiredCategory', True, pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 649, 2), )

    
    requiredCategory = property(__requiredCategory.value, __requiredCategory.set, None, '\n        \n      ')

    
    # Attribute policyRef uses Python identifier policyRef
    __policyRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'policyRef'), 'policyRef', '__httpwww_xmlspif_orgspif_equivalentClassification__policyRef', _module_typeBindings.policyName, required=True)
    __policyRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 691, 4)
    __policyRef._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 691, 4)
    
    policyRef = property(__policyRef.value, __policyRef.set, None, None)

    
    # Attribute lacv uses Python identifier lacv
    __lacv = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lacv'), 'lacv', '__httpwww_xmlspif_orgspif_equivalentClassification__lacv', _module_typeBindings.lacvInt, required=True)
    __lacv._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 692, 4)
    __lacv._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 692, 4)
    
    lacv = property(__lacv.value, __lacv.set, None, None)

    
    # Attribute applied uses Python identifier applied
    __applied = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'applied'), 'applied', '__httpwww_xmlspif_orgspif_equivalentClassification__applied', _module_typeBindings.applied, required=True)
    __applied._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 693, 4)
    __applied._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 693, 4)
    
    applied = property(__applied.value, __applied.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        __requiredCategory.name() : __requiredCategory
    })
    _AttributeMap.update({
        __policyRef.name() : __policyRef,
        __lacv.name() : __lacv,
        __applied.name() : __applied
    })
_module_typeBindings.equivalentClassification_ = equivalentClassification_
Namespace.addCategoryObject('typeBinding', 'equivalentClassification', equivalentClassification_)


# Complex type {http://www.xmlspif.org/spif}equivalentPolicy with content type ELEMENT_ONLY
class equivalentPolicy_ (pyxb.binding.basis.complexTypeDefinition):
    """
        
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'equivalentPolicy')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 706, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xmlspif.org/spif}requiredCategory uses Python identifier requiredCategory
    __requiredCategory = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'requiredCategory'), 'requiredCategory', '__httpwww_xmlspif_orgspif_equivalentPolicy__httpwww_xmlspif_orgspifrequiredCategory', True, pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 649, 2), )

    
    requiredCategory = property(__requiredCategory.value, __requiredCategory.set, None, '\n        \n      ')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_xmlspif_orgspif_equivalentPolicy__name', _module_typeBindings.policyName, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 727, 4)
    __name._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 727, 4)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xmlspif_orgspif_equivalentPolicy__id', _module_typeBindings.oid, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 728, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 728, 4)
    
    id = property(__id.value, __id.set, None, None)

    
    # Attribute userRefURI uses Python identifier userRefURI
    __userRefURI = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'userRefURI'), 'userRefURI', '__httpwww_xmlspif_orgspif_equivalentPolicy__userRefURI', pyxb.binding.datatypes.anyURI)
    __userRefURI._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 729, 4)
    __userRefURI._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 729, 4)
    
    userRefURI = property(__userRefURI.value, __userRefURI.set, None, None)

    
    # Attribute docRefURI uses Python identifier docRefURI
    __docRefURI = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'docRefURI'), 'docRefURI', '__httpwww_xmlspif_orgspif_equivalentPolicy__docRefURI', pyxb.binding.datatypes.anyURI)
    __docRefURI._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 730, 4)
    __docRefURI._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 730, 4)
    
    docRefURI = property(__docRefURI.value, __docRefURI.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        __requiredCategory.name() : __requiredCategory
    })
    _AttributeMap.update({
        __name.name() : __name,
        __id.name() : __id,
        __userRefURI.name() : __userRefURI,
        __docRefURI.name() : __docRefURI
    })
_module_typeBindings.equivalentPolicy_ = equivalentPolicy_
Namespace.addCategoryObject('typeBinding', 'equivalentPolicy', equivalentPolicy_)


# Complex type {http://www.xmlspif.org/spif}markingData with content type ELEMENT_ONLY
class markingData_ (pyxb.binding.basis.complexTypeDefinition):
    """
        
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'markingData')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 842, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xmlspif.org/spif}code uses Python identifier code
    __code = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'code'), 'code', '__httpwww_xmlspif_orgspif_markingData__httpwww_xmlspif_orgspifcode', True, pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 403, 2), )

    
    code = property(__code.value, __code.set, None, '\n        \n      ')

    
    # Attribute phrase uses Python identifier phrase
    __phrase = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'phrase'), 'phrase', '__httpwww_xmlspif_orgspif_markingData__phrase', _module_typeBindings.markingPhrase)
    __phrase._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 859, 4)
    __phrase._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 859, 4)
    
    phrase = property(__phrase.value, __phrase.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        __code.name() : __code
    })
    _AttributeMap.update({
        __phrase.name() : __phrase
    })
_module_typeBindings.markingData_ = markingData_
Namespace.addCategoryObject('typeBinding', 'markingData', markingData_)


# Complex type {http://www.xmlspif.org/spif}qualifier with content type EMPTY
class qualifier_ (pyxb.binding.basis.complexTypeDefinition):
    """
        
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'qualifier')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1049, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute markingQualifier uses Python identifier markingQualifier
    __markingQualifier = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'markingQualifier'), 'markingQualifier', '__httpwww_xmlspif_orgspif_qualifier__markingQualifier', _module_typeBindings.markingPhrase, required=True)
    __markingQualifier._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1062, 4)
    __markingQualifier._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1062, 4)
    
    markingQualifier = property(__markingQualifier.value, __markingQualifier.set, None, None)

    
    # Attribute qualifierCode uses Python identifier qualifierCode
    __qualifierCode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'qualifierCode'), 'qualifierCode', '__httpwww_xmlspif_orgspif_qualifier__qualifierCode', _module_typeBindings.qualifierCode, required=True)
    __qualifierCode._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1063, 4)
    __qualifierCode._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1063, 4)
    
    qualifierCode = property(__qualifierCode.value, __qualifierCode.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __markingQualifier.name() : __markingQualifier,
        __qualifierCode.name() : __qualifierCode
    })
_module_typeBindings.qualifier_ = qualifier_
Namespace.addCategoryObject('typeBinding', 'qualifier', qualifier_)


# Complex type {http://www.xmlspif.org/spif}markingQualifier with content type ELEMENT_ONLY
class markingQualifier_ (pyxb.binding.basis.complexTypeDefinition):
    """
        
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'markingQualifier')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1076, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xmlspif.org/spif}qualifier uses Python identifier qualifier
    __qualifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'qualifier'), 'qualifier', '__httpwww_xmlspif_orgspif_markingQualifier__httpwww_xmlspif_orgspifqualifier', True, pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1066, 2), )

    
    qualifier = property(__qualifier.value, __qualifier.set, None, '\n        \n      ')

    
    # Attribute markingCode uses Python identifier markingCode
    __markingCode = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'markingCode'), 'markingCode', '__httpwww_xmlspif_orgspif_markingQualifier__markingCode', _module_typeBindings.markingCode)
    __markingCode._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1092, 4)
    __markingCode._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1092, 4)
    
    markingCode = property(__markingCode.value, __markingCode.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        __qualifier.name() : __qualifier
    })
    _AttributeMap.update({
        __markingCode.name() : __markingCode
    })
_module_typeBindings.markingQualifier_ = markingQualifier_
Namespace.addCategoryObject('typeBinding', 'markingQualifier', markingQualifier_)


# Complex type {http://www.xmlspif.org/spif}securityCategoryTagSet with content type ELEMENT_ONLY
class securityCategoryTagSet_ (pyxb.binding.basis.complexTypeDefinition):
    """
        
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'securityCategoryTagSet')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1150, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xmlspif.org/spif}securityCategoryTag uses Python identifier securityCategoryTag
    __securityCategoryTag = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'securityCategoryTag'), 'securityCategoryTag', '__httpwww_xmlspif_orgspif_securityCategoryTagSet__httpwww_xmlspif_orgspifsecurityCategoryTag', True, pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1140, 2), )

    
    securityCategoryTag = property(__securityCategoryTag.value, __securityCategoryTag.set, None, '\n        \n      ')

    
    # Element {http://www.xmlspif.org/spif}equivalentSecurityCategoryTagSet uses Python identifier equivalentSecurityCategoryTagSet
    __equivalentSecurityCategoryTagSet = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'equivalentSecurityCategoryTagSet'), 'equivalentSecurityCategoryTagSet', '__httpwww_xmlspif_orgspif_securityCategoryTagSet__httpwww_xmlspif_orgspifequivalentSecurityCategoryTagSet', True, pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1207, 2), )

    
    equivalentSecurityCategoryTagSet = property(__equivalentSecurityCategoryTagSet.value, __equivalentSecurityCategoryTagSet.set, None, '\n        \n      ')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_xmlspif_orgspif_securityCategoryTagSet__name', _module_typeBindings.tagSetName, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1169, 4)
    __name._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1169, 4)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xmlspif_orgspif_securityCategoryTagSet__id', _module_typeBindings.oid, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1170, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1170, 4)
    
    id = property(__id.value, __id.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        __securityCategoryTag.name() : __securityCategoryTag,
        __equivalentSecurityCategoryTagSet.name() : __equivalentSecurityCategoryTagSet
    })
    _AttributeMap.update({
        __name.name() : __name,
        __id.name() : __id
    })
_module_typeBindings.securityCategoryTagSet_ = securityCategoryTagSet_
Namespace.addCategoryObject('typeBinding', 'securityCategoryTagSet', securityCategoryTagSet_)


# Complex type {http://www.xmlspif.org/spif}equivalentSecurityCategoryTagSet with content type ELEMENT_ONLY
class equivalentSecurityCategoryTagSet_ (pyxb.binding.basis.complexTypeDefinition):
    """
        
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'equivalentSecurityCategoryTagSet')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1184, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xmlspif.org/spif}requiredCategory uses Python identifier requiredCategory
    __requiredCategory = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'requiredCategory'), 'requiredCategory', '__httpwww_xmlspif_orgspif_equivalentSecurityCategoryTagSet__httpwww_xmlspif_orgspifrequiredCategory', True, pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 649, 2), )

    
    requiredCategory = property(__requiredCategory.value, __requiredCategory.set, None, '\n        \n      ')

    
    # Attribute policyRef uses Python identifier policyRef
    __policyRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'policyRef'), 'policyRef', '__httpwww_xmlspif_orgspif_equivalentSecurityCategoryTagSet__policyRef', _module_typeBindings.policyName, required=True)
    __policyRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1202, 4)
    __policyRef._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1202, 4)
    
    policyRef = property(__policyRef.value, __policyRef.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_xmlspif_orgspif_equivalentSecurityCategoryTagSet__name', _module_typeBindings.tagSetName)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1203, 4)
    __name._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1203, 4)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xmlspif_orgspif_equivalentSecurityCategoryTagSet__id', _module_typeBindings.oid)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1204, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1204, 4)
    
    id = property(__id.value, __id.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        __requiredCategory.name() : __requiredCategory
    })
    _AttributeMap.update({
        __policyRef.name() : __policyRef,
        __name.name() : __name,
        __id.name() : __id
    })
_module_typeBindings.equivalentSecurityCategoryTagSet_ = equivalentSecurityCategoryTagSet_
Namespace.addCategoryObject('typeBinding', 'equivalentSecurityCategoryTagSet', equivalentSecurityCategoryTagSet_)


# Complex type {http://www.xmlspif.org/spif}objectIdData with content type ELEMENT_ONLY
class objectIdData (pyxb.binding.basis.complexTypeDefinition):
    """
        
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'objectIdData')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1244, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xmlspif.org/spif}markingData uses Python identifier markingData
    __markingData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'markingData'), 'markingData', '__httpwww_xmlspif_orgspif_objectIdData_httpwww_xmlspif_orgspifmarkingData', True, pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 862, 2), )

    
    markingData = property(__markingData.value, __markingData.set, None, '\n        \n      ')

    
    # Element {http://www.xmlspif.org/spif}markingQualifier uses Python identifier markingQualifier
    __markingQualifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'markingQualifier'), 'markingQualifier', '__httpwww_xmlspif_orgspif_objectIdData_httpwww_xmlspif_orgspifmarkingQualifier', True, pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1095, 2), )

    
    markingQualifier = property(__markingQualifier.value, __markingQualifier.set, None, '\n        \n      ')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_xmlspif_orgspif_objectIdData_name', _module_typeBindings.policyName, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1263, 4)
    __name._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1263, 4)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute id uses Python identifier id
    __id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'id'), 'id', '__httpwww_xmlspif_orgspif_objectIdData_id', _module_typeBindings.oid, required=True)
    __id._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1264, 4)
    __id._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1264, 4)
    
    id = property(__id.value, __id.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        __markingData.name() : __markingData,
        __markingQualifier.name() : __markingQualifier
    })
    _AttributeMap.update({
        __name.name() : __name,
        __id.name() : __id
    })
_module_typeBindings.objectIdData = objectIdData
Namespace.addCategoryObject('typeBinding', 'objectIdData', objectIdData)


# Complex type [anonymous] with content type ELEMENT_ONLY
class CTD_ANON (pyxb.binding.basis.complexTypeDefinition):
    """
        
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = None
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1352, 4)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xmlspif.org/spif}updateInfo uses Python identifier updateInfo
    __updateInfo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'updateInfo'), 'updateInfo', '__httpwww_xmlspif_orgspif_CTD_ANON_httpwww_xmlspif_orgspifupdateInfo', False, pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 668, 2), )

    
    updateInfo = property(__updateInfo.value, __updateInfo.set, None, None)

    
    # Element {http://www.xmlspif.org/spif}equivalentPolicies uses Python identifier equivalentPolicies
    __equivalentPolicies = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'equivalentPolicies'), 'equivalentPolicies', '__httpwww_xmlspif_orgspif_CTD_ANON_httpwww_xmlspif_orgspifequivalentPolicies', False, pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 759, 2), )

    
    equivalentPolicies = property(__equivalentPolicies.value, __equivalentPolicies.set, None, '\n        \n      ')

    
    # Element {http://www.xmlspif.org/spif}privacyMarks uses Python identifier privacyMarks
    __privacyMarks = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'privacyMarks'), 'privacyMarks', '__httpwww_xmlspif_orgspif_CTD_ANON_httpwww_xmlspif_orgspifprivacyMarks', False, pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 832, 2), )

    
    privacyMarks = property(__privacyMarks.value, __privacyMarks.set, None, '\n        \n      ')

    
    # Element {http://www.xmlspif.org/spif}markingData uses Python identifier markingData
    __markingData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'markingData'), 'markingData', '__httpwww_xmlspif_orgspif_CTD_ANON_httpwww_xmlspif_orgspifmarkingData', True, pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 862, 2), )

    
    markingData = property(__markingData.value, __markingData.set, None, '\n        \n      ')

    
    # Element {http://www.xmlspif.org/spif}securityClassifications uses Python identifier securityClassifications
    __securityClassifications = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'securityClassifications'), 'securityClassifications', '__httpwww_xmlspif_orgspif_CTD_ANON_httpwww_xmlspif_orgspifsecurityClassifications', False, pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 942, 2), )

    
    securityClassifications = property(__securityClassifications.value, __securityClassifications.set, None, '\n        \n      ')

    
    # Element {http://www.xmlspif.org/spif}markingQualifier uses Python identifier markingQualifier
    __markingQualifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'markingQualifier'), 'markingQualifier', '__httpwww_xmlspif_orgspif_CTD_ANON_httpwww_xmlspif_orgspifmarkingQualifier', True, pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1095, 2), )

    
    markingQualifier = property(__markingQualifier.value, __markingQualifier.set, None, '\n        \n      ')

    
    # Element {http://www.xmlspif.org/spif}securityCategoryTagSets uses Python identifier securityCategoryTagSets
    __securityCategoryTagSets = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'securityCategoryTagSets'), 'securityCategoryTagSets', '__httpwww_xmlspif_orgspif_CTD_ANON_httpwww_xmlspif_orgspifsecurityCategoryTagSets', False, pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1234, 2), )

    
    securityCategoryTagSets = property(__securityCategoryTagSets.value, __securityCategoryTagSets.set, None, '\n        \n      ')

    
    # Element {http://www.xmlspif.org/spif}defaultSecurityPolicyId uses Python identifier defaultSecurityPolicyId
    __defaultSecurityPolicyId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'defaultSecurityPolicyId'), 'defaultSecurityPolicyId', '__httpwww_xmlspif_orgspif_CTD_ANON_httpwww_xmlspif_orgspifdefaultSecurityPolicyId', False, pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1267, 2), )

    
    defaultSecurityPolicyId = property(__defaultSecurityPolicyId.value, __defaultSecurityPolicyId.set, None, '\n        \n      ')

    
    # Element {http://www.xmlspif.org/spif}securityPolicyId uses Python identifier securityPolicyId
    __securityPolicyId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'securityPolicyId'), 'securityPolicyId', '__httpwww_xmlspif_orgspif_CTD_ANON_httpwww_xmlspif_orgspifsecurityPolicyId', False, pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1276, 2), )

    
    securityPolicyId = property(__securityPolicyId.value, __securityPolicyId.set, None, '\n        \n      ')

    
    # Element {http://www.xmlspif.org/spif}extensions uses Python identifier extensions
    __extensions = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'extensions'), 'extensions', '__httpwww_xmlspif_orgspif_CTD_ANON_httpwww_xmlspif_orgspifextensions', False, pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1298, 2), )

    
    extensions = property(__extensions.value, __extensions.set, None, '\n        \n      ')

    
    # Attribute notBefore uses Python identifier notBefore
    __notBefore = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'notBefore'), 'notBefore', '__httpwww_xmlspif_orgspif_CTD_ANON_notBefore', pyxb.binding.datatypes.dateTime)
    __notBefore._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 579, 4)
    __notBefore._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 579, 4)
    
    notBefore = property(__notBefore.value, __notBefore.set, None, None)

    
    # Attribute notAfter uses Python identifier notAfter
    __notAfter = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'notAfter'), 'notAfter', '__httpwww_xmlspif_orgspif_CTD_ANON_notAfter', pyxb.binding.datatypes.dateTime)
    __notAfter._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 580, 4)
    __notAfter._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 580, 4)
    
    notAfter = property(__notAfter.value, __notAfter.set, None, None)

    
    # Attribute schemaVersion uses Python identifier schemaVersion
    __schemaVersion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'schemaVersion'), 'schemaVersion', '__httpwww_xmlspif_orgspif_CTD_ANON_schemaVersion', _module_typeBindings.version, required=True)
    __schemaVersion._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1367, 6)
    __schemaVersion._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1367, 6)
    
    schemaVersion = property(__schemaVersion.value, __schemaVersion.set, None, None)

    
    # Attribute version uses Python identifier version
    __version = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'version'), 'version', '__httpwww_xmlspif_orgspif_CTD_ANON_version', pyxb.binding.datatypes.integer, unicode_default='1')
    __version._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1368, 6)
    __version._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1368, 6)
    
    version = property(__version.value, __version.set, None, None)

    
    # Attribute creationDate uses Python identifier creationDate
    __creationDate = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'creationDate'), 'creationDate', '__httpwww_xmlspif_orgspif_CTD_ANON_creationDate', _module_typeBindings.genTime, required=True)
    __creationDate._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1369, 6)
    __creationDate._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1369, 6)
    
    creationDate = property(__creationDate.value, __creationDate.set, None, None)

    
    # Attribute originatorDN uses Python identifier originatorDN
    __originatorDN = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'originatorDN'), 'originatorDN', '__httpwww_xmlspif_orgspif_CTD_ANON_originatorDN', pyxb.binding.datatypes.string, required=True)
    __originatorDN._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1370, 6)
    __originatorDN._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1370, 6)
    
    originatorDN = property(__originatorDN.value, __originatorDN.set, None, None)

    
    # Attribute keyIdentifier uses Python identifier keyIdentifier
    __keyIdentifier = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'keyIdentifier'), 'keyIdentifier', '__httpwww_xmlspif_orgspif_CTD_ANON_keyIdentifier', pyxb.binding.datatypes.string, required=True)
    __keyIdentifier._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1371, 6)
    __keyIdentifier._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1371, 6)
    
    keyIdentifier = property(__keyIdentifier.value, __keyIdentifier.set, None, None)

    
    # Attribute privilegeId uses Python identifier privilegeId
    __privilegeId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'privilegeId'), 'privilegeId', '__httpwww_xmlspif_orgspif_CTD_ANON_privilegeId', _module_typeBindings.oid, required=True)
    __privilegeId._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1372, 6)
    __privilegeId._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1372, 6)
    
    privilegeId = property(__privilegeId.value, __privilegeId.set, None, None)

    
    # Attribute rbacId uses Python identifier rbacId
    __rbacId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'rbacId'), 'rbacId', '__httpwww_xmlspif_orgspif_CTD_ANON_rbacId', _module_typeBindings.oid, required=True)
    __rbacId._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1373, 6)
    __rbacId._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1373, 6)
    
    rbacId = property(__rbacId.value, __rbacId.set, None, None)

    
    # Attribute userRefURI uses Python identifier userRefURI
    __userRefURI = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'userRefURI'), 'userRefURI', '__httpwww_xmlspif_orgspif_CTD_ANON_userRefURI', pyxb.binding.datatypes.anyURI)
    __userRefURI._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1374, 6)
    __userRefURI._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1374, 6)
    
    userRefURI = property(__userRefURI.value, __userRefURI.set, None, None)

    
    # Attribute docRefURI uses Python identifier docRefURI
    __docRefURI = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'docRefURI'), 'docRefURI', '__httpwww_xmlspif_orgspif_CTD_ANON_docRefURI', pyxb.binding.datatypes.anyURI)
    __docRefURI._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1375, 6)
    __docRefURI._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1375, 6)
    
    docRefURI = property(__docRefURI.value, __docRefURI.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        __updateInfo.name() : __updateInfo,
        __equivalentPolicies.name() : __equivalentPolicies,
        __privacyMarks.name() : __privacyMarks,
        __markingData.name() : __markingData,
        __securityClassifications.name() : __securityClassifications,
        __markingQualifier.name() : __markingQualifier,
        __securityCategoryTagSets.name() : __securityCategoryTagSets,
        __defaultSecurityPolicyId.name() : __defaultSecurityPolicyId,
        __securityPolicyId.name() : __securityPolicyId,
        __extensions.name() : __extensions
    })
    _AttributeMap.update({
        __notBefore.name() : __notBefore,
        __notAfter.name() : __notAfter,
        __schemaVersion.name() : __schemaVersion,
        __version.name() : __version,
        __creationDate.name() : __creationDate,
        __originatorDN.name() : __originatorDN,
        __keyIdentifier.name() : __keyIdentifier,
        __privilegeId.name() : __privilegeId,
        __rbacId.name() : __rbacId,
        __userRefURI.name() : __userRefURI,
        __docRefURI.name() : __docRefURI
    })
_module_typeBindings.CTD_ANON = CTD_ANON


# Complex type {http://www.xmlspif.org/spif}optionalCategoryData with content type EMPTY
class optionalCategoryData (pyxb.binding.basis.complexTypeDefinition):
    """
        
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'optionalCategoryData')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 584, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute tagSetRef uses Python identifier tagSetRef
    __tagSetRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tagSetRef'), 'tagSetRef', '__httpwww_xmlspif_orgspif_optionalCategoryData_tagSetRef', _module_typeBindings.tagSetName, required=True)
    __tagSetRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 602, 4)
    __tagSetRef._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 602, 4)
    
    tagSetRef = property(__tagSetRef.value, __tagSetRef.set, None, None)

    
    # Attribute tagType uses Python identifier tagType
    __tagType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tagType'), 'tagType', '__httpwww_xmlspif_orgspif_optionalCategoryData_tagType', _module_typeBindings.tagType, required=True)
    __tagType._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 603, 4)
    __tagType._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 603, 4)
    
    tagType = property(__tagType.value, __tagType.set, None, None)

    
    # Attribute enumType uses Python identifier enumType
    __enumType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'enumType'), 'enumType', '__httpwww_xmlspif_orgspif_optionalCategoryData_enumType', _module_typeBindings.enumType)
    __enumType._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 604, 4)
    __enumType._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 604, 4)
    
    enumType = property(__enumType.value, __enumType.set, None, None)

    
    # Attribute lacv uses Python identifier lacv
    __lacv = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lacv'), 'lacv', '__httpwww_xmlspif_orgspif_optionalCategoryData_lacv', _module_typeBindings.lacv)
    __lacv._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 605, 4)
    __lacv._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 605, 4)
    
    lacv = property(__lacv.value, __lacv.set, None, None)

    
    # Attribute all uses Python identifier all
    __all = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'all'), 'all', '__httpwww_xmlspif_orgspif_optionalCategoryData_all', pyxb.binding.datatypes.boolean)
    __all._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 607, 4)
    __all._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 607, 4)
    
    all = property(__all.value, __all.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __tagSetRef.name() : __tagSetRef,
        __tagType.name() : __tagType,
        __enumType.name() : __enumType,
        __lacv.name() : __lacv,
        __all.name() : __all
    })
_module_typeBindings.optionalCategoryData = optionalCategoryData
Namespace.addCategoryObject('typeBinding', 'optionalCategoryData', optionalCategoryData)


# Complex type {http://www.xmlspif.org/spif}privacyMarks with content type ELEMENT_ONLY
class privacyMarks_ (pyxb.binding.basis.complexTypeDefinition):
    """
        
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'privacyMarks')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 804, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xmlspif.org/spif}privacyMark uses Python identifier privacyMark
    __privacyMark = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'privacyMark'), 'privacyMark', '__httpwww_xmlspif_orgspif_privacyMarks__httpwww_xmlspif_orgspifprivacyMark', True, pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 794, 2), )

    
    privacyMark = property(__privacyMark.value, __privacyMark.set, None, '\n        \n      ')

    
    # Element {http://www.xmlspif.org/spif}markingData uses Python identifier markingData
    __markingData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'markingData'), 'markingData', '__httpwww_xmlspif_orgspif_privacyMarks__httpwww_xmlspif_orgspifmarkingData', True, pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 862, 2), )

    
    markingData = property(__markingData.value, __markingData.set, None, '\n        \n      ')

    
    # Element {http://www.xmlspif.org/spif}markingQualifier uses Python identifier markingQualifier
    __markingQualifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'markingQualifier'), 'markingQualifier', '__httpwww_xmlspif_orgspif_privacyMarks__httpwww_xmlspif_orgspifmarkingQualifier', True, pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1095, 2), )

    
    markingQualifier = property(__markingQualifier.value, __markingQualifier.set, None, '\n        \n      ')

    
    # Attribute maxSelection uses Python identifier maxSelection
    __maxSelection = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'maxSelection'), 'maxSelection', '__httpwww_xmlspif_orgspif_privacyMarks__maxSelection', _module_typeBindings.selection, unicode_default='unbounded')
    __maxSelection._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 828, 4)
    __maxSelection._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 828, 4)
    
    maxSelection = property(__maxSelection.value, __maxSelection.set, None, None)

    
    # Attribute minSelection uses Python identifier minSelection
    __minSelection = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'minSelection'), 'minSelection', '__httpwww_xmlspif_orgspif_privacyMarks__minSelection', _module_typeBindings.selection, unicode_default='unbounded')
    __minSelection._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 829, 4)
    __minSelection._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 829, 4)
    
    minSelection = property(__minSelection.value, __minSelection.set, None, None)

    _ElementMap.update({
        __privacyMark.name() : __privacyMark,
        __markingData.name() : __markingData,
        __markingQualifier.name() : __markingQualifier
    })
    _AttributeMap.update({
        __maxSelection.name() : __maxSelection,
        __minSelection.name() : __minSelection
    })
_module_typeBindings.privacyMarks_ = privacyMarks_
Namespace.addCategoryObject('typeBinding', 'privacyMarks', privacyMarks_)


# Complex type {http://www.xmlspif.org/spif}securityClassification with content type ELEMENT_ONLY
class securityClassification_ (pyxb.binding.basis.complexTypeDefinition):
    """
        
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'securityClassification')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 872, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xmlspif.org/spif}requiredCategory uses Python identifier requiredCategory
    __requiredCategory = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'requiredCategory'), 'requiredCategory', '__httpwww_xmlspif_orgspif_securityClassification__httpwww_xmlspif_orgspifrequiredCategory', True, pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 649, 2), )

    
    requiredCategory = property(__requiredCategory.value, __requiredCategory.set, None, '\n        \n      ')

    
    # Element {http://www.xmlspif.org/spif}equivalentClassification uses Python identifier equivalentClassification
    __equivalentClassification = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'equivalentClassification'), 'equivalentClassification', '__httpwww_xmlspif_orgspif_securityClassification__httpwww_xmlspif_orgspifequivalentClassification', True, pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 696, 2), )

    
    equivalentClassification = property(__equivalentClassification.value, __equivalentClassification.set, None, '\n        \n      ')

    
    # Element {http://www.xmlspif.org/spif}markingData uses Python identifier markingData
    __markingData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'markingData'), 'markingData', '__httpwww_xmlspif_orgspif_securityClassification__httpwww_xmlspif_orgspifmarkingData', True, pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 862, 2), )

    
    markingData = property(__markingData.value, __markingData.set, None, '\n        \n      ')

    
    # Element {http://www.xmlspif.org/spif}markingQualifier uses Python identifier markingQualifier
    __markingQualifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'markingQualifier'), 'markingQualifier', '__httpwww_xmlspif_orgspif_securityClassification__httpwww_xmlspif_orgspifmarkingQualifier', True, pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1095, 2), )

    
    markingQualifier = property(__markingQualifier.value, __markingQualifier.set, None, '\n        \n      ')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_xmlspif_orgspif_securityClassification__name', _module_typeBindings.className, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 898, 4)
    __name._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 898, 4)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute color uses Python identifier color
    __color = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'color'), 'color', '__httpwww_xmlspif_orgspif_securityClassification__color', _module_typeBindings.color)
    __color._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 899, 4)
    __color._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 899, 4)
    
    color = property(__color.value, __color.set, None, None)

    
    # Attribute lacv uses Python identifier lacv
    __lacv = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lacv'), 'lacv', '__httpwww_xmlspif_orgspif_securityClassification__lacv', _module_typeBindings.lacvInt, required=True)
    __lacv._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 900, 4)
    __lacv._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 900, 4)
    
    lacv = property(__lacv.value, __lacv.set, None, None)

    
    # Attribute hierarchy uses Python identifier hierarchy
    __hierarchy = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'hierarchy'), 'hierarchy', '__httpwww_xmlspif_orgspif_securityClassification__hierarchy', _module_typeBindings.hierarchy, required=True)
    __hierarchy._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 901, 4)
    __hierarchy._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 901, 4)
    
    hierarchy = property(__hierarchy.value, __hierarchy.set, None, None)

    
    # Attribute obsolete uses Python identifier obsolete
    __obsolete = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'obsolete'), 'obsolete', '__httpwww_xmlspif_orgspif_securityClassification__obsolete', pyxb.binding.datatypes.boolean, unicode_default='false')
    __obsolete._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 902, 4)
    __obsolete._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 902, 4)
    
    obsolete = property(__obsolete.value, __obsolete.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        __requiredCategory.name() : __requiredCategory,
        __equivalentClassification.name() : __equivalentClassification,
        __markingData.name() : __markingData,
        __markingQualifier.name() : __markingQualifier
    })
    _AttributeMap.update({
        __name.name() : __name,
        __color.name() : __color,
        __lacv.name() : __lacv,
        __hierarchy.name() : __hierarchy,
        __obsolete.name() : __obsolete
    })
_module_typeBindings.securityClassification_ = securityClassification_
Namespace.addCategoryObject('typeBinding', 'securityClassification', securityClassification_)


# Complex type {http://www.xmlspif.org/spif}equivalentSecCategoryTag with content type EMPTY
class equivalentSecCategoryTag_ (pyxb.binding.basis.complexTypeDefinition):
    """
        
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'equivalentSecCategoryTag')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 952, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute policyRef uses Python identifier policyRef
    __policyRef = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'policyRef'), 'policyRef', '__httpwww_xmlspif_orgspif_equivalentSecCategoryTag__policyRef', _module_typeBindings.policyName, required=True)
    __policyRef._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 970, 4)
    __policyRef._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 970, 4)
    
    policyRef = property(__policyRef.value, __policyRef.set, None, None)

    
    # Attribute tagSetId uses Python identifier tagSetId
    __tagSetId = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tagSetId'), 'tagSetId', '__httpwww_xmlspif_orgspif_equivalentSecCategoryTag__tagSetId', _module_typeBindings.oid, required=True)
    __tagSetId._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 971, 4)
    __tagSetId._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 971, 4)
    
    tagSetId = property(__tagSetId.value, __tagSetId.set, None, None)

    
    # Attribute tagType uses Python identifier tagType
    __tagType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tagType'), 'tagType', '__httpwww_xmlspif_orgspif_equivalentSecCategoryTag__tagType', _module_typeBindings.tagType, required=True)
    __tagType._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 972, 4)
    __tagType._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 972, 4)
    
    tagType = property(__tagType.value, __tagType.set, None, None)

    
    # Attribute enumType uses Python identifier enumType
    __enumType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'enumType'), 'enumType', '__httpwww_xmlspif_orgspif_equivalentSecCategoryTag__enumType', _module_typeBindings.enumType)
    __enumType._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 973, 4)
    __enumType._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 973, 4)
    
    enumType = property(__enumType.value, __enumType.set, None, None)

    
    # Attribute lacv uses Python identifier lacv
    __lacv = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lacv'), 'lacv', '__httpwww_xmlspif_orgspif_equivalentSecCategoryTag__lacv', _module_typeBindings.lacv, required=True)
    __lacv._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 974, 4)
    __lacv._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 974, 4)
    
    lacv = property(__lacv.value, __lacv.set, None, None)

    
    # Attribute applied uses Python identifier applied
    __applied = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'applied'), 'applied', '__httpwww_xmlspif_orgspif_equivalentSecCategoryTag__applied', _module_typeBindings.applied, required=True)
    __applied._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 975, 4)
    __applied._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 975, 4)
    
    applied = property(__applied.value, __applied.set, None, None)

    
    # Attribute action uses Python identifier action
    __action = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'action'), 'action', '__httpwww_xmlspif_orgspif_equivalentSecCategoryTag__action', _module_typeBindings.equivalencyAction)
    __action._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 977, 4)
    __action._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 977, 4)
    
    action = property(__action.value, __action.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __policyRef.name() : __policyRef,
        __tagSetId.name() : __tagSetId,
        __tagType.name() : __tagType,
        __enumType.name() : __enumType,
        __lacv.name() : __lacv,
        __applied.name() : __applied,
        __action.name() : __action
    })
_module_typeBindings.equivalentSecCategoryTag_ = equivalentSecCategoryTag_
Namespace.addCategoryObject('typeBinding', 'equivalentSecCategoryTag', equivalentSecCategoryTag_)


# Complex type {http://www.xmlspif.org/spif}tagCategory with content type ELEMENT_ONLY
class tagCategory_ (pyxb.binding.basis.complexTypeDefinition):
    """
        
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'tagCategory')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 991, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xmlspif.org/spif}excludedClass uses Python identifier excludedClass
    __excludedClass = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'excludedClass'), 'excludedClass', '__httpwww_xmlspif_orgspif_tagCategory__httpwww_xmlspif_orgspifexcludedClass', True, pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 283, 2), )

    
    excludedClass = property(__excludedClass.value, __excludedClass.set, None, '\n        \n      ')

    
    # Element {http://www.xmlspif.org/spif}excludedCategory uses Python identifier excludedCategory
    __excludedCategory = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'excludedCategory'), 'excludedCategory', '__httpwww_xmlspif_orgspif_tagCategory__httpwww_xmlspif_orgspifexcludedCategory', True, pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 619, 2), )

    
    excludedCategory = property(__excludedCategory.value, __excludedCategory.set, None, '\n        \n      ')

    
    # Element {http://www.xmlspif.org/spif}requiredCategory uses Python identifier requiredCategory
    __requiredCategory = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'requiredCategory'), 'requiredCategory', '__httpwww_xmlspif_orgspif_tagCategory__httpwww_xmlspif_orgspifrequiredCategory', True, pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 649, 2), )

    
    requiredCategory = property(__requiredCategory.value, __requiredCategory.set, None, '\n        \n      ')

    
    # Element {http://www.xmlspif.org/spif}markingData uses Python identifier markingData
    __markingData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'markingData'), 'markingData', '__httpwww_xmlspif_orgspif_tagCategory__httpwww_xmlspif_orgspifmarkingData', True, pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 862, 2), )

    
    markingData = property(__markingData.value, __markingData.set, None, '\n        \n      ')

    
    # Element {http://www.xmlspif.org/spif}equivalentSecCategoryTag uses Python identifier equivalentSecCategoryTag
    __equivalentSecCategoryTag = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'equivalentSecCategoryTag'), 'equivalentSecCategoryTag', '__httpwww_xmlspif_orgspif_tagCategory__httpwww_xmlspif_orgspifequivalentSecCategoryTag', True, pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 981, 2), )

    
    equivalentSecCategoryTag = property(__equivalentSecCategoryTag.value, __equivalentSecCategoryTag.set, None, '\n        \n      ')

    
    # Element {http://www.xmlspif.org/spif}markingQualifier uses Python identifier markingQualifier
    __markingQualifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'markingQualifier'), 'markingQualifier', '__httpwww_xmlspif_orgspif_tagCategory__httpwww_xmlspif_orgspifmarkingQualifier', True, pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1095, 2), )

    
    markingQualifier = property(__markingQualifier.value, __markingQualifier.set, None, '\n        \n      ')

    
    # Attribute notBefore uses Python identifier notBefore
    __notBefore = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'notBefore'), 'notBefore', '__httpwww_xmlspif_orgspif_tagCategory__notBefore', pyxb.binding.datatypes.dateTime)
    __notBefore._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 579, 4)
    __notBefore._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 579, 4)
    
    notBefore = property(__notBefore.value, __notBefore.set, None, None)

    
    # Attribute notAfter uses Python identifier notAfter
    __notAfter = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'notAfter'), 'notAfter', '__httpwww_xmlspif_orgspif_tagCategory__notAfter', pyxb.binding.datatypes.dateTime)
    __notAfter._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 580, 4)
    __notAfter._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 580, 4)
    
    notAfter = property(__notAfter.value, __notAfter.set, None, None)

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_xmlspif_orgspif_tagCategory__name', pyxb.binding.datatypes.string, required=True)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1024, 4)
    __name._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1024, 4)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute lacv uses Python identifier lacv
    __lacv = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'lacv'), 'lacv', '__httpwww_xmlspif_orgspif_tagCategory__lacv', _module_typeBindings.lacv, required=True)
    __lacv._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1025, 4)
    __lacv._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1025, 4)
    
    lacv = property(__lacv.value, __lacv.set, None, None)

    
    # Attribute userInput uses Python identifier userInput
    __userInput = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'userInput'), 'userInput', '__httpwww_xmlspif_orgspif_tagCategory__userInput', _module_typeBindings.userInput)
    __userInput._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1026, 4)
    __userInput._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1026, 4)
    
    userInput = property(__userInput.value, __userInput.set, None, None)

    
    # Attribute requiredClass uses Python identifier requiredClass
    __requiredClass = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'requiredClass'), 'requiredClass', '__httpwww_xmlspif_orgspif_tagCategory__requiredClass', _module_typeBindings.className)
    __requiredClass._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1027, 4)
    __requiredClass._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1027, 4)
    
    requiredClass = property(__requiredClass.value, __requiredClass.set, None, None)

    
    # Attribute obsolete uses Python identifier obsolete
    __obsolete = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'obsolete'), 'obsolete', '__httpwww_xmlspif_orgspif_tagCategory__obsolete', pyxb.binding.datatypes.boolean, unicode_default='false')
    __obsolete._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1028, 4)
    __obsolete._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1028, 4)
    
    obsolete = property(__obsolete.value, __obsolete.set, None, None)

    
    # Attribute dateFormat uses Python identifier dateFormat
    __dateFormat = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'dateFormat'), 'dateFormat', '__httpwww_xmlspif_orgspif_tagCategory__dateFormat', pyxb.binding.datatypes.string)
    __dateFormat._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1030, 4)
    __dateFormat._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1030, 4)
    
    dateFormat = property(__dateFormat.value, __dateFormat.set, None, 'Format as defined in ISO 8601')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        __excludedClass.name() : __excludedClass,
        __excludedCategory.name() : __excludedCategory,
        __requiredCategory.name() : __requiredCategory,
        __markingData.name() : __markingData,
        __equivalentSecCategoryTag.name() : __equivalentSecCategoryTag,
        __markingQualifier.name() : __markingQualifier
    })
    _AttributeMap.update({
        __notBefore.name() : __notBefore,
        __notAfter.name() : __notAfter,
        __name.name() : __name,
        __lacv.name() : __lacv,
        __userInput.name() : __userInput,
        __requiredClass.name() : __requiredClass,
        __obsolete.name() : __obsolete,
        __dateFormat.name() : __dateFormat
    })
_module_typeBindings.tagCategory_ = tagCategory_
Namespace.addCategoryObject('typeBinding', 'tagCategory', tagCategory_)


# Complex type {http://www.xmlspif.org/spif}securityCategoryTag with content type ELEMENT_ONLY
class securityCategoryTag_ (pyxb.binding.basis.complexTypeDefinition):
    """
        
      """
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'securityCategoryTag')
    _XSDLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1105, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.xmlspif.org/spif}tagCategory uses Python identifier tagCategory
    __tagCategory = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'tagCategory'), 'tagCategory', '__httpwww_xmlspif_orgspif_securityCategoryTag__httpwww_xmlspif_orgspiftagCategory', True, pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1039, 2), )

    
    tagCategory = property(__tagCategory.value, __tagCategory.set, None, '\n        \n      ')

    
    # Element {http://www.xmlspif.org/spif}markingQualifier uses Python identifier markingQualifier
    __markingQualifier = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'markingQualifier'), 'markingQualifier', '__httpwww_xmlspif_orgspif_securityCategoryTag__httpwww_xmlspif_orgspifmarkingQualifier', True, pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1095, 2), )

    
    markingQualifier = property(__markingQualifier.value, __markingQualifier.set, None, '\n        \n      ')

    
    # Attribute name uses Python identifier name
    __name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'name'), 'name', '__httpwww_xmlspif_orgspif_securityCategoryTag__name', pyxb.binding.datatypes.string)
    __name._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1129, 4)
    __name._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1129, 4)
    
    name = property(__name.value, __name.set, None, None)

    
    # Attribute tagType uses Python identifier tagType
    __tagType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tagType'), 'tagType', '__httpwww_xmlspif_orgspif_securityCategoryTag__tagType', _module_typeBindings.tagType, required=True)
    __tagType._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1130, 4)
    __tagType._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1130, 4)
    
    tagType = property(__tagType.value, __tagType.set, None, None)

    
    # Attribute enumType uses Python identifier enumType
    __enumType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'enumType'), 'enumType', '__httpwww_xmlspif_orgspif_securityCategoryTag__enumType', _module_typeBindings.enumType)
    __enumType._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1131, 4)
    __enumType._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1131, 4)
    
    enumType = property(__enumType.value, __enumType.set, None, None)

    
    # Attribute tag7Encoding uses Python identifier tag7Encoding
    __tag7Encoding = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'tag7Encoding'), 'tag7Encoding', '__httpwww_xmlspif_orgspif_securityCategoryTag__tag7Encoding', _module_typeBindings.tag7Encoding)
    __tag7Encoding._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1132, 4)
    __tag7Encoding._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1132, 4)
    
    tag7Encoding = property(__tag7Encoding.value, __tag7Encoding.set, None, None)

    
    # Attribute singleSelection uses Python identifier singleSelection
    __singleSelection = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'singleSelection'), 'singleSelection', '__httpwww_xmlspif_orgspif_securityCategoryTag__singleSelection', pyxb.binding.datatypes.boolean, unicode_default='false')
    __singleSelection._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1133, 4)
    __singleSelection._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1133, 4)
    
    singleSelection = property(__singleSelection.value, __singleSelection.set, None, None)

    
    # Attribute maxSelection uses Python identifier maxSelection
    __maxSelection = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'maxSelection'), 'maxSelection', '__httpwww_xmlspif_orgspif_securityCategoryTag__maxSelection', _module_typeBindings.selection, unicode_default='unbounded')
    __maxSelection._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1135, 4)
    __maxSelection._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1135, 4)
    
    maxSelection = property(__maxSelection.value, __maxSelection.set, None, None)

    
    # Attribute minSelection uses Python identifier minSelection
    __minSelection = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, 'minSelection'), 'minSelection', '__httpwww_xmlspif_orgspif_securityCategoryTag__minSelection', _module_typeBindings.selection, unicode_default='unbounded')
    __minSelection._DeclarationLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1136, 4)
    __minSelection._UseLocation = pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1136, 4)
    
    minSelection = property(__minSelection.value, __minSelection.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        __tagCategory.name() : __tagCategory,
        __markingQualifier.name() : __markingQualifier
    })
    _AttributeMap.update({
        __name.name() : __name,
        __tagType.name() : __tagType,
        __enumType.name() : __enumType,
        __tag7Encoding.name() : __tag7Encoding,
        __singleSelection.name() : __singleSelection,
        __maxSelection.name() : __maxSelection,
        __minSelection.name() : __minSelection
    })
_module_typeBindings.securityCategoryTag_ = securityCategoryTag_
Namespace.addCategoryObject('typeBinding', 'securityCategoryTag', securityCategoryTag_)


excludedClass = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'excludedClass'), className, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 283, 2))
Namespace.addCategoryObject('elementBinding', excludedClass.name().localName(), excludedClass)

code = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'code'), markingCode, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 403, 2))
Namespace.addCategoryObject('elementBinding', code.name().localName(), code)

updateInfo = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'updateInfo'), updateInfo_, location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 668, 2))
Namespace.addCategoryObject('elementBinding', updateInfo.name().localName(), updateInfo)

equivalentPolicies = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'equivalentPolicies'), equivalentPolicies_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 759, 2))
Namespace.addCategoryObject('elementBinding', equivalentPolicies.name().localName(), equivalentPolicies)

privacyMark = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'privacyMark'), privacyMark_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 794, 2))
Namespace.addCategoryObject('elementBinding', privacyMark.name().localName(), privacyMark)

securityClassifications = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'securityClassifications'), securityClassifications_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 942, 2))
Namespace.addCategoryObject('elementBinding', securityClassifications.name().localName(), securityClassifications)

securityCategoryTagSets = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'securityCategoryTagSets'), securityCategoryTagSets_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1234, 2))
Namespace.addCategoryObject('elementBinding', securityCategoryTagSets.name().localName(), securityCategoryTagSets)

extensions = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'extensions'), extensions_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1298, 2))
Namespace.addCategoryObject('elementBinding', extensions.name().localName(), extensions)

requiredCategory = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'requiredCategory'), optionalCategoryGroup, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 649, 2))
Namespace.addCategoryObject('elementBinding', requiredCategory.name().localName(), requiredCategory)

equivalentClassification = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'equivalentClassification'), equivalentClassification_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 696, 2))
Namespace.addCategoryObject('elementBinding', equivalentClassification.name().localName(), equivalentClassification)

equivalentPolicy = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'equivalentPolicy'), equivalentPolicy_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 733, 2))
Namespace.addCategoryObject('elementBinding', equivalentPolicy.name().localName(), equivalentPolicy)

markingData = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'markingData'), markingData_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 862, 2))
Namespace.addCategoryObject('elementBinding', markingData.name().localName(), markingData)

qualifier = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'qualifier'), qualifier_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1066, 2))
Namespace.addCategoryObject('elementBinding', qualifier.name().localName(), qualifier)

markingQualifier = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'markingQualifier'), markingQualifier_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1095, 2))
Namespace.addCategoryObject('elementBinding', markingQualifier.name().localName(), markingQualifier)

securityCategoryTagSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'securityCategoryTagSet'), securityCategoryTagSet_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1173, 2))
Namespace.addCategoryObject('elementBinding', securityCategoryTagSet.name().localName(), securityCategoryTagSet)

equivalentSecurityCategoryTagSet = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'equivalentSecurityCategoryTagSet'), equivalentSecurityCategoryTagSet_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1207, 2))
Namespace.addCategoryObject('elementBinding', equivalentSecurityCategoryTagSet.name().localName(), equivalentSecurityCategoryTagSet)

defaultSecurityPolicyId = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'defaultSecurityPolicyId'), objectIdData, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1267, 2))
Namespace.addCategoryObject('elementBinding', defaultSecurityPolicyId.name().localName(), defaultSecurityPolicyId)

securityPolicyId = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'securityPolicyId'), objectIdData, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1276, 2))
Namespace.addCategoryObject('elementBinding', securityPolicyId.name().localName(), securityPolicyId)

SPIF = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'SPIF'), CTD_ANON, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1308, 2))
Namespace.addCategoryObject('elementBinding', SPIF.name().localName(), SPIF)

categoryGroup = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'categoryGroup'), optionalCategoryData, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 610, 2))
Namespace.addCategoryObject('elementBinding', categoryGroup.name().localName(), categoryGroup)

excludedCategory = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'excludedCategory'), optionalCategoryData, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 619, 2))
Namespace.addCategoryObject('elementBinding', excludedCategory.name().localName(), excludedCategory)

privacyMarks = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'privacyMarks'), privacyMarks_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 832, 2))
Namespace.addCategoryObject('elementBinding', privacyMarks.name().localName(), privacyMarks)

securityClassification = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'securityClassification'), securityClassification_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 905, 2))
Namespace.addCategoryObject('elementBinding', securityClassification.name().localName(), securityClassification)

equivalentSecCategoryTag = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'equivalentSecCategoryTag'), equivalentSecCategoryTag_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 981, 2))
Namespace.addCategoryObject('elementBinding', equivalentSecCategoryTag.name().localName(), equivalentSecCategoryTag)

tagCategory = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tagCategory'), tagCategory_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1039, 2))
Namespace.addCategoryObject('elementBinding', tagCategory.name().localName(), tagCategory)

securityCategoryTag = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'securityCategoryTag'), securityCategoryTag_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1140, 2))
Namespace.addCategoryObject('elementBinding', securityCategoryTag.name().localName(), securityCategoryTag)



equivalentPolicies_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'equivalentPolicy'), equivalentPolicy_, scope=equivalentPolicies_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 733, 2)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(equivalentPolicies_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'equivalentPolicy')), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 756, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
equivalentPolicies_._Automaton = _BuildAutomaton()




privacyMark_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'markingData'), markingData_, scope=privacyMark_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 862, 2)))

privacyMark_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'markingQualifier'), markingQualifier_, scope=privacyMark_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1095, 2)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 786, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 787, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(privacyMark_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'markingData')), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 786, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(privacyMark_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'markingQualifier')), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 787, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
privacyMark_._Automaton = _BuildAutomaton_()




securityClassifications_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'markingData'), markingData_, scope=securityClassifications_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 862, 2)))

securityClassifications_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'securityClassification'), securityClassification_, scope=securityClassifications_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 905, 2)))

securityClassifications_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'markingQualifier'), markingQualifier_, scope=securityClassifications_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1095, 2)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 933, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 934, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(securityClassifications_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'securityClassification')), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 931, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(securityClassifications_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'markingData')), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 933, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(securityClassifications_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'markingQualifier')), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 934, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
securityClassifications_._Automaton = _BuildAutomaton_2()




securityCategoryTagSets_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'securityCategoryTagSet'), securityCategoryTagSet_, scope=securityCategoryTagSets_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1173, 2)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(securityCategoryTagSets_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'securityCategoryTagSet')), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1231, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
securityCategoryTagSets_._Automaton = _BuildAutomaton_3()




def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1295, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1295, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
extensions_._Automaton = _BuildAutomaton_4()




optionalCategoryGroup._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'categoryGroup'), optionalCategoryData, scope=optionalCategoryGroup, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 610, 2)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(optionalCategoryGroup._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'categoryGroup')), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 644, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
optionalCategoryGroup._Automaton = _BuildAutomaton_5()




equivalentClassification_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'requiredCategory'), optionalCategoryGroup, scope=equivalentClassification_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 649, 2)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 688, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(equivalentClassification_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'requiredCategory')), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 688, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
equivalentClassification_._Automaton = _BuildAutomaton_6()




equivalentPolicy_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'requiredCategory'), optionalCategoryGroup, scope=equivalentPolicy_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 649, 2)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 724, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(equivalentPolicy_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'requiredCategory')), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 724, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
equivalentPolicy_._Automaton = _BuildAutomaton_7()




markingData_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'code'), markingCode, scope=markingData_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 403, 2)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(markingData_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'code')), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 857, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
markingData_._Automaton = _BuildAutomaton_8()




markingQualifier_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'qualifier'), qualifier_, scope=markingQualifier_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1066, 2)))

def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(markingQualifier_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'qualifier')), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1090, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
markingQualifier_._Automaton = _BuildAutomaton_9()




securityCategoryTagSet_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'securityCategoryTag'), securityCategoryTag_, scope=securityCategoryTagSet_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1140, 2)))

securityCategoryTagSet_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'equivalentSecurityCategoryTagSet'), equivalentSecurityCategoryTagSet_, scope=securityCategoryTagSet_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1207, 2)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1166, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(securityCategoryTagSet_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'securityCategoryTag')), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1164, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(securityCategoryTagSet_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'equivalentSecurityCategoryTagSet')), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1166, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
securityCategoryTagSet_._Automaton = _BuildAutomaton_10()




equivalentSecurityCategoryTagSet_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'requiredCategory'), optionalCategoryGroup, scope=equivalentSecurityCategoryTagSet_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 649, 2)))

def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1200, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(equivalentSecurityCategoryTagSet_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'requiredCategory')), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1200, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
equivalentSecurityCategoryTagSet_._Automaton = _BuildAutomaton_11()




objectIdData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'markingData'), markingData_, scope=objectIdData, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 862, 2)))

objectIdData._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'markingQualifier'), markingQualifier_, scope=objectIdData, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1095, 2)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1259, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1260, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(objectIdData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'markingData')), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1259, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(objectIdData._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'markingQualifier')), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1260, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
objectIdData._Automaton = _BuildAutomaton_12()




CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'updateInfo'), updateInfo_, scope=CTD_ANON, location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 668, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'equivalentPolicies'), equivalentPolicies_, scope=CTD_ANON, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 759, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'privacyMarks'), privacyMarks_, scope=CTD_ANON, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 832, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'markingData'), markingData_, scope=CTD_ANON, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 862, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'securityClassifications'), securityClassifications_, scope=CTD_ANON, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 942, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'markingQualifier'), markingQualifier_, scope=CTD_ANON, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1095, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'securityCategoryTagSets'), securityCategoryTagSets_, scope=CTD_ANON, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1234, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'defaultSecurityPolicyId'), objectIdData, scope=CTD_ANON, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1267, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'securityPolicyId'), objectIdData, scope=CTD_ANON, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1276, 2)))

CTD_ANON._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'extensions'), extensions_, scope=CTD_ANON, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1298, 2)))

def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1354, 8))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1356, 8))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1358, 8))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1359, 8))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1360, 8))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1362, 8))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1363, 8))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1365, 8))
    counters.add(cc_7)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'defaultSecurityPolicyId')), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1354, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'securityPolicyId')), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1355, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'updateInfo')), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1356, 8))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'securityClassifications')), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1357, 8))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'securityCategoryTagSets')), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1358, 8))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'privacyMarks')), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1359, 8))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'equivalentPolicies')), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1360, 8))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'markingData')), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1362, 8))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'markingQualifier')), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1363, 8))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(CTD_ANON._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'extensions')), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1365, 8))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
         ]))
    transitions.append(fac.Transition(st_5, [
         ]))
    transitions.append(fac.Transition(st_6, [
         ]))
    transitions.append(fac.Transition(st_7, [
         ]))
    transitions.append(fac.Transition(st_8, [
         ]))
    transitions.append(fac.Transition(st_9, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, True) ]))
    st_9._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
CTD_ANON._Automaton = _BuildAutomaton_13()




privacyMarks_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'privacyMark'), privacyMark_, scope=privacyMarks_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 794, 2)))

privacyMarks_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'markingData'), markingData_, scope=privacyMarks_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 862, 2)))

privacyMarks_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'markingQualifier'), markingQualifier_, scope=privacyMarks_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1095, 2)))

def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 823, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 824, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(privacyMarks_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'privacyMark')), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 821, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(privacyMarks_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'markingData')), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 823, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(privacyMarks_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'markingQualifier')), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 824, 6))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
privacyMarks_._Automaton = _BuildAutomaton_14()




securityClassification_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'requiredCategory'), optionalCategoryGroup, scope=securityClassification_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 649, 2)))

securityClassification_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'equivalentClassification'), equivalentClassification_, scope=securityClassification_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 696, 2)))

securityClassification_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'markingData'), markingData_, scope=securityClassification_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 862, 2)))

securityClassification_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'markingQualifier'), markingQualifier_, scope=securityClassification_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1095, 2)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 893, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 894, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 895, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 896, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(securityClassification_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'equivalentClassification')), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 893, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(securityClassification_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'markingData')), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 894, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(securityClassification_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'markingQualifier')), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 895, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(securityClassification_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'requiredCategory')), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 896, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
securityClassification_._Automaton = _BuildAutomaton_15()




tagCategory_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'excludedClass'), className, scope=tagCategory_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 283, 2)))

tagCategory_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'excludedCategory'), optionalCategoryData, scope=tagCategory_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 619, 2)))

tagCategory_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'requiredCategory'), optionalCategoryGroup, scope=tagCategory_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 649, 2)))

tagCategory_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'markingData'), markingData_, scope=tagCategory_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 862, 2)))

tagCategory_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'equivalentSecCategoryTag'), equivalentSecCategoryTag_, scope=tagCategory_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 981, 2)))

tagCategory_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'markingQualifier'), markingQualifier_, scope=tagCategory_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1095, 2)))

def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1015, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1016, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1018, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1020, 6))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1021, 6))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1022, 6))
    counters.add(cc_5)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(tagCategory_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'equivalentSecCategoryTag')), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1015, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(tagCategory_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'markingData')), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1016, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(tagCategory_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'markingQualifier')), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1018, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(tagCategory_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'excludedClass')), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1020, 6))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(tagCategory_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'requiredCategory')), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1021, 6))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(tagCategory_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'excludedCategory')), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1022, 6))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
tagCategory_._Automaton = _BuildAutomaton_16()




securityCategoryTag_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'tagCategory'), tagCategory_, scope=securityCategoryTag_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1039, 2)))

securityCategoryTag_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'markingQualifier'), markingQualifier_, scope=securityCategoryTag_, documentation='\n        \n      ', location=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1095, 2)))

def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1126, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1127, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(securityCategoryTag_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'tagCategory')), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1126, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(securityCategoryTag_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'markingQualifier')), pyxb.utils.utility.Location('http://www.xmlspif.org/schema/xmlspif.xsd', 1127, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
securityCategoryTag_._Automaton = _BuildAutomaton_17()

