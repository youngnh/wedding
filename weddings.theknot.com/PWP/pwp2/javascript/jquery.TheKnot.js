
$.TheKnot=function(){};$.TheKnot.pwp=function(){};$.TheKnot.pwp.admin=function(){};$.TheKnot.pwp.admin.PageEditor=function(){};$.TheKnot.pwp.admin.PageEditor.LiveEditorInteraction=function(){};$.extend($.TheKnot,{formatStr:function(FormatString,ParmString0,ParmStringN)
{if(this.isUndef(FormatString)||this.isUndef(ParmString0)||FormatString.indexOf('{0}')==-1)
{return;}
var retStr=FormatString;for(var i=1;i<arguments.length;++i)
{var s='{'+(i-1)+'}';while(retStr.indexOf(s)!=-1)
{retStr=retStr.replace(s,arguments[i]);}}
return retStr;},isUndef:function(obj)
{return(typeof(obj)===typeof(void(0)));},isNullOrUndef:function(obj)
{return(this.isUndef(obj)||obj==null)?true:false;},CreateQueryStringFrom2Objects:function(defaultObj,overrideObj)
{var retStr="";for(var o in defaultObj)
{if(typeof(overrideObj[o])!==typeof(void(0)))
{retStr=retStr+$.TheKnot.formatStr("{0}={1}&",o,overrideObj[o]);}
else
{retStr=retStr+$.TheKnot.formatStr("{0}={1}&",o,defaultObj[o]);}}
retStr=retStr.substring(0,retStr.length-1);return retStr;},isValidEmailAddress:function(strTest)
{return/\w+([-+.'']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*/.test(strTest);},CreateQueryStringFromObject:function(obj)
{var retStr="";for(var o in obj)
{retStr=retStr+$.TheKnot.formatStr("{0}={1}&",o,obj[o]);}
retStr=retStr.substring(0,retStr.length-1);return retStr;},DOMCloneWithDataElements:function(obj2clone,objDataKeys2cloneAlso,boolCloneEvents)
{if(this.isNullOrUndef(obj2clone)||this.isNullOrUndef(objDataKeys2cloneAlso))
{return obj2clone;}
boolCloneEvents=(this.isNullOrUndef(boolCloneEvents))?true:boolCloneEvents;var Clone=obj2clone.clone(boolCloneEvents);if(!this.isNullOrUndef(obj2clone.data(objDataKeys2cloneAlso)))
{Clone.data(objDataKeys2cloneAlso,obj2clone.data(objDataKeys2cloneAlso));}
obj2clone.find('*').each(function()
{if(!$.TheKnot.isNullOrUndef($(this).data(objDataKeys2cloneAlso)))
{Clone.find(this.tagName+"#"+this.id).data(objDataKeys2cloneAlso,$(this).data(objDataKeys2cloneAlso));}});return Clone;}});$.TheKnot.InputField=function(strSelector,strFriendlyName,rexValidator,boolRequired,ErrorMessage)
{this.selector=strSelector;this.friendlyName=strFriendlyName;this.validator=rexValidator;this.required=boolRequired;this.error=(!$.TheKnot.isUndef(ErrorMessage))?ErrorMessage:'';this.isvalid=false;this.jqueryField=function()
{return $(this.selector);};this.htmlField=function()
{return $(this.selector)[0];};this.value=function()
{return $(this.selector).val();};this.validate=function()
{with($(this.selector))
{if($.trim(val()).length==0||RegExp(this.validator).test(val()))
{if(this.error.length==0)
{this.error=$.TheKnot.formatStr("The '{0}' field {1} have a value.",this.friendlyName,((this.required)?"must":"does not"));}
return false;}
this.isvalid=true;return true;}};return this;};