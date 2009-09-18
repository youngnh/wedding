
if(typeof($)!==typeof(void(0)))
{$(document).ready(function()
{return true;});}
$.TheKnot.pwp.MemberPage=function(){};$.extend($.TheKnot.pwp.MemberPage,{SetPageMainImageDimensions:function()
{var jqoImgDiv=$('.contentImg');if(jqoImgDiv.length>0)
{var img=jqoImgDiv.find('img');if(img.length==0)
{debugger;}
with(img)
{var jqoImgDivWidth=jqoImgDiv.css('width').replace('px','');if(jqoImgDivWidth!==typeof(void(0))&&jqoImgDivWidth!=''&&!isNaN(jqoImgDivWidth))
{if(img[0].width>jqoImgDivWidth)
{css('width',jqoImgDivWidth);}}
else
{if(img[0].width>300)
{img.css('width',300);}}
var jqoImgDivHeight=jqoImgDiv.css('height').replace('px','');if(jqoImgDivHeight!==typeof(void(0))&&jqoImgDivHeight!=''&&!isNaN(jqoImgDivHeight))
{if(img[0].height>jqoImgDivHeight)
{css('height',jqoImgDivHeight);}}
else
{if(img[0].height>250)
{img.css('height',250);}}
if(img.width()==0||img.height()==0)
{debugger;}}}}});$.TheKnot.pwp.MemberPage.PhotoAlbum=function(){};$.extend($.TheKnot.pwp.MemberPage.PhotoAlbum,{ShowImage:function(obj,MemberId,ImageId)
{$('div[id$=Modal]').hide();this._GetImageInfo(MemberId,ImageId);},_GetImageInfo:function(MemberId,ImageId)
{$.ajax({type:'GET',url:'/pwp/pwp2/PwpWebServices/PhotoAlbumViewer.ashx',data:'mid='+MemberId+'&iid='+ImageId,dataType:'json',cache:false,success:function(data,textStatus)
{var pop=$('div#popupModal');var popImg=pop.find('img.main_image');var popImgDesc=pop.find('p#pImgDesc');var popNext=pop.find('a.next');var popPrev=pop.find('a.prev');var popCounter=pop.find('div.counter');popImg[0].src=data.imagePath;popImgDesc.text(unescape(data.description));popNext.unbind('click');popNext.click
(function(e)
{e.preventDefault();$.TheKnot.pwp.MemberPage.PhotoAlbum.ShowImage(null,MemberId,data.nextImageId);});popPrev.unbind('click');popPrev.click
(function(e)
{e.preventDefault();$.TheKnot.pwp.MemberPage.PhotoAlbum.ShowImage(null,MemberId,data.prevImageId);});popCounter.text($.TheKnot.formatStr('Photo {0} of {1}',((data.imageIndex*1)+1),data.totalImages));if($.browser.msie)
{pop.find('table:first').css('top',document.documentElement.scrollTop-10);}
else
{pop.find('table:first').css('top',window.scrollY-10);}
pop.find('table:first').css('left','50%');pop.show();},error:function(XMLHttpRequest,textStatus,errorThrown)
{}});}});