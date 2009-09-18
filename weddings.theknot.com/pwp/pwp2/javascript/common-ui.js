
KeyPressEvent=function(event)
{if(typeof(document.all)===typeof(void(0)))
{if(event.which!=13)
{return true;}
else
{if(typeof(event.target)!==typeof(void(0))&&(event.target.tagName=='TEXTAREA'||event.target.tagName=='A'))
{return true;}
event.returnValue=false;event.preventDefault();}}
else
{if(window.event.keyCode==13&&(window.event.srcElement.tagName!='TEXTAREA'&&window.event.srcElement.tagName!='A'))
{return false;}}
return true;}
if(typeof(document.all)===typeof(void(0)))
{document.addEventListener("keypress",KeyPressEvent,true);}
else
{document.onkeypress=KeyPressEvent;}
function open_popup_preview(id)
{var url="http://weddings.theknot.com/pwp/samples/pwp_sample"+id+".html";var properties="toolbar=0,location=0,directories=0,status=0,menubar=0,copyhistory=0,scrollbars=1,resizeable=1,width=540,height=580";child=window.open(url,"popup",properties);}
function redirt(thisarea)
{thisurl=''+thisarea;window.location=thisurl;}
function helppop(URL)
{myWindow=window.open(URL,"","toolbar=YES,location=0,directories=0,status=0,menubar=0,scrollbars=YES,copyhistory=0,width=450,height=320, left=100, top=100");}
function imageopen(thisfile)
{window.open(thisfile,"popup","toolbar=no,menubar=no,scrollbars=no,resizable=yes,width=500,height=600");}