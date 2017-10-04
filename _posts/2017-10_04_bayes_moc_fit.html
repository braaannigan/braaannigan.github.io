---
layout: post
title:  "Bayesian inference of MOC variability"
date:   2017-10-04 10:35:24
categories: communication
---


<!DOCTYPE html>
<html>
<head><meta charset="utf-8" />
<title>bayes_moc_gaussian</title><script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>

<style type="text/css">
    /*!
*
* Twitter Bootstrap
*
*/
/*!
 * Bootstrap v3.3.7 (http://getbootstrap.com)
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 */
/*! normalize.css v3.0.3 | MIT License | github.com/necolas/normalize.css */
html {
  font-family: sans-serif;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
}
body {
  margin: 0;
}
article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
main,
menu,
nav,
section,
summary {
  display: block;
}
audio,
canvas,
progress,
video {
  display: inline-block;
  vertical-align: baseline;
}
audio:not([controls]) {
  display: none;
  height: 0;
}
[hidden],
template {
  display: none;
}
a {
  background-color: transparent;
}
a:active,
a:hover {
  outline: 0;
}
abbr[title] {
  border-bottom: 1px dotted;
}
b,
strong {
  font-weight: bold;
}
dfn {
  font-style: italic;
}
h1 {
  font-size: 2em;
  margin: 0.67em 0;
}
mark {
  background: #ff0;
  color: #000;
}
small {
  font-size: 80%;
}
sub,
sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}
sup {
  top: -0.5em;
}
sub {
  bottom: -0.25em;
}
img {
  border: 0;
}
svg:not(:root) {
  overflow: hidden;
}
figure {
  margin: 1em 40px;
}
hr {
  box-sizing: content-box;
  height: 0;
}
pre {
  overflow: auto;
}
code,
kbd,
pre,
samp {
  font-family: monospace, monospace;
  font-size: 1em;
}
button,
input,
optgroup,
select,
textarea {
  color: inherit;
  font: inherit;
  margin: 0;
}
button {
  overflow: visible;
}
button,
select {
  text-transform: none;
}
button,
html input[type="button"],
input[type="reset"],
input[type="submit"] {
  -webkit-appearance: button;
  cursor: pointer;
}
button[disabled],
html input[disabled] {
  cursor: default;
}
button::-moz-focus-inner,
input::-moz-focus-inner {
  border: 0;
  padding: 0;
}
input {
  line-height: normal;
}
input[type="checkbox"],
input[type="radio"] {
  box-sizing: border-box;
  padding: 0;
}
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: textfield;
  box-sizing: content-box;
}
input[type="search"]::-webkit-search-cancel-button,
input[type="search"]::-webkit-search-decoration {
  -webkit-appearance: none;
}
fieldset {
  border: 1px solid #c0c0c0;
  margin: 0 2px;
  padding: 0.35em 0.625em 0.75em;
}
legend {
  border: 0;
  padding: 0;
}
textarea {
  overflow: auto;
}
optgroup {
  font-weight: bold;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}
td,
th {
  padding: 0;
}
/*! Source: https://github.com/h5bp/html5-boilerplate/blob/master/src/css/main.css */
@media print {
  *,
  *:before,
  *:after {
    background: transparent !important;
    color: #000 !important;
    box-shadow: none !important;
    text-shadow: none !important;
  }
  a,
  a:visited {
    text-decoration: underline;
  }
  a[href]:after {
    content: " (" attr(href) ")";
  }
  abbr[title]:after {
    content: " (" attr(title) ")";
  }
  a[href^="#"]:after,
  a[href^="javascript:"]:after {
    content: "";
  }
  pre,
  blockquote {
    border: 1px solid #999;
    page-break-inside: avoid;
  }
  thead {
    display: table-header-group;
  }
  tr,
  img {
    page-break-inside: avoid;
  }
  img {
    max-width: 100% !important;
  }
  p,
  h2,
  h3 {
    orphans: 3;
    widows: 3;
  }
  h2,
  h3 {
    page-break-after: avoid;
  }
  .navbar {
    display: none;
  }
  .btn > .caret,
  .dropup > .btn > .caret {
    border-top-color: #000 !important;
  }
  .label {
    border: 1px solid #000;
  }
  .table {
    border-collapse: collapse !important;
  }
  .table td,
  .table th {
    background-color: #fff !important;
  }
  .table-bordered th,
  .table-bordered td {
    border: 1px solid #ddd !important;
  }
}
@font-face {
  font-family: 'Glyphicons Halflings';
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot');
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot?#iefix') format('embedded-opentype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff2') format('woff2'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff') format('woff'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.ttf') format('truetype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.svg#glyphicons_halflingsregular') format('svg');
}
.glyphicon {
  position: relative;
  top: 1px;
  display: inline-block;
  font-family: 'Glyphicons Halflings';
  font-style: normal;
  font-weight: normal;
  line-height: 1;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.glyphicon-asterisk:before {
  content: "\002a";
}
.glyphicon-plus:before {
  content: "\002b";
}
.glyphicon-euro:before,
.glyphicon-eur:before {
  content: "\20ac";
}
.glyphicon-minus:before {
  content: "\2212";
}
.glyphicon-cloud:before {
  content: "\2601";
}
.glyphicon-envelope:before {
  content: "\2709";
}
.glyphicon-pencil:before {
  content: "\270f";
}
.glyphicon-glass:before {
  content: "\e001";
}
.glyphicon-music:before {
  content: "\e002";
}
.glyphicon-search:before {
  content: "\e003";
}
.glyphicon-heart:before {
  content: "\e005";
}
.glyphicon-star:before {
  content: "\e006";
}
.glyphicon-star-empty:before {
  content: "\e007";
}
.glyphicon-user:before {
  content: "\e008";
}
.glyphicon-film:before {
  content: "\e009";
}
.glyphicon-th-large:before {
  content: "\e010";
}
.glyphicon-th:before {
  content: "\e011";
}
.glyphicon-th-list:before {
  content: "\e012";
}
.glyphicon-ok:before {
  content: "\e013";
}
.glyphicon-remove:before {
  content: "\e014";
}
.glyphicon-zoom-in:before {
  content: "\e015";
}
.glyphicon-zoom-out:before {
  content: "\e016";
}
.glyphicon-off:before {
  content: "\e017";
}
.glyphicon-signal:before {
  content: "\e018";
}
.glyphicon-cog:before {
  content: "\e019";
}
.glyphicon-trash:before {
  content: "\e020";
}
.glyphicon-home:before {
  content: "\e021";
}
.glyphicon-file:before {
  content: "\e022";
}
.glyphicon-time:before {
  content: "\e023";
}
.glyphicon-road:before {
  content: "\e024";
}
.glyphicon-download-alt:before {
  content: "\e025";
}
.glyphicon-download:before {
  content: "\e026";
}
.glyphicon-upload:before {
  content: "\e027";
}
.glyphicon-inbox:before {
  content: "\e028";
}
.glyphicon-play-circle:before {
  content: "\e029";
}
.glyphicon-repeat:before {
  content: "\e030";
}
.glyphicon-refresh:before {
  content: "\e031";
}
.glyphicon-list-alt:before {
  content: "\e032";
}
.glyphicon-lock:before {
  content: "\e033";
}
.glyphicon-flag:before {
  content: "\e034";
}
.glyphicon-headphones:before {
  content: "\e035";
}
.glyphicon-volume-off:before {
  content: "\e036";
}
.glyphicon-volume-down:before {
  content: "\e037";
}
.glyphicon-volume-up:before {
  content: "\e038";
}
.glyphicon-qrcode:before {
  content: "\e039";
}
.glyphicon-barcode:before {
  content: "\e040";
}
.glyphicon-tag:before {
  content: "\e041";
}
.glyphicon-tags:before {
  content: "\e042";
}
.glyphicon-book:before {
  content: "\e043";
}
.glyphicon-bookmark:before {
  content: "\e044";
}
.glyphicon-print:before {
  content: "\e045";
}
.glyphicon-camera:before {
  content: "\e046";
}
.glyphicon-font:before {
  content: "\e047";
}
.glyphicon-bold:before {
  content: "\e048";
}
.glyphicon-italic:before {
  content: "\e049";
}
.glyphicon-text-height:before {
  content: "\e050";
}
.glyphicon-text-width:before {
  content: "\e051";
}
.glyphicon-align-left:before {
  content: "\e052";
}
.glyphicon-align-center:before {
  content: "\e053";
}
.glyphicon-align-right:before {
  content: "\e054";
}
.glyphicon-align-justify:before {
  content: "\e055";
}
.glyphicon-list:before {
  content: "\e056";
}
.glyphicon-indent-left:before {
  content: "\e057";
}
.glyphicon-indent-right:before {
  content: "\e058";
}
.glyphicon-facetime-video:before {
  content: "\e059";
}
.glyphicon-picture:before {
  content: "\e060";
}
.glyphicon-map-marker:before {
  content: "\e062";
}
.glyphicon-adjust:before {
  content: "\e063";
}
.glyphicon-tint:before {
  content: "\e064";
}
.glyphicon-edit:before {
  content: "\e065";
}
.glyphicon-share:before {
  content: "\e066";
}
.glyphicon-check:before {
  content: "\e067";
}
.glyphicon-move:before {
  content: "\e068";
}
.glyphicon-step-backward:before {
  content: "\e069";
}
.glyphicon-fast-backward:before {
  content: "\e070";
}
.glyphicon-backward:before {
  content: "\e071";
}
.glyphicon-play:before {
  content: "\e072";
}
.glyphicon-pause:before {
  content: "\e073";
}
.glyphicon-stop:before {
  content: "\e074";
}
.glyphicon-forward:before {
  content: "\e075";
}
.glyphicon-fast-forward:before {
  content: "\e076";
}
.glyphicon-step-forward:before {
  content: "\e077";
}
.glyphicon-eject:before {
  content: "\e078";
}
.glyphicon-chevron-left:before {
  content: "\e079";
}
.glyphicon-chevron-right:before {
  content: "\e080";
}
.glyphicon-plus-sign:before {
  content: "\e081";
}
.glyphicon-minus-sign:before {
  content: "\e082";
}
.glyphicon-remove-sign:before {
  content: "\e083";
}
.glyphicon-ok-sign:before {
  content: "\e084";
}
.glyphicon-question-sign:before {
  content: "\e085";
}
.glyphicon-info-sign:before {
  content: "\e086";
}
.glyphicon-screenshot:before {
  content: "\e087";
}
.glyphicon-remove-circle:before {
  content: "\e088";
}
.glyphicon-ok-circle:before {
  content: "\e089";
}
.glyphicon-ban-circle:before {
  content: "\e090";
}
.glyphicon-arrow-left:before {
  content: "\e091";
}
.glyphicon-arrow-right:before {
  content: "\e092";
}
.glyphicon-arrow-up:before {
  content: "\e093";
}
.glyphicon-arrow-down:before {
  content: "\e094";
}
.glyphicon-share-alt:before {
  content: "\e095";
}
.glyphicon-resize-full:before {
  content: "\e096";
}
.glyphicon-resize-small:before {
  content: "\e097";
}
.glyphicon-exclamation-sign:before {
  content: "\e101";
}
.glyphicon-gift:before {
  content: "\e102";
}
.glyphicon-leaf:before {
  content: "\e103";
}
.glyphicon-fire:before {
  content: "\e104";
}
.glyphicon-eye-open:before {
  content: "\e105";
}
.glyphicon-eye-close:before {
  content: "\e106";
}
.glyphicon-warning-sign:before {
  content: "\e107";
}
.glyphicon-plane:before {
  content: "\e108";
}
.glyphicon-calendar:before {
  content: "\e109";
}
.glyphicon-random:before {
  content: "\e110";
}
.glyphicon-comment:before {
  content: "\e111";
}
.glyphicon-magnet:before {
  content: "\e112";
}
.glyphicon-chevron-up:before {
  content: "\e113";
}
.glyphicon-chevron-down:before {
  content: "\e114";
}
.glyphicon-retweet:before {
  content: "\e115";
}
.glyphicon-shopping-cart:before {
  content: "\e116";
}
.glyphicon-folder-close:before {
  content: "\e117";
}
.glyphicon-folder-open:before {
  content: "\e118";
}
.glyphicon-resize-vertical:before {
  content: "\e119";
}
.glyphicon-resize-horizontal:before {
  content: "\e120";
}
.glyphicon-hdd:before {
  content: "\e121";
}
.glyphicon-bullhorn:before {
  content: "\e122";
}
.glyphicon-bell:before {
  content: "\e123";
}
.glyphicon-certificate:before {
  content: "\e124";
}
.glyphicon-thumbs-up:before {
  content: "\e125";
}
.glyphicon-thumbs-down:before {
  content: "\e126";
}
.glyphicon-hand-right:before {
  content: "\e127";
}
.glyphicon-hand-left:before {
  content: "\e128";
}
.glyphicon-hand-up:before {
  content: "\e129";
}
.glyphicon-hand-down:before {
  content: "\e130";
}
.glyphicon-circle-arrow-right:before {
  content: "\e131";
}
.glyphicon-circle-arrow-left:before {
  content: "\e132";
}
.glyphicon-circle-arrow-up:before {
  content: "\e133";
}
.glyphicon-circle-arrow-down:before {
  content: "\e134";
}
.glyphicon-globe:before {
  content: "\e135";
}
.glyphicon-wrench:before {
  content: "\e136";
}
.glyphicon-tasks:before {
  content: "\e137";
}
.glyphicon-filter:before {
  content: "\e138";
}
.glyphicon-briefcase:before {
  content: "\e139";
}
.glyphicon-fullscreen:before {
  content: "\e140";
}
.glyphicon-dashboard:before {
  content: "\e141";
}
.glyphicon-paperclip:before {
  content: "\e142";
}
.glyphicon-heart-empty:before {
  content: "\e143";
}
.glyphicon-link:before {
  content: "\e144";
}
.glyphicon-phone:before {
  content: "\e145";
}
.glyphicon-pushpin:before {
  content: "\e146";
}
.glyphicon-usd:before {
  content: "\e148";
}
.glyphicon-gbp:before {
  content: "\e149";
}
.glyphicon-sort:before {
  content: "\e150";
}
.glyphicon-sort-by-alphabet:before {
  content: "\e151";
}
.glyphicon-sort-by-alphabet-alt:before {
  content: "\e152";
}
.glyphicon-sort-by-order:before {
  content: "\e153";
}
.glyphicon-sort-by-order-alt:before {
  content: "\e154";
}
.glyphicon-sort-by-attributes:before {
  content: "\e155";
}
.glyphicon-sort-by-attributes-alt:before {
  content: "\e156";
}
.glyphicon-unchecked:before {
  content: "\e157";
}
.glyphicon-expand:before {
  content: "\e158";
}
.glyphicon-collapse-down:before {
  content: "\e159";
}
.glyphicon-collapse-up:before {
  content: "\e160";
}
.glyphicon-log-in:before {
  content: "\e161";
}
.glyphicon-flash:before {
  content: "\e162";
}
.glyphicon-log-out:before {
  content: "\e163";
}
.glyphicon-new-window:before {
  content: "\e164";
}
.glyphicon-record:before {
  content: "\e165";
}
.glyphicon-save:before {
  content: "\e166";
}
.glyphicon-open:before {
  content: "\e167";
}
.glyphicon-saved:before {
  content: "\e168";
}
.glyphicon-import:before {
  content: "\e169";
}
.glyphicon-export:before {
  content: "\e170";
}
.glyphicon-send:before {
  content: "\e171";
}
.glyphicon-floppy-disk:before {
  content: "\e172";
}
.glyphicon-floppy-saved:before {
  content: "\e173";
}
.glyphicon-floppy-remove:before {
  content: "\e174";
}
.glyphicon-floppy-save:before {
  content: "\e175";
}
.glyphicon-floppy-open:before {
  content: "\e176";
}
.glyphicon-credit-card:before {
  content: "\e177";
}
.glyphicon-transfer:before {
  content: "\e178";
}
.glyphicon-cutlery:before {
  content: "\e179";
}
.glyphicon-header:before {
  content: "\e180";
}
.glyphicon-compressed:before {
  content: "\e181";
}
.glyphicon-earphone:before {
  content: "\e182";
}
.glyphicon-phone-alt:before {
  content: "\e183";
}
.glyphicon-tower:before {
  content: "\e184";
}
.glyphicon-stats:before {
  content: "\e185";
}
.glyphicon-sd-video:before {
  content: "\e186";
}
.glyphicon-hd-video:before {
  content: "\e187";
}
.glyphicon-subtitles:before {
  content: "\e188";
}
.glyphicon-sound-stereo:before {
  content: "\e189";
}
.glyphicon-sound-dolby:before {
  content: "\e190";
}
.glyphicon-sound-5-1:before {
  content: "\e191";
}
.glyphicon-sound-6-1:before {
  content: "\e192";
}
.glyphicon-sound-7-1:before {
  content: "\e193";
}
.glyphicon-copyright-mark:before {
  content: "\e194";
}
.glyphicon-registration-mark:before {
  content: "\e195";
}
.glyphicon-cloud-download:before {
  content: "\e197";
}
.glyphicon-cloud-upload:before {
  content: "\e198";
}
.glyphicon-tree-conifer:before {
  content: "\e199";
}
.glyphicon-tree-deciduous:before {
  content: "\e200";
}
.glyphicon-cd:before {
  content: "\e201";
}
.glyphicon-save-file:before {
  content: "\e202";
}
.glyphicon-open-file:before {
  content: "\e203";
}
.glyphicon-level-up:before {
  content: "\e204";
}
.glyphicon-copy:before {
  content: "\e205";
}
.glyphicon-paste:before {
  content: "\e206";
}
.glyphicon-alert:before {
  content: "\e209";
}
.glyphicon-equalizer:before {
  content: "\e210";
}
.glyphicon-king:before {
  content: "\e211";
}
.glyphicon-queen:before {
  content: "\e212";
}
.glyphicon-pawn:before {
  content: "\e213";
}
.glyphicon-bishop:before {
  content: "\e214";
}
.glyphicon-knight:before {
  content: "\e215";
}
.glyphicon-baby-formula:before {
  content: "\e216";
}
.glyphicon-tent:before {
  content: "\26fa";
}
.glyphicon-blackboard:before {
  content: "\e218";
}
.glyphicon-bed:before {
  content: "\e219";
}
.glyphicon-apple:before {
  content: "\f8ff";
}
.glyphicon-erase:before {
  content: "\e221";
}
.glyphicon-hourglass:before {
  content: "\231b";
}
.glyphicon-lamp:before {
  content: "\e223";
}
.glyphicon-duplicate:before {
  content: "\e224";
}
.glyphicon-piggy-bank:before {
  content: "\e225";
}
.glyphicon-scissors:before {
  content: "\e226";
}
.glyphicon-bitcoin:before {
  content: "\e227";
}
.glyphicon-btc:before {
  content: "\e227";
}
.glyphicon-xbt:before {
  content: "\e227";
}
.glyphicon-yen:before {
  content: "\00a5";
}
.glyphicon-jpy:before {
  content: "\00a5";
}
.glyphicon-ruble:before {
  content: "\20bd";
}
.glyphicon-rub:before {
  content: "\20bd";
}
.glyphicon-scale:before {
  content: "\e230";
}
.glyphicon-ice-lolly:before {
  content: "\e231";
}
.glyphicon-ice-lolly-tasted:before {
  content: "\e232";
}
.glyphicon-education:before {
  content: "\e233";
}
.glyphicon-option-horizontal:before {
  content: "\e234";
}
.glyphicon-option-vertical:before {
  content: "\e235";
}
.glyphicon-menu-hamburger:before {
  content: "\e236";
}
.glyphicon-modal-window:before {
  content: "\e237";
}
.glyphicon-oil:before {
  content: "\e238";
}
.glyphicon-grain:before {
  content: "\e239";
}
.glyphicon-sunglasses:before {
  content: "\e240";
}
.glyphicon-text-size:before {
  content: "\e241";
}
.glyphicon-text-color:before {
  content: "\e242";
}
.glyphicon-text-background:before {
  content: "\e243";
}
.glyphicon-object-align-top:before {
  content: "\e244";
}
.glyphicon-object-align-bottom:before {
  content: "\e245";
}
.glyphicon-object-align-horizontal:before {
  content: "\e246";
}
.glyphicon-object-align-left:before {
  content: "\e247";
}
.glyphicon-object-align-vertical:before {
  content: "\e248";
}
.glyphicon-object-align-right:before {
  content: "\e249";
}
.glyphicon-triangle-right:before {
  content: "\e250";
}
.glyphicon-triangle-left:before {
  content: "\e251";
}
.glyphicon-triangle-bottom:before {
  content: "\e252";
}
.glyphicon-triangle-top:before {
  content: "\e253";
}
.glyphicon-console:before {
  content: "\e254";
}
.glyphicon-superscript:before {
  content: "\e255";
}
.glyphicon-subscript:before {
  content: "\e256";
}
.glyphicon-menu-left:before {
  content: "\e257";
}
.glyphicon-menu-right:before {
  content: "\e258";
}
.glyphicon-menu-down:before {
  content: "\e259";
}
.glyphicon-menu-up:before {
  content: "\e260";
}
* {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
*:before,
*:after {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
html {
  font-size: 10px;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}
body {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 13px;
  line-height: 1.42857143;
  color: #000;
  background-color: #fff;
}
input,
button,
select,
textarea {
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
}
a {
  color: #337ab7;
  text-decoration: none;
}
a:hover,
a:focus {
  color: #23527c;
  text-decoration: underline;
}
a:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
figure {
  margin: 0;
}
img {
  vertical-align: middle;
}
.img-responsive,
.thumbnail > img,
.thumbnail a > img,
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  display: block;
  max-width: 100%;
  height: auto;
}
.img-rounded {
  border-radius: 3px;
}
.img-thumbnail {
  padding: 4px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: all 0.2s ease-in-out;
  -o-transition: all 0.2s ease-in-out;
  transition: all 0.2s ease-in-out;
  display: inline-block;
  max-width: 100%;
  height: auto;
}
.img-circle {
  border-radius: 50%;
}
hr {
  margin-top: 18px;
  margin-bottom: 18px;
  border: 0;
  border-top: 1px solid #eeeeee;
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
[role="button"] {
  cursor: pointer;
}
h1,
h2,
h3,
h4,
h5,
h6,
.h1,
.h2,
.h3,
.h4,
.h5,
.h6 {
  font-family: inherit;
  font-weight: 500;
  line-height: 1.1;
  color: inherit;
}
h1 small,
h2 small,
h3 small,
h4 small,
h5 small,
h6 small,
.h1 small,
.h2 small,
.h3 small,
.h4 small,
.h5 small,
.h6 small,
h1 .small,
h2 .small,
h3 .small,
h4 .small,
h5 .small,
h6 .small,
.h1 .small,
.h2 .small,
.h3 .small,
.h4 .small,
.h5 .small,
.h6 .small {
  font-weight: normal;
  line-height: 1;
  color: #777777;
}
h1,
.h1,
h2,
.h2,
h3,
.h3 {
  margin-top: 18px;
  margin-bottom: 9px;
}
h1 small,
.h1 small,
h2 small,
.h2 small,
h3 small,
.h3 small,
h1 .small,
.h1 .small,
h2 .small,
.h2 .small,
h3 .small,
.h3 .small {
  font-size: 65%;
}
h4,
.h4,
h5,
.h5,
h6,
.h6 {
  margin-top: 9px;
  margin-bottom: 9px;
}
h4 small,
.h4 small,
h5 small,
.h5 small,
h6 small,
.h6 small,
h4 .small,
.h4 .small,
h5 .small,
.h5 .small,
h6 .small,
.h6 .small {
  font-size: 75%;
}
h1,
.h1 {
  font-size: 33px;
}
h2,
.h2 {
  font-size: 27px;
}
h3,
.h3 {
  font-size: 23px;
}
h4,
.h4 {
  font-size: 17px;
}
h5,
.h5 {
  font-size: 13px;
}
h6,
.h6 {
  font-size: 12px;
}
p {
  margin: 0 0 9px;
}
.lead {
  margin-bottom: 18px;
  font-size: 14px;
  font-weight: 300;
  line-height: 1.4;
}
@media (min-width: 768px) {
  .lead {
    font-size: 19.5px;
  }
}
small,
.small {
  font-size: 92%;
}
mark,
.mark {
  background-color: #fcf8e3;
  padding: .2em;
}
.text-left {
  text-align: left;
}
.text-right {
  text-align: right;
}
.text-center {
  text-align: center;
}
.text-justify {
  text-align: justify;
}
.text-nowrap {
  white-space: nowrap;
}
.text-lowercase {
  text-transform: lowercase;
}
.text-uppercase {
  text-transform: uppercase;
}
.text-capitalize {
  text-transform: capitalize;
}
.text-muted {
  color: #777777;
}
.text-primary {
  color: #337ab7;
}
a.text-primary:hover,
a.text-primary:focus {
  color: #286090;
}
.text-success {
  color: #3c763d;
}
a.text-success:hover,
a.text-success:focus {
  color: #2b542c;
}
.text-info {
  color: #31708f;
}
a.text-info:hover,
a.text-info:focus {
  color: #245269;
}
.text-warning {
  color: #8a6d3b;
}
a.text-warning:hover,
a.text-warning:focus {
  color: #66512c;
}
.text-danger {
  color: #a94442;
}
a.text-danger:hover,
a.text-danger:focus {
  color: #843534;
}
.bg-primary {
  color: #fff;
  background-color: #337ab7;
}
a.bg-primary:hover,
a.bg-primary:focus {
  background-color: #286090;
}
.bg-success {
  background-color: #dff0d8;
}
a.bg-success:hover,
a.bg-success:focus {
  background-color: #c1e2b3;
}
.bg-info {
  background-color: #d9edf7;
}
a.bg-info:hover,
a.bg-info:focus {
  background-color: #afd9ee;
}
.bg-warning {
  background-color: #fcf8e3;
}
a.bg-warning:hover,
a.bg-warning:focus {
  background-color: #f7ecb5;
}
.bg-danger {
  background-color: #f2dede;
}
a.bg-danger:hover,
a.bg-danger:focus {
  background-color: #e4b9b9;
}
.page-header {
  padding-bottom: 8px;
  margin: 36px 0 18px;
  border-bottom: 1px solid #eeeeee;
}
ul,
ol {
  margin-top: 0;
  margin-bottom: 9px;
}
ul ul,
ol ul,
ul ol,
ol ol {
  margin-bottom: 0;
}
.list-unstyled {
  padding-left: 0;
  list-style: none;
}
.list-inline {
  padding-left: 0;
  list-style: none;
  margin-left: -5px;
}
.list-inline > li {
  display: inline-block;
  padding-left: 5px;
  padding-right: 5px;
}
dl {
  margin-top: 0;
  margin-bottom: 18px;
}
dt,
dd {
  line-height: 1.42857143;
}
dt {
  font-weight: bold;
}
dd {
  margin-left: 0;
}
@media (min-width: 541px) {
  .dl-horizontal dt {
    float: left;
    width: 160px;
    clear: left;
    text-align: right;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .dl-horizontal dd {
    margin-left: 180px;
  }
}
abbr[title],
abbr[data-original-title] {
  cursor: help;
  border-bottom: 1px dotted #777777;
}
.initialism {
  font-size: 90%;
  text-transform: uppercase;
}
blockquote {
  padding: 9px 18px;
  margin: 0 0 18px;
  font-size: inherit;
  border-left: 5px solid #eeeeee;
}
blockquote p:last-child,
blockquote ul:last-child,
blockquote ol:last-child {
  margin-bottom: 0;
}
blockquote footer,
blockquote small,
blockquote .small {
  display: block;
  font-size: 80%;
  line-height: 1.42857143;
  color: #777777;
}
blockquote footer:before,
blockquote small:before,
blockquote .small:before {
  content: '\2014 \00A0';
}
.blockquote-reverse,
blockquote.pull-right {
  padding-right: 15px;
  padding-left: 0;
  border-right: 5px solid #eeeeee;
  border-left: 0;
  text-align: right;
}
.blockquote-reverse footer:before,
blockquote.pull-right footer:before,
.blockquote-reverse small:before,
blockquote.pull-right small:before,
.blockquote-reverse .small:before,
blockquote.pull-right .small:before {
  content: '';
}
.blockquote-reverse footer:after,
blockquote.pull-right footer:after,
.blockquote-reverse small:after,
blockquote.pull-right small:after,
.blockquote-reverse .small:after,
blockquote.pull-right .small:after {
  content: '\00A0 \2014';
}
address {
  margin-bottom: 18px;
  font-style: normal;
  line-height: 1.42857143;
}
code,
kbd,
pre,
samp {
  font-family: monospace;
}
code {
  padding: 2px 4px;
  font-size: 90%;
  color: #c7254e;
  background-color: #f9f2f4;
  border-radius: 2px;
}
kbd {
  padding: 2px 4px;
  font-size: 90%;
  color: #888;
  background-color: transparent;
  border-radius: 1px;
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.25);
}
kbd kbd {
  padding: 0;
  font-size: 100%;
  font-weight: bold;
  box-shadow: none;
}
pre {
  display: block;
  padding: 8.5px;
  margin: 0 0 9px;
  font-size: 12px;
  line-height: 1.42857143;
  word-break: break-all;
  word-wrap: break-word;
  color: #333333;
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  border-radius: 2px;
}
pre code {
  padding: 0;
  font-size: inherit;
  color: inherit;
  white-space: pre-wrap;
  background-color: transparent;
  border-radius: 0;
}
.pre-scrollable {
  max-height: 340px;
  overflow-y: scroll;
}
.container {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
@media (min-width: 768px) {
  .container {
    width: 768px;
  }
}
@media (min-width: 992px) {
  .container {
    width: 940px;
  }
}
@media (min-width: 1200px) {
  .container {
    width: 1140px;
  }
}
.container-fluid {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
.row {
  margin-left: 0px;
  margin-right: 0px;
}
.col-xs-1, .col-sm-1, .col-md-1, .col-lg-1, .col-xs-2, .col-sm-2, .col-md-2, .col-lg-2, .col-xs-3, .col-sm-3, .col-md-3, .col-lg-3, .col-xs-4, .col-sm-4, .col-md-4, .col-lg-4, .col-xs-5, .col-sm-5, .col-md-5, .col-lg-5, .col-xs-6, .col-sm-6, .col-md-6, .col-lg-6, .col-xs-7, .col-sm-7, .col-md-7, .col-lg-7, .col-xs-8, .col-sm-8, .col-md-8, .col-lg-8, .col-xs-9, .col-sm-9, .col-md-9, .col-lg-9, .col-xs-10, .col-sm-10, .col-md-10, .col-lg-10, .col-xs-11, .col-sm-11, .col-md-11, .col-lg-11, .col-xs-12, .col-sm-12, .col-md-12, .col-lg-12 {
  position: relative;
  min-height: 1px;
  padding-left: 0px;
  padding-right: 0px;
}
.col-xs-1, .col-xs-2, .col-xs-3, .col-xs-4, .col-xs-5, .col-xs-6, .col-xs-7, .col-xs-8, .col-xs-9, .col-xs-10, .col-xs-11, .col-xs-12 {
  float: left;
}
.col-xs-12 {
  width: 100%;
}
.col-xs-11 {
  width: 91.66666667%;
}
.col-xs-10 {
  width: 83.33333333%;
}
.col-xs-9 {
  width: 75%;
}
.col-xs-8 {
  width: 66.66666667%;
}
.col-xs-7 {
  width: 58.33333333%;
}
.col-xs-6 {
  width: 50%;
}
.col-xs-5 {
  width: 41.66666667%;
}
.col-xs-4 {
  width: 33.33333333%;
}
.col-xs-3 {
  width: 25%;
}
.col-xs-2 {
  width: 16.66666667%;
}
.col-xs-1 {
  width: 8.33333333%;
}
.col-xs-pull-12 {
  right: 100%;
}
.col-xs-pull-11 {
  right: 91.66666667%;
}
.col-xs-pull-10 {
  right: 83.33333333%;
}
.col-xs-pull-9 {
  right: 75%;
}
.col-xs-pull-8 {
  right: 66.66666667%;
}
.col-xs-pull-7 {
  right: 58.33333333%;
}
.col-xs-pull-6 {
  right: 50%;
}
.col-xs-pull-5 {
  right: 41.66666667%;
}
.col-xs-pull-4 {
  right: 33.33333333%;
}
.col-xs-pull-3 {
  right: 25%;
}
.col-xs-pull-2 {
  right: 16.66666667%;
}
.col-xs-pull-1 {
  right: 8.33333333%;
}
.col-xs-pull-0 {
  right: auto;
}
.col-xs-push-12 {
  left: 100%;
}
.col-xs-push-11 {
  left: 91.66666667%;
}
.col-xs-push-10 {
  left: 83.33333333%;
}
.col-xs-push-9 {
  left: 75%;
}
.col-xs-push-8 {
  left: 66.66666667%;
}
.col-xs-push-7 {
  left: 58.33333333%;
}
.col-xs-push-6 {
  left: 50%;
}
.col-xs-push-5 {
  left: 41.66666667%;
}
.col-xs-push-4 {
  left: 33.33333333%;
}
.col-xs-push-3 {
  left: 25%;
}
.col-xs-push-2 {
  left: 16.66666667%;
}
.col-xs-push-1 {
  left: 8.33333333%;
}
.col-xs-push-0 {
  left: auto;
}
.col-xs-offset-12 {
  margin-left: 100%;
}
.col-xs-offset-11 {
  margin-left: 91.66666667%;
}
.col-xs-offset-10 {
  margin-left: 83.33333333%;
}
.col-xs-offset-9 {
  margin-left: 75%;
}
.col-xs-offset-8 {
  margin-left: 66.66666667%;
}
.col-xs-offset-7 {
  margin-left: 58.33333333%;
}
.col-xs-offset-6 {
  margin-left: 50%;
}
.col-xs-offset-5 {
  margin-left: 41.66666667%;
}
.col-xs-offset-4 {
  margin-left: 33.33333333%;
}
.col-xs-offset-3 {
  margin-left: 25%;
}
.col-xs-offset-2 {
  margin-left: 16.66666667%;
}
.col-xs-offset-1 {
  margin-left: 8.33333333%;
}
.col-xs-offset-0 {
  margin-left: 0%;
}
@media (min-width: 768px) {
  .col-sm-1, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9, .col-sm-10, .col-sm-11, .col-sm-12 {
    float: left;
  }
  .col-sm-12 {
    width: 100%;
  }
  .col-sm-11 {
    width: 91.66666667%;
  }
  .col-sm-10 {
    width: 83.33333333%;
  }
  .col-sm-9 {
    width: 75%;
  }
  .col-sm-8 {
    width: 66.66666667%;
  }
  .col-sm-7 {
    width: 58.33333333%;
  }
  .col-sm-6 {
    width: 50%;
  }
  .col-sm-5 {
    width: 41.66666667%;
  }
  .col-sm-4 {
    width: 33.33333333%;
  }
  .col-sm-3 {
    width: 25%;
  }
  .col-sm-2 {
    width: 16.66666667%;
  }
  .col-sm-1 {
    width: 8.33333333%;
  }
  .col-sm-pull-12 {
    right: 100%;
  }
  .col-sm-pull-11 {
    right: 91.66666667%;
  }
  .col-sm-pull-10 {
    right: 83.33333333%;
  }
  .col-sm-pull-9 {
    right: 75%;
  }
  .col-sm-pull-8 {
    right: 66.66666667%;
  }
  .col-sm-pull-7 {
    right: 58.33333333%;
  }
  .col-sm-pull-6 {
    right: 50%;
  }
  .col-sm-pull-5 {
    right: 41.66666667%;
  }
  .col-sm-pull-4 {
    right: 33.33333333%;
  }
  .col-sm-pull-3 {
    right: 25%;
  }
  .col-sm-pull-2 {
    right: 16.66666667%;
  }
  .col-sm-pull-1 {
    right: 8.33333333%;
  }
  .col-sm-pull-0 {
    right: auto;
  }
  .col-sm-push-12 {
    left: 100%;
  }
  .col-sm-push-11 {
    left: 91.66666667%;
  }
  .col-sm-push-10 {
    left: 83.33333333%;
  }
  .col-sm-push-9 {
    left: 75%;
  }
  .col-sm-push-8 {
    left: 66.66666667%;
  }
  .col-sm-push-7 {
    left: 58.33333333%;
  }
  .col-sm-push-6 {
    left: 50%;
  }
  .col-sm-push-5 {
    left: 41.66666667%;
  }
  .col-sm-push-4 {
    left: 33.33333333%;
  }
  .col-sm-push-3 {
    left: 25%;
  }
  .col-sm-push-2 {
    left: 16.66666667%;
  }
  .col-sm-push-1 {
    left: 8.33333333%;
  }
  .col-sm-push-0 {
    left: auto;
  }
  .col-sm-offset-12 {
    margin-left: 100%;
  }
  .col-sm-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-sm-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-sm-offset-9 {
    margin-left: 75%;
  }
  .col-sm-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-sm-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-sm-offset-6 {
    margin-left: 50%;
  }
  .col-sm-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-sm-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-sm-offset-3 {
    margin-left: 25%;
  }
  .col-sm-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-sm-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-sm-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 992px) {
  .col-md-1, .col-md-2, .col-md-3, .col-md-4, .col-md-5, .col-md-6, .col-md-7, .col-md-8, .col-md-9, .col-md-10, .col-md-11, .col-md-12 {
    float: left;
  }
  .col-md-12 {
    width: 100%;
  }
  .col-md-11 {
    width: 91.66666667%;
  }
  .col-md-10 {
    width: 83.33333333%;
  }
  .col-md-9 {
    width: 75%;
  }
  .col-md-8 {
    width: 66.66666667%;
  }
  .col-md-7 {
    width: 58.33333333%;
  }
  .col-md-6 {
    width: 50%;
  }
  .col-md-5 {
    width: 41.66666667%;
  }
  .col-md-4 {
    width: 33.33333333%;
  }
  .col-md-3 {
    width: 25%;
  }
  .col-md-2 {
    width: 16.66666667%;
  }
  .col-md-1 {
    width: 8.33333333%;
  }
  .col-md-pull-12 {
    right: 100%;
  }
  .col-md-pull-11 {
    right: 91.66666667%;
  }
  .col-md-pull-10 {
    right: 83.33333333%;
  }
  .col-md-pull-9 {
    right: 75%;
  }
  .col-md-pull-8 {
    right: 66.66666667%;
  }
  .col-md-pull-7 {
    right: 58.33333333%;
  }
  .col-md-pull-6 {
    right: 50%;
  }
  .col-md-pull-5 {
    right: 41.66666667%;
  }
  .col-md-pull-4 {
    right: 33.33333333%;
  }
  .col-md-pull-3 {
    right: 25%;
  }
  .col-md-pull-2 {
    right: 16.66666667%;
  }
  .col-md-pull-1 {
    right: 8.33333333%;
  }
  .col-md-pull-0 {
    right: auto;
  }
  .col-md-push-12 {
    left: 100%;
  }
  .col-md-push-11 {
    left: 91.66666667%;
  }
  .col-md-push-10 {
    left: 83.33333333%;
  }
  .col-md-push-9 {
    left: 75%;
  }
  .col-md-push-8 {
    left: 66.66666667%;
  }
  .col-md-push-7 {
    left: 58.33333333%;
  }
  .col-md-push-6 {
    left: 50%;
  }
  .col-md-push-5 {
    left: 41.66666667%;
  }
  .col-md-push-4 {
    left: 33.33333333%;
  }
  .col-md-push-3 {
    left: 25%;
  }
  .col-md-push-2 {
    left: 16.66666667%;
  }
  .col-md-push-1 {
    left: 8.33333333%;
  }
  .col-md-push-0 {
    left: auto;
  }
  .col-md-offset-12 {
    margin-left: 100%;
  }
  .col-md-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-md-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-md-offset-9 {
    margin-left: 75%;
  }
  .col-md-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-md-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-md-offset-6 {
    margin-left: 50%;
  }
  .col-md-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-md-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-md-offset-3 {
    margin-left: 25%;
  }
  .col-md-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-md-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-md-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 1200px) {
  .col-lg-1, .col-lg-2, .col-lg-3, .col-lg-4, .col-lg-5, .col-lg-6, .col-lg-7, .col-lg-8, .col-lg-9, .col-lg-10, .col-lg-11, .col-lg-12 {
    float: left;
  }
  .col-lg-12 {
    width: 100%;
  }
  .col-lg-11 {
    width: 91.66666667%;
  }
  .col-lg-10 {
    width: 83.33333333%;
  }
  .col-lg-9 {
    width: 75%;
  }
  .col-lg-8 {
    width: 66.66666667%;
  }
  .col-lg-7 {
    width: 58.33333333%;
  }
  .col-lg-6 {
    width: 50%;
  }
  .col-lg-5 {
    width: 41.66666667%;
  }
  .col-lg-4 {
    width: 33.33333333%;
  }
  .col-lg-3 {
    width: 25%;
  }
  .col-lg-2 {
    width: 16.66666667%;
  }
  .col-lg-1 {
    width: 8.33333333%;
  }
  .col-lg-pull-12 {
    right: 100%;
  }
  .col-lg-pull-11 {
    right: 91.66666667%;
  }
  .col-lg-pull-10 {
    right: 83.33333333%;
  }
  .col-lg-pull-9 {
    right: 75%;
  }
  .col-lg-pull-8 {
    right: 66.66666667%;
  }
  .col-lg-pull-7 {
    right: 58.33333333%;
  }
  .col-lg-pull-6 {
    right: 50%;
  }
  .col-lg-pull-5 {
    right: 41.66666667%;
  }
  .col-lg-pull-4 {
    right: 33.33333333%;
  }
  .col-lg-pull-3 {
    right: 25%;
  }
  .col-lg-pull-2 {
    right: 16.66666667%;
  }
  .col-lg-pull-1 {
    right: 8.33333333%;
  }
  .col-lg-pull-0 {
    right: auto;
  }
  .col-lg-push-12 {
    left: 100%;
  }
  .col-lg-push-11 {
    left: 91.66666667%;
  }
  .col-lg-push-10 {
    left: 83.33333333%;
  }
  .col-lg-push-9 {
    left: 75%;
  }
  .col-lg-push-8 {
    left: 66.66666667%;
  }
  .col-lg-push-7 {
    left: 58.33333333%;
  }
  .col-lg-push-6 {
    left: 50%;
  }
  .col-lg-push-5 {
    left: 41.66666667%;
  }
  .col-lg-push-4 {
    left: 33.33333333%;
  }
  .col-lg-push-3 {
    left: 25%;
  }
  .col-lg-push-2 {
    left: 16.66666667%;
  }
  .col-lg-push-1 {
    left: 8.33333333%;
  }
  .col-lg-push-0 {
    left: auto;
  }
  .col-lg-offset-12 {
    margin-left: 100%;
  }
  .col-lg-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-lg-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-lg-offset-9 {
    margin-left: 75%;
  }
  .col-lg-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-lg-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-lg-offset-6 {
    margin-left: 50%;
  }
  .col-lg-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-lg-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-lg-offset-3 {
    margin-left: 25%;
  }
  .col-lg-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-lg-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-lg-offset-0 {
    margin-left: 0%;
  }
}
table {
  background-color: transparent;
}
caption {
  padding-top: 8px;
  padding-bottom: 8px;
  color: #777777;
  text-align: left;
}
th {
  text-align: left;
}
.table {
  width: 100%;
  max-width: 100%;
  margin-bottom: 18px;
}
.table > thead > tr > th,
.table > tbody > tr > th,
.table > tfoot > tr > th,
.table > thead > tr > td,
.table > tbody > tr > td,
.table > tfoot > tr > td {
  padding: 8px;
  line-height: 1.42857143;
  vertical-align: top;
  border-top: 1px solid #ddd;
}
.table > thead > tr > th {
  vertical-align: bottom;
  border-bottom: 2px solid #ddd;
}
.table > caption + thead > tr:first-child > th,
.table > colgroup + thead > tr:first-child > th,
.table > thead:first-child > tr:first-child > th,
.table > caption + thead > tr:first-child > td,
.table > colgroup + thead > tr:first-child > td,
.table > thead:first-child > tr:first-child > td {
  border-top: 0;
}
.table > tbody + tbody {
  border-top: 2px solid #ddd;
}
.table .table {
  background-color: #fff;
}
.table-condensed > thead > tr > th,
.table-condensed > tbody > tr > th,
.table-condensed > tfoot > tr > th,
.table-condensed > thead > tr > td,
.table-condensed > tbody > tr > td,
.table-condensed > tfoot > tr > td {
  padding: 5px;
}
.table-bordered {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > tbody > tr > th,
.table-bordered > tfoot > tr > th,
.table-bordered > thead > tr > td,
.table-bordered > tbody > tr > td,
.table-bordered > tfoot > tr > td {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > thead > tr > td {
  border-bottom-width: 2px;
}
.table-striped > tbody > tr:nth-of-type(odd) {
  background-color: #f9f9f9;
}
.table-hover > tbody > tr:hover {
  background-color: #f5f5f5;
}
table col[class*="col-"] {
  position: static;
  float: none;
  display: table-column;
}
table td[class*="col-"],
table th[class*="col-"] {
  position: static;
  float: none;
  display: table-cell;
}
.table > thead > tr > td.active,
.table > tbody > tr > td.active,
.table > tfoot > tr > td.active,
.table > thead > tr > th.active,
.table > tbody > tr > th.active,
.table > tfoot > tr > th.active,
.table > thead > tr.active > td,
.table > tbody > tr.active > td,
.table > tfoot > tr.active > td,
.table > thead > tr.active > th,
.table > tbody > tr.active > th,
.table > tfoot > tr.active > th {
  background-color: #f5f5f5;
}
.table-hover > tbody > tr > td.active:hover,
.table-hover > tbody > tr > th.active:hover,
.table-hover > tbody > tr.active:hover > td,
.table-hover > tbody > tr:hover > .active,
.table-hover > tbody > tr.active:hover > th {
  background-color: #e8e8e8;
}
.table > thead > tr > td.success,
.table > tbody > tr > td.success,
.table > tfoot > tr > td.success,
.table > thead > tr > th.success,
.table > tbody > tr > th.success,
.table > tfoot > tr > th.success,
.table > thead > tr.success > td,
.table > tbody > tr.success > td,
.table > tfoot > tr.success > td,
.table > thead > tr.success > th,
.table > tbody > tr.success > th,
.table > tfoot > tr.success > th {
  background-color: #dff0d8;
}
.table-hover > tbody > tr > td.success:hover,
.table-hover > tbody > tr > th.success:hover,
.table-hover > tbody > tr.success:hover > td,
.table-hover > tbody > tr:hover > .success,
.table-hover > tbody > tr.success:hover > th {
  background-color: #d0e9c6;
}
.table > thead > tr > td.info,
.table > tbody > tr > td.info,
.table > tfoot > tr > td.info,
.table > thead > tr > th.info,
.table > tbody > tr > th.info,
.table > tfoot > tr > th.info,
.table > thead > tr.info > td,
.table > tbody > tr.info > td,
.table > tfoot > tr.info > td,
.table > thead > tr.info > th,
.table > tbody > tr.info > th,
.table > tfoot > tr.info > th {
  background-color: #d9edf7;
}
.table-hover > tbody > tr > td.info:hover,
.table-hover > tbody > tr > th.info:hover,
.table-hover > tbody > tr.info:hover > td,
.table-hover > tbody > tr:hover > .info,
.table-hover > tbody > tr.info:hover > th {
  background-color: #c4e3f3;
}
.table > thead > tr > td.warning,
.table > tbody > tr > td.warning,
.table > tfoot > tr > td.warning,
.table > thead > tr > th.warning,
.table > tbody > tr > th.warning,
.table > tfoot > tr > th.warning,
.table > thead > tr.warning > td,
.table > tbody > tr.warning > td,
.table > tfoot > tr.warning > td,
.table > thead > tr.warning > th,
.table > tbody > tr.warning > th,
.table > tfoot > tr.warning > th {
  background-color: #fcf8e3;
}
.table-hover > tbody > tr > td.warning:hover,
.table-hover > tbody > tr > th.warning:hover,
.table-hover > tbody > tr.warning:hover > td,
.table-hover > tbody > tr:hover > .warning,
.table-hover > tbody > tr.warning:hover > th {
  background-color: #faf2cc;
}
.table > thead > tr > td.danger,
.table > tbody > tr > td.danger,
.table > tfoot > tr > td.danger,
.table > thead > tr > th.danger,
.table > tbody > tr > th.danger,
.table > tfoot > tr > th.danger,
.table > thead > tr.danger > td,
.table > tbody > tr.danger > td,
.table > tfoot > tr.danger > td,
.table > thead > tr.danger > th,
.table > tbody > tr.danger > th,
.table > tfoot > tr.danger > th {
  background-color: #f2dede;
}
.table-hover > tbody > tr > td.danger:hover,
.table-hover > tbody > tr > th.danger:hover,
.table-hover > tbody > tr.danger:hover > td,
.table-hover > tbody > tr:hover > .danger,
.table-hover > tbody > tr.danger:hover > th {
  background-color: #ebcccc;
}
.table-responsive {
  overflow-x: auto;
  min-height: 0.01%;
}
@media screen and (max-width: 767px) {
  .table-responsive {
    width: 100%;
    margin-bottom: 13.5px;
    overflow-y: hidden;
    -ms-overflow-style: -ms-autohiding-scrollbar;
    border: 1px solid #ddd;
  }
  .table-responsive > .table {
    margin-bottom: 0;
  }
  .table-responsive > .table > thead > tr > th,
  .table-responsive > .table > tbody > tr > th,
  .table-responsive > .table > tfoot > tr > th,
  .table-responsive > .table > thead > tr > td,
  .table-responsive > .table > tbody > tr > td,
  .table-responsive > .table > tfoot > tr > td {
    white-space: nowrap;
  }
  .table-responsive > .table-bordered {
    border: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:first-child,
  .table-responsive > .table-bordered > tbody > tr > th:first-child,
  .table-responsive > .table-bordered > tfoot > tr > th:first-child,
  .table-responsive > .table-bordered > thead > tr > td:first-child,
  .table-responsive > .table-bordered > tbody > tr > td:first-child,
  .table-responsive > .table-bordered > tfoot > tr > td:first-child {
    border-left: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:last-child,
  .table-responsive > .table-bordered > tbody > tr > th:last-child,
  .table-responsive > .table-bordered > tfoot > tr > th:last-child,
  .table-responsive > .table-bordered > thead > tr > td:last-child,
  .table-responsive > .table-bordered > tbody > tr > td:last-child,
  .table-responsive > .table-bordered > tfoot > tr > td:last-child {
    border-right: 0;
  }
  .table-responsive > .table-bordered > tbody > tr:last-child > th,
  .table-responsive > .table-bordered > tfoot > tr:last-child > th,
  .table-responsive > .table-bordered > tbody > tr:last-child > td,
  .table-responsive > .table-bordered > tfoot > tr:last-child > td {
    border-bottom: 0;
  }
}
fieldset {
  padding: 0;
  margin: 0;
  border: 0;
  min-width: 0;
}
legend {
  display: block;
  width: 100%;
  padding: 0;
  margin-bottom: 18px;
  font-size: 19.5px;
  line-height: inherit;
  color: #333333;
  border: 0;
  border-bottom: 1px solid #e5e5e5;
}
label {
  display: inline-block;
  max-width: 100%;
  margin-bottom: 5px;
  font-weight: bold;
}
input[type="search"] {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
input[type="radio"],
input[type="checkbox"] {
  margin: 4px 0 0;
  margin-top: 1px \9;
  line-height: normal;
}
input[type="file"] {
  display: block;
}
input[type="range"] {
  display: block;
  width: 100%;
}
select[multiple],
select[size] {
  height: auto;
}
input[type="file"]:focus,
input[type="radio"]:focus,
input[type="checkbox"]:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
output {
  display: block;
  padding-top: 7px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
}
.form-control {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
}
.form-control:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.form-control::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.form-control:-ms-input-placeholder {
  color: #999;
}
.form-control::-webkit-input-placeholder {
  color: #999;
}
.form-control::-ms-expand {
  border: 0;
  background-color: transparent;
}
.form-control[disabled],
.form-control[readonly],
fieldset[disabled] .form-control {
  background-color: #eeeeee;
  opacity: 1;
}
.form-control[disabled],
fieldset[disabled] .form-control {
  cursor: not-allowed;
}
textarea.form-control {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: none;
}
@media screen and (-webkit-min-device-pixel-ratio: 0) {
  input[type="date"].form-control,
  input[type="time"].form-control,
  input[type="datetime-local"].form-control,
  input[type="month"].form-control {
    line-height: 32px;
  }
  input[type="date"].input-sm,
  input[type="time"].input-sm,
  input[type="datetime-local"].input-sm,
  input[type="month"].input-sm,
  .input-group-sm input[type="date"],
  .input-group-sm input[type="time"],
  .input-group-sm input[type="datetime-local"],
  .input-group-sm input[type="month"] {
    line-height: 30px;
  }
  input[type="date"].input-lg,
  input[type="time"].input-lg,
  input[type="datetime-local"].input-lg,
  input[type="month"].input-lg,
  .input-group-lg input[type="date"],
  .input-group-lg input[type="time"],
  .input-group-lg input[type="datetime-local"],
  .input-group-lg input[type="month"] {
    line-height: 45px;
  }
}
.form-group {
  margin-bottom: 15px;
}
.radio,
.checkbox {
  position: relative;
  display: block;
  margin-top: 10px;
  margin-bottom: 10px;
}
.radio label,
.checkbox label {
  min-height: 18px;
  padding-left: 20px;
  margin-bottom: 0;
  font-weight: normal;
  cursor: pointer;
}
.radio input[type="radio"],
.radio-inline input[type="radio"],
.checkbox input[type="checkbox"],
.checkbox-inline input[type="checkbox"] {
  position: absolute;
  margin-left: -20px;
  margin-top: 4px \9;
}
.radio + .radio,
.checkbox + .checkbox {
  margin-top: -5px;
}
.radio-inline,
.checkbox-inline {
  position: relative;
  display: inline-block;
  padding-left: 20px;
  margin-bottom: 0;
  vertical-align: middle;
  font-weight: normal;
  cursor: pointer;
}
.radio-inline + .radio-inline,
.checkbox-inline + .checkbox-inline {
  margin-top: 0;
  margin-left: 10px;
}
input[type="radio"][disabled],
input[type="checkbox"][disabled],
input[type="radio"].disabled,
input[type="checkbox"].disabled,
fieldset[disabled] input[type="radio"],
fieldset[disabled] input[type="checkbox"] {
  cursor: not-allowed;
}
.radio-inline.disabled,
.checkbox-inline.disabled,
fieldset[disabled] .radio-inline,
fieldset[disabled] .checkbox-inline {
  cursor: not-allowed;
}
.radio.disabled label,
.checkbox.disabled label,
fieldset[disabled] .radio label,
fieldset[disabled] .checkbox label {
  cursor: not-allowed;
}
.form-control-static {
  padding-top: 7px;
  padding-bottom: 7px;
  margin-bottom: 0;
  min-height: 31px;
}
.form-control-static.input-lg,
.form-control-static.input-sm {
  padding-left: 0;
  padding-right: 0;
}
.input-sm {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-sm {
  height: 30px;
  line-height: 30px;
}
textarea.input-sm,
select[multiple].input-sm {
  height: auto;
}
.form-group-sm .form-control {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.form-group-sm select.form-control {
  height: 30px;
  line-height: 30px;
}
.form-group-sm textarea.form-control,
.form-group-sm select[multiple].form-control {
  height: auto;
}
.form-group-sm .form-control-static {
  height: 30px;
  min-height: 30px;
  padding: 6px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.input-lg {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-lg {
  height: 45px;
  line-height: 45px;
}
textarea.input-lg,
select[multiple].input-lg {
  height: auto;
}
.form-group-lg .form-control {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.form-group-lg select.form-control {
  height: 45px;
  line-height: 45px;
}
.form-group-lg textarea.form-control,
.form-group-lg select[multiple].form-control {
  height: auto;
}
.form-group-lg .form-control-static {
  height: 45px;
  min-height: 35px;
  padding: 11px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.has-feedback {
  position: relative;
}
.has-feedback .form-control {
  padding-right: 40px;
}
.form-control-feedback {
  position: absolute;
  top: 0;
  right: 0;
  z-index: 2;
  display: block;
  width: 32px;
  height: 32px;
  line-height: 32px;
  text-align: center;
  pointer-events: none;
}
.input-lg + .form-control-feedback,
.input-group-lg + .form-control-feedback,
.form-group-lg .form-control + .form-control-feedback {
  width: 45px;
  height: 45px;
  line-height: 45px;
}
.input-sm + .form-control-feedback,
.input-group-sm + .form-control-feedback,
.form-group-sm .form-control + .form-control-feedback {
  width: 30px;
  height: 30px;
  line-height: 30px;
}
.has-success .help-block,
.has-success .control-label,
.has-success .radio,
.has-success .checkbox,
.has-success .radio-inline,
.has-success .checkbox-inline,
.has-success.radio label,
.has-success.checkbox label,
.has-success.radio-inline label,
.has-success.checkbox-inline label {
  color: #3c763d;
}
.has-success .form-control {
  border-color: #3c763d;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-success .form-control:focus {
  border-color: #2b542c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
}
.has-success .input-group-addon {
  color: #3c763d;
  border-color: #3c763d;
  background-color: #dff0d8;
}
.has-success .form-control-feedback {
  color: #3c763d;
}
.has-warning .help-block,
.has-warning .control-label,
.has-warning .radio,
.has-warning .checkbox,
.has-warning .radio-inline,
.has-warning .checkbox-inline,
.has-warning.radio label,
.has-warning.checkbox label,
.has-warning.radio-inline label,
.has-warning.checkbox-inline label {
  color: #8a6d3b;
}
.has-warning .form-control {
  border-color: #8a6d3b;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-warning .form-control:focus {
  border-color: #66512c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
}
.has-warning .input-group-addon {
  color: #8a6d3b;
  border-color: #8a6d3b;
  background-color: #fcf8e3;
}
.has-warning .form-control-feedback {
  color: #8a6d3b;
}
.has-error .help-block,
.has-error .control-label,
.has-error .radio,
.has-error .checkbox,
.has-error .radio-inline,
.has-error .checkbox-inline,
.has-error.radio label,
.has-error.checkbox label,
.has-error.radio-inline label,
.has-error.checkbox-inline label {
  color: #a94442;
}
.has-error .form-control {
  border-color: #a94442;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-error .form-control:focus {
  border-color: #843534;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
}
.has-error .input-group-addon {
  color: #a94442;
  border-color: #a94442;
  background-color: #f2dede;
}
.has-error .form-control-feedback {
  color: #a94442;
}
.has-feedback label ~ .form-control-feedback {
  top: 23px;
}
.has-feedback label.sr-only ~ .form-control-feedback {
  top: 0;
}
.help-block {
  display: block;
  margin-top: 5px;
  margin-bottom: 10px;
  color: #404040;
}
@media (min-width: 768px) {
  .form-inline .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .form-inline .form-control-static {
    display: inline-block;
  }
  .form-inline .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .form-inline .input-group .input-group-addon,
  .form-inline .input-group .input-group-btn,
  .form-inline .input-group .form-control {
    width: auto;
  }
  .form-inline .input-group > .form-control {
    width: 100%;
  }
  .form-inline .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio,
  .form-inline .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio label,
  .form-inline .checkbox label {
    padding-left: 0;
  }
  .form-inline .radio input[type="radio"],
  .form-inline .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .form-inline .has-feedback .form-control-feedback {
    top: 0;
  }
}
.form-horizontal .radio,
.form-horizontal .checkbox,
.form-horizontal .radio-inline,
.form-horizontal .checkbox-inline {
  margin-top: 0;
  margin-bottom: 0;
  padding-top: 7px;
}
.form-horizontal .radio,
.form-horizontal .checkbox {
  min-height: 25px;
}
.form-horizontal .form-group {
  margin-left: 0px;
  margin-right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .control-label {
    text-align: right;
    margin-bottom: 0;
    padding-top: 7px;
  }
}
.form-horizontal .has-feedback .form-control-feedback {
  right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .form-group-lg .control-label {
    padding-top: 11px;
    font-size: 17px;
  }
}
@media (min-width: 768px) {
  .form-horizontal .form-group-sm .control-label {
    padding-top: 6px;
    font-size: 12px;
  }
}
.btn {
  display: inline-block;
  margin-bottom: 0;
  font-weight: normal;
  text-align: center;
  vertical-align: middle;
  touch-action: manipulation;
  cursor: pointer;
  background-image: none;
  border: 1px solid transparent;
  white-space: nowrap;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  border-radius: 2px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.btn:focus,
.btn:active:focus,
.btn.active:focus,
.btn.focus,
.btn:active.focus,
.btn.active.focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
.btn:hover,
.btn:focus,
.btn.focus {
  color: #333;
  text-decoration: none;
}
.btn:active,
.btn.active {
  outline: 0;
  background-image: none;
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn.disabled,
.btn[disabled],
fieldset[disabled] .btn {
  cursor: not-allowed;
  opacity: 0.65;
  filter: alpha(opacity=65);
  -webkit-box-shadow: none;
  box-shadow: none;
}
a.btn.disabled,
fieldset[disabled] a.btn {
  pointer-events: none;
}
.btn-default {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.btn-default:focus,
.btn-default.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.btn-default:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active:hover,
.btn-default.active:hover,
.open > .dropdown-toggle.btn-default:hover,
.btn-default:active:focus,
.btn-default.active:focus,
.open > .dropdown-toggle.btn-default:focus,
.btn-default:active.focus,
.btn-default.active.focus,
.open > .dropdown-toggle.btn-default.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  background-image: none;
}
.btn-default.disabled:hover,
.btn-default[disabled]:hover,
fieldset[disabled] .btn-default:hover,
.btn-default.disabled:focus,
.btn-default[disabled]:focus,
fieldset[disabled] .btn-default:focus,
.btn-default.disabled.focus,
.btn-default[disabled].focus,
fieldset[disabled] .btn-default.focus {
  background-color: #fff;
  border-color: #ccc;
}
.btn-default .badge {
  color: #fff;
  background-color: #333;
}
.btn-primary {
  color: #fff;
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary:focus,
.btn-primary.focus {
  color: #fff;
  background-color: #286090;
  border-color: #122b40;
}
.btn-primary:hover {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active:hover,
.btn-primary.active:hover,
.open > .dropdown-toggle.btn-primary:hover,
.btn-primary:active:focus,
.btn-primary.active:focus,
.open > .dropdown-toggle.btn-primary:focus,
.btn-primary:active.focus,
.btn-primary.active.focus,
.open > .dropdown-toggle.btn-primary.focus {
  color: #fff;
  background-color: #204d74;
  border-color: #122b40;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  background-image: none;
}
.btn-primary.disabled:hover,
.btn-primary[disabled]:hover,
fieldset[disabled] .btn-primary:hover,
.btn-primary.disabled:focus,
.btn-primary[disabled]:focus,
fieldset[disabled] .btn-primary:focus,
.btn-primary.disabled.focus,
.btn-primary[disabled].focus,
fieldset[disabled] .btn-primary.focus {
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary .badge {
  color: #337ab7;
  background-color: #fff;
}
.btn-success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success:focus,
.btn-success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.btn-success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active:hover,
.btn-success.active:hover,
.open > .dropdown-toggle.btn-success:hover,
.btn-success:active:focus,
.btn-success.active:focus,
.open > .dropdown-toggle.btn-success:focus,
.btn-success:active.focus,
.btn-success.active.focus,
.open > .dropdown-toggle.btn-success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  background-image: none;
}
.btn-success.disabled:hover,
.btn-success[disabled]:hover,
fieldset[disabled] .btn-success:hover,
.btn-success.disabled:focus,
.btn-success[disabled]:focus,
fieldset[disabled] .btn-success:focus,
.btn-success.disabled.focus,
.btn-success[disabled].focus,
fieldset[disabled] .btn-success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.btn-info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info:focus,
.btn-info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.btn-info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active:hover,
.btn-info.active:hover,
.open > .dropdown-toggle.btn-info:hover,
.btn-info:active:focus,
.btn-info.active:focus,
.open > .dropdown-toggle.btn-info:focus,
.btn-info:active.focus,
.btn-info.active.focus,
.open > .dropdown-toggle.btn-info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  background-image: none;
}
.btn-info.disabled:hover,
.btn-info[disabled]:hover,
fieldset[disabled] .btn-info:hover,
.btn-info.disabled:focus,
.btn-info[disabled]:focus,
fieldset[disabled] .btn-info:focus,
.btn-info.disabled.focus,
.btn-info[disabled].focus,
fieldset[disabled] .btn-info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.btn-warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning:focus,
.btn-warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.btn-warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active:hover,
.btn-warning.active:hover,
.open > .dropdown-toggle.btn-warning:hover,
.btn-warning:active:focus,
.btn-warning.active:focus,
.open > .dropdown-toggle.btn-warning:focus,
.btn-warning:active.focus,
.btn-warning.active.focus,
.open > .dropdown-toggle.btn-warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  background-image: none;
}
.btn-warning.disabled:hover,
.btn-warning[disabled]:hover,
fieldset[disabled] .btn-warning:hover,
.btn-warning.disabled:focus,
.btn-warning[disabled]:focus,
fieldset[disabled] .btn-warning:focus,
.btn-warning.disabled.focus,
.btn-warning[disabled].focus,
fieldset[disabled] .btn-warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.btn-danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger:focus,
.btn-danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.btn-danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active:hover,
.btn-danger.active:hover,
.open > .dropdown-toggle.btn-danger:hover,
.btn-danger:active:focus,
.btn-danger.active:focus,
.open > .dropdown-toggle.btn-danger:focus,
.btn-danger:active.focus,
.btn-danger.active.focus,
.open > .dropdown-toggle.btn-danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  background-image: none;
}
.btn-danger.disabled:hover,
.btn-danger[disabled]:hover,
fieldset[disabled] .btn-danger:hover,
.btn-danger.disabled:focus,
.btn-danger[disabled]:focus,
fieldset[disabled] .btn-danger:focus,
.btn-danger.disabled.focus,
.btn-danger[disabled].focus,
fieldset[disabled] .btn-danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger .badge {
  color: #d9534f;
  background-color: #fff;
}
.btn-link {
  color: #337ab7;
  font-weight: normal;
  border-radius: 0;
}
.btn-link,
.btn-link:active,
.btn-link.active,
.btn-link[disabled],
fieldset[disabled] .btn-link {
  background-color: transparent;
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn-link,
.btn-link:hover,
.btn-link:focus,
.btn-link:active {
  border-color: transparent;
}
.btn-link:hover,
.btn-link:focus {
  color: #23527c;
  text-decoration: underline;
  background-color: transparent;
}
.btn-link[disabled]:hover,
fieldset[disabled] .btn-link:hover,
.btn-link[disabled]:focus,
fieldset[disabled] .btn-link:focus {
  color: #777777;
  text-decoration: none;
}
.btn-lg,
.btn-group-lg > .btn {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.btn-sm,
.btn-group-sm > .btn {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-xs,
.btn-group-xs > .btn {
  padding: 1px 5px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-block {
  display: block;
  width: 100%;
}
.btn-block + .btn-block {
  margin-top: 5px;
}
input[type="submit"].btn-block,
input[type="reset"].btn-block,
input[type="button"].btn-block {
  width: 100%;
}
.fade {
  opacity: 0;
  -webkit-transition: opacity 0.15s linear;
  -o-transition: opacity 0.15s linear;
  transition: opacity 0.15s linear;
}
.fade.in {
  opacity: 1;
}
.collapse {
  display: none;
}
.collapse.in {
  display: block;
}
tr.collapse.in {
  display: table-row;
}
tbody.collapse.in {
  display: table-row-group;
}
.collapsing {
  position: relative;
  height: 0;
  overflow: hidden;
  -webkit-transition-property: height, visibility;
  transition-property: height, visibility;
  -webkit-transition-duration: 0.35s;
  transition-duration: 0.35s;
  -webkit-transition-timing-function: ease;
  transition-timing-function: ease;
}
.caret {
  display: inline-block;
  width: 0;
  height: 0;
  margin-left: 2px;
  vertical-align: middle;
  border-top: 4px dashed;
  border-top: 4px solid \9;
  border-right: 4px solid transparent;
  border-left: 4px solid transparent;
}
.dropup,
.dropdown {
  position: relative;
}
.dropdown-toggle:focus {
  outline: 0;
}
.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 1000;
  display: none;
  float: left;
  min-width: 160px;
  padding: 5px 0;
  margin: 2px 0 0;
  list-style: none;
  font-size: 13px;
  text-align: left;
  background-color: #fff;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.15);
  border-radius: 2px;
  -webkit-box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  background-clip: padding-box;
}
.dropdown-menu.pull-right {
  right: 0;
  left: auto;
}
.dropdown-menu .divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.dropdown-menu > li > a {
  display: block;
  padding: 3px 20px;
  clear: both;
  font-weight: normal;
  line-height: 1.42857143;
  color: #333333;
  white-space: nowrap;
}
.dropdown-menu > li > a:hover,
.dropdown-menu > li > a:focus {
  text-decoration: none;
  color: #262626;
  background-color: #f5f5f5;
}
.dropdown-menu > .active > a,
.dropdown-menu > .active > a:hover,
.dropdown-menu > .active > a:focus {
  color: #fff;
  text-decoration: none;
  outline: 0;
  background-color: #337ab7;
}
.dropdown-menu > .disabled > a,
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  color: #777777;
}
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  text-decoration: none;
  background-color: transparent;
  background-image: none;
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  cursor: not-allowed;
}
.open > .dropdown-menu {
  display: block;
}
.open > a {
  outline: 0;
}
.dropdown-menu-right {
  left: auto;
  right: 0;
}
.dropdown-menu-left {
  left: 0;
  right: auto;
}
.dropdown-header {
  display: block;
  padding: 3px 20px;
  font-size: 12px;
  line-height: 1.42857143;
  color: #777777;
  white-space: nowrap;
}
.dropdown-backdrop {
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  top: 0;
  z-index: 990;
}
.pull-right > .dropdown-menu {
  right: 0;
  left: auto;
}
.dropup .caret,
.navbar-fixed-bottom .dropdown .caret {
  border-top: 0;
  border-bottom: 4px dashed;
  border-bottom: 4px solid \9;
  content: "";
}
.dropup .dropdown-menu,
.navbar-fixed-bottom .dropdown .dropdown-menu {
  top: auto;
  bottom: 100%;
  margin-bottom: 2px;
}
@media (min-width: 541px) {
  .navbar-right .dropdown-menu {
    left: auto;
    right: 0;
  }
  .navbar-right .dropdown-menu-left {
    left: 0;
    right: auto;
  }
}
.btn-group,
.btn-group-vertical {
  position: relative;
  display: inline-block;
  vertical-align: middle;
}
.btn-group > .btn,
.btn-group-vertical > .btn {
  position: relative;
  float: left;
}
.btn-group > .btn:hover,
.btn-group-vertical > .btn:hover,
.btn-group > .btn:focus,
.btn-group-vertical > .btn:focus,
.btn-group > .btn:active,
.btn-group-vertical > .btn:active,
.btn-group > .btn.active,
.btn-group-vertical > .btn.active {
  z-index: 2;
}
.btn-group .btn + .btn,
.btn-group .btn + .btn-group,
.btn-group .btn-group + .btn,
.btn-group .btn-group + .btn-group {
  margin-left: -1px;
}
.btn-toolbar {
  margin-left: -5px;
}
.btn-toolbar .btn,
.btn-toolbar .btn-group,
.btn-toolbar .input-group {
  float: left;
}
.btn-toolbar > .btn,
.btn-toolbar > .btn-group,
.btn-toolbar > .input-group {
  margin-left: 5px;
}
.btn-group > .btn:not(:first-child):not(:last-child):not(.dropdown-toggle) {
  border-radius: 0;
}
.btn-group > .btn:first-child {
  margin-left: 0;
}
.btn-group > .btn:first-child:not(:last-child):not(.dropdown-toggle) {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn:last-child:not(:first-child),
.btn-group > .dropdown-toggle:not(:first-child) {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group > .btn-group {
  float: left;
}
.btn-group > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group .dropdown-toggle:active,
.btn-group.open .dropdown-toggle {
  outline: 0;
}
.btn-group > .btn + .dropdown-toggle {
  padding-left: 8px;
  padding-right: 8px;
}
.btn-group > .btn-lg + .dropdown-toggle {
  padding-left: 12px;
  padding-right: 12px;
}
.btn-group.open .dropdown-toggle {
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn-group.open .dropdown-toggle.btn-link {
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn .caret {
  margin-left: 0;
}
.btn-lg .caret {
  border-width: 5px 5px 0;
  border-bottom-width: 0;
}
.dropup .btn-lg .caret {
  border-width: 0 5px 5px;
}
.btn-group-vertical > .btn,
.btn-group-vertical > .btn-group,
.btn-group-vertical > .btn-group > .btn {
  display: block;
  float: none;
  width: 100%;
  max-width: 100%;
}
.btn-group-vertical > .btn-group > .btn {
  float: none;
}
.btn-group-vertical > .btn + .btn,
.btn-group-vertical > .btn + .btn-group,
.btn-group-vertical > .btn-group + .btn,
.btn-group-vertical > .btn-group + .btn-group {
  margin-top: -1px;
  margin-left: 0;
}
.btn-group-vertical > .btn:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.btn-group-vertical > .btn:first-child:not(:last-child) {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn:last-child:not(:first-child) {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
.btn-group-vertical > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.btn-group-justified {
  display: table;
  width: 100%;
  table-layout: fixed;
  border-collapse: separate;
}
.btn-group-justified > .btn,
.btn-group-justified > .btn-group {
  float: none;
  display: table-cell;
  width: 1%;
}
.btn-group-justified > .btn-group .btn {
  width: 100%;
}
.btn-group-justified > .btn-group .dropdown-menu {
  left: auto;
}
[data-toggle="buttons"] > .btn input[type="radio"],
[data-toggle="buttons"] > .btn-group > .btn input[type="radio"],
[data-toggle="buttons"] > .btn input[type="checkbox"],
[data-toggle="buttons"] > .btn-group > .btn input[type="checkbox"] {
  position: absolute;
  clip: rect(0, 0, 0, 0);
  pointer-events: none;
}
.input-group {
  position: relative;
  display: table;
  border-collapse: separate;
}
.input-group[class*="col-"] {
  float: none;
  padding-left: 0;
  padding-right: 0;
}
.input-group .form-control {
  position: relative;
  z-index: 2;
  float: left;
  width: 100%;
  margin-bottom: 0;
}
.input-group .form-control:focus {
  z-index: 3;
}
.input-group-lg > .form-control,
.input-group-lg > .input-group-addon,
.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-group-lg > .form-control,
select.input-group-lg > .input-group-addon,
select.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  line-height: 45px;
}
textarea.input-group-lg > .form-control,
textarea.input-group-lg > .input-group-addon,
textarea.input-group-lg > .input-group-btn > .btn,
select[multiple].input-group-lg > .form-control,
select[multiple].input-group-lg > .input-group-addon,
select[multiple].input-group-lg > .input-group-btn > .btn {
  height: auto;
}
.input-group-sm > .form-control,
.input-group-sm > .input-group-addon,
.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-group-sm > .form-control,
select.input-group-sm > .input-group-addon,
select.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  line-height: 30px;
}
textarea.input-group-sm > .form-control,
textarea.input-group-sm > .input-group-addon,
textarea.input-group-sm > .input-group-btn > .btn,
select[multiple].input-group-sm > .form-control,
select[multiple].input-group-sm > .input-group-addon,
select[multiple].input-group-sm > .input-group-btn > .btn {
  height: auto;
}
.input-group-addon,
.input-group-btn,
.input-group .form-control {
  display: table-cell;
}
.input-group-addon:not(:first-child):not(:last-child),
.input-group-btn:not(:first-child):not(:last-child),
.input-group .form-control:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.input-group-addon,
.input-group-btn {
  width: 1%;
  white-space: nowrap;
  vertical-align: middle;
}
.input-group-addon {
  padding: 6px 12px;
  font-size: 13px;
  font-weight: normal;
  line-height: 1;
  color: #555555;
  text-align: center;
  background-color: #eeeeee;
  border: 1px solid #ccc;
  border-radius: 2px;
}
.input-group-addon.input-sm {
  padding: 5px 10px;
  font-size: 12px;
  border-radius: 1px;
}
.input-group-addon.input-lg {
  padding: 10px 16px;
  font-size: 17px;
  border-radius: 3px;
}
.input-group-addon input[type="radio"],
.input-group-addon input[type="checkbox"] {
  margin-top: 0;
}
.input-group .form-control:first-child,
.input-group-addon:first-child,
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group > .btn,
.input-group-btn:first-child > .dropdown-toggle,
.input-group-btn:last-child > .btn:not(:last-child):not(.dropdown-toggle),
.input-group-btn:last-child > .btn-group:not(:last-child) > .btn {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.input-group-addon:first-child {
  border-right: 0;
}
.input-group .form-control:last-child,
.input-group-addon:last-child,
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group > .btn,
.input-group-btn:last-child > .dropdown-toggle,
.input-group-btn:first-child > .btn:not(:first-child),
.input-group-btn:first-child > .btn-group:not(:first-child) > .btn {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.input-group-addon:last-child {
  border-left: 0;
}
.input-group-btn {
  position: relative;
  font-size: 0;
  white-space: nowrap;
}
.input-group-btn > .btn {
  position: relative;
}
.input-group-btn > .btn + .btn {
  margin-left: -1px;
}
.input-group-btn > .btn:hover,
.input-group-btn > .btn:focus,
.input-group-btn > .btn:active {
  z-index: 2;
}
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group {
  margin-right: -1px;
}
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group {
  z-index: 2;
  margin-left: -1px;
}
.nav {
  margin-bottom: 0;
  padding-left: 0;
  list-style: none;
}
.nav > li {
  position: relative;
  display: block;
}
.nav > li > a {
  position: relative;
  display: block;
  padding: 10px 15px;
}
.nav > li > a:hover,
.nav > li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.nav > li.disabled > a {
  color: #777777;
}
.nav > li.disabled > a:hover,
.nav > li.disabled > a:focus {
  color: #777777;
  text-decoration: none;
  background-color: transparent;
  cursor: not-allowed;
}
.nav .open > a,
.nav .open > a:hover,
.nav .open > a:focus {
  background-color: #eeeeee;
  border-color: #337ab7;
}
.nav .nav-divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.nav > li > a > img {
  max-width: none;
}
.nav-tabs {
  border-bottom: 1px solid #ddd;
}
.nav-tabs > li {
  float: left;
  margin-bottom: -1px;
}
.nav-tabs > li > a {
  margin-right: 2px;
  line-height: 1.42857143;
  border: 1px solid transparent;
  border-radius: 2px 2px 0 0;
}
.nav-tabs > li > a:hover {
  border-color: #eeeeee #eeeeee #ddd;
}
.nav-tabs > li.active > a,
.nav-tabs > li.active > a:hover,
.nav-tabs > li.active > a:focus {
  color: #555555;
  background-color: #fff;
  border: 1px solid #ddd;
  border-bottom-color: transparent;
  cursor: default;
}
.nav-tabs.nav-justified {
  width: 100%;
  border-bottom: 0;
}
.nav-tabs.nav-justified > li {
  float: none;
}
.nav-tabs.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-tabs.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-tabs.nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs.nav-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs.nav-justified > .active > a,
.nav-tabs.nav-justified > .active > a:hover,
.nav-tabs.nav-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs.nav-justified > .active > a,
  .nav-tabs.nav-justified > .active > a:hover,
  .nav-tabs.nav-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.nav-pills > li {
  float: left;
}
.nav-pills > li > a {
  border-radius: 2px;
}
.nav-pills > li + li {
  margin-left: 2px;
}
.nav-pills > li.active > a,
.nav-pills > li.active > a:hover,
.nav-pills > li.active > a:focus {
  color: #fff;
  background-color: #337ab7;
}
.nav-stacked > li {
  float: none;
}
.nav-stacked > li + li {
  margin-top: 2px;
  margin-left: 0;
}
.nav-justified {
  width: 100%;
}
.nav-justified > li {
  float: none;
}
.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs-justified {
  border-bottom: 0;
}
.nav-tabs-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs-justified > .active > a,
.nav-tabs-justified > .active > a:hover,
.nav-tabs-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs-justified > .active > a,
  .nav-tabs-justified > .active > a:hover,
  .nav-tabs-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.tab-content > .tab-pane {
  display: none;
}
.tab-content > .active {
  display: block;
}
.nav-tabs .dropdown-menu {
  margin-top: -1px;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar {
  position: relative;
  min-height: 30px;
  margin-bottom: 18px;
  border: 1px solid transparent;
}
@media (min-width: 541px) {
  .navbar {
    border-radius: 2px;
  }
}
@media (min-width: 541px) {
  .navbar-header {
    float: left;
  }
}
.navbar-collapse {
  overflow-x: visible;
  padding-right: 0px;
  padding-left: 0px;
  border-top: 1px solid transparent;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1);
  -webkit-overflow-scrolling: touch;
}
.navbar-collapse.in {
  overflow-y: auto;
}
@media (min-width: 541px) {
  .navbar-collapse {
    width: auto;
    border-top: 0;
    box-shadow: none;
  }
  .navbar-collapse.collapse {
    display: block !important;
    height: auto !important;
    padding-bottom: 0;
    overflow: visible !important;
  }
  .navbar-collapse.in {
    overflow-y: visible;
  }
  .navbar-fixed-top .navbar-collapse,
  .navbar-static-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    padding-left: 0;
    padding-right: 0;
  }
}
.navbar-fixed-top .navbar-collapse,
.navbar-fixed-bottom .navbar-collapse {
  max-height: 340px;
}
@media (max-device-width: 540px) and (orientation: landscape) {
  .navbar-fixed-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    max-height: 200px;
  }
}
.container > .navbar-header,
.container-fluid > .navbar-header,
.container > .navbar-collapse,
.container-fluid > .navbar-collapse {
  margin-right: 0px;
  margin-left: 0px;
}
@media (min-width: 541px) {
  .container > .navbar-header,
  .container-fluid > .navbar-header,
  .container > .navbar-collapse,
  .container-fluid > .navbar-collapse {
    margin-right: 0;
    margin-left: 0;
  }
}
.navbar-static-top {
  z-index: 1000;
  border-width: 0 0 1px;
}
@media (min-width: 541px) {
  .navbar-static-top {
    border-radius: 0;
  }
}
.navbar-fixed-top,
.navbar-fixed-bottom {
  position: fixed;
  right: 0;
  left: 0;
  z-index: 1030;
}
@media (min-width: 541px) {
  .navbar-fixed-top,
  .navbar-fixed-bottom {
    border-radius: 0;
  }
}
.navbar-fixed-top {
  top: 0;
  border-width: 0 0 1px;
}
.navbar-fixed-bottom {
  bottom: 0;
  margin-bottom: 0;
  border-width: 1px 0 0;
}
.navbar-brand {
  float: left;
  padding: 6px 0px;
  font-size: 17px;
  line-height: 18px;
  height: 30px;
}
.navbar-brand:hover,
.navbar-brand:focus {
  text-decoration: none;
}
.navbar-brand > img {
  display: block;
}
@media (min-width: 541px) {
  .navbar > .container .navbar-brand,
  .navbar > .container-fluid .navbar-brand {
    margin-left: 0px;
  }
}
.navbar-toggle {
  position: relative;
  float: right;
  margin-right: 0px;
  padding: 9px 10px;
  margin-top: -2px;
  margin-bottom: -2px;
  background-color: transparent;
  background-image: none;
  border: 1px solid transparent;
  border-radius: 2px;
}
.navbar-toggle:focus {
  outline: 0;
}
.navbar-toggle .icon-bar {
  display: block;
  width: 22px;
  height: 2px;
  border-radius: 1px;
}
.navbar-toggle .icon-bar + .icon-bar {
  margin-top: 4px;
}
@media (min-width: 541px) {
  .navbar-toggle {
    display: none;
  }
}
.navbar-nav {
  margin: 3px 0px;
}
.navbar-nav > li > a {
  padding-top: 10px;
  padding-bottom: 10px;
  line-height: 18px;
}
@media (max-width: 540px) {
  .navbar-nav .open .dropdown-menu {
    position: static;
    float: none;
    width: auto;
    margin-top: 0;
    background-color: transparent;
    border: 0;
    box-shadow: none;
  }
  .navbar-nav .open .dropdown-menu > li > a,
  .navbar-nav .open .dropdown-menu .dropdown-header {
    padding: 5px 15px 5px 25px;
  }
  .navbar-nav .open .dropdown-menu > li > a {
    line-height: 18px;
  }
  .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-nav .open .dropdown-menu > li > a:focus {
    background-image: none;
  }
}
@media (min-width: 541px) {
  .navbar-nav {
    float: left;
    margin: 0;
  }
  .navbar-nav > li {
    float: left;
  }
  .navbar-nav > li > a {
    padding-top: 6px;
    padding-bottom: 6px;
  }
}
.navbar-form {
  margin-left: 0px;
  margin-right: 0px;
  padding: 10px 0px;
  border-top: 1px solid transparent;
  border-bottom: 1px solid transparent;
  -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  margin-top: -1px;
  margin-bottom: -1px;
}
@media (min-width: 768px) {
  .navbar-form .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .navbar-form .form-control-static {
    display: inline-block;
  }
  .navbar-form .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .navbar-form .input-group .input-group-addon,
  .navbar-form .input-group .input-group-btn,
  .navbar-form .input-group .form-control {
    width: auto;
  }
  .navbar-form .input-group > .form-control {
    width: 100%;
  }
  .navbar-form .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio,
  .navbar-form .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio label,
  .navbar-form .checkbox label {
    padding-left: 0;
  }
  .navbar-form .radio input[type="radio"],
  .navbar-form .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .navbar-form .has-feedback .form-control-feedback {
    top: 0;
  }
}
@media (max-width: 540px) {
  .navbar-form .form-group {
    margin-bottom: 5px;
  }
  .navbar-form .form-group:last-child {
    margin-bottom: 0;
  }
}
@media (min-width: 541px) {
  .navbar-form {
    width: auto;
    border: 0;
    margin-left: 0;
    margin-right: 0;
    padding-top: 0;
    padding-bottom: 0;
    -webkit-box-shadow: none;
    box-shadow: none;
  }
}
.navbar-nav > li > .dropdown-menu {
  margin-top: 0;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar-fixed-bottom .navbar-nav > li > .dropdown-menu {
  margin-bottom: 0;
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.navbar-btn {
  margin-top: -1px;
  margin-bottom: -1px;
}
.navbar-btn.btn-sm {
  margin-top: 0px;
  margin-bottom: 0px;
}
.navbar-btn.btn-xs {
  margin-top: 4px;
  margin-bottom: 4px;
}
.navbar-text {
  margin-top: 6px;
  margin-bottom: 6px;
}
@media (min-width: 541px) {
  .navbar-text {
    float: left;
    margin-left: 0px;
    margin-right: 0px;
  }
}
@media (min-width: 541px) {
  .navbar-left {
    float: left !important;
    float: left;
  }
  .navbar-right {
    float: right !important;
    float: right;
    margin-right: 0px;
  }
  .navbar-right ~ .navbar-right {
    margin-right: 0;
  }
}
.navbar-default {
  background-color: #f8f8f8;
  border-color: #e7e7e7;
}
.navbar-default .navbar-brand {
  color: #777;
}
.navbar-default .navbar-brand:hover,
.navbar-default .navbar-brand:focus {
  color: #5e5e5e;
  background-color: transparent;
}
.navbar-default .navbar-text {
  color: #777;
}
.navbar-default .navbar-nav > li > a {
  color: #777;
}
.navbar-default .navbar-nav > li > a:hover,
.navbar-default .navbar-nav > li > a:focus {
  color: #333;
  background-color: transparent;
}
.navbar-default .navbar-nav > .active > a,
.navbar-default .navbar-nav > .active > a:hover,
.navbar-default .navbar-nav > .active > a:focus {
  color: #555;
  background-color: #e7e7e7;
}
.navbar-default .navbar-nav > .disabled > a,
.navbar-default .navbar-nav > .disabled > a:hover,
.navbar-default .navbar-nav > .disabled > a:focus {
  color: #ccc;
  background-color: transparent;
}
.navbar-default .navbar-toggle {
  border-color: #ddd;
}
.navbar-default .navbar-toggle:hover,
.navbar-default .navbar-toggle:focus {
  background-color: #ddd;
}
.navbar-default .navbar-toggle .icon-bar {
  background-color: #888;
}
.navbar-default .navbar-collapse,
.navbar-default .navbar-form {
  border-color: #e7e7e7;
}
.navbar-default .navbar-nav > .open > a,
.navbar-default .navbar-nav > .open > a:hover,
.navbar-default .navbar-nav > .open > a:focus {
  background-color: #e7e7e7;
  color: #555;
}
@media (max-width: 540px) {
  .navbar-default .navbar-nav .open .dropdown-menu > li > a {
    color: #777;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #333;
    background-color: transparent;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #555;
    background-color: #e7e7e7;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #ccc;
    background-color: transparent;
  }
}
.navbar-default .navbar-link {
  color: #777;
}
.navbar-default .navbar-link:hover {
  color: #333;
}
.navbar-default .btn-link {
  color: #777;
}
.navbar-default .btn-link:hover,
.navbar-default .btn-link:focus {
  color: #333;
}
.navbar-default .btn-link[disabled]:hover,
fieldset[disabled] .navbar-default .btn-link:hover,
.navbar-default .btn-link[disabled]:focus,
fieldset[disabled] .navbar-default .btn-link:focus {
  color: #ccc;
}
.navbar-inverse {
  background-color: #222;
  border-color: #080808;
}
.navbar-inverse .navbar-brand {
  color: #9d9d9d;
}
.navbar-inverse .navbar-brand:hover,
.navbar-inverse .navbar-brand:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-text {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a:hover,
.navbar-inverse .navbar-nav > li > a:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-nav > .active > a,
.navbar-inverse .navbar-nav > .active > a:hover,
.navbar-inverse .navbar-nav > .active > a:focus {
  color: #fff;
  background-color: #080808;
}
.navbar-inverse .navbar-nav > .disabled > a,
.navbar-inverse .navbar-nav > .disabled > a:hover,
.navbar-inverse .navbar-nav > .disabled > a:focus {
  color: #444;
  background-color: transparent;
}
.navbar-inverse .navbar-toggle {
  border-color: #333;
}
.navbar-inverse .navbar-toggle:hover,
.navbar-inverse .navbar-toggle:focus {
  background-color: #333;
}
.navbar-inverse .navbar-toggle .icon-bar {
  background-color: #fff;
}
.navbar-inverse .navbar-collapse,
.navbar-inverse .navbar-form {
  border-color: #101010;
}
.navbar-inverse .navbar-nav > .open > a,
.navbar-inverse .navbar-nav > .open > a:hover,
.navbar-inverse .navbar-nav > .open > a:focus {
  background-color: #080808;
  color: #fff;
}
@media (max-width: 540px) {
  .navbar-inverse .navbar-nav .open .dropdown-menu > .dropdown-header {
    border-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu .divider {
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a {
    color: #9d9d9d;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #fff;
    background-color: transparent;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #fff;
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #444;
    background-color: transparent;
  }
}
.navbar-inverse .navbar-link {
  color: #9d9d9d;
}
.navbar-inverse .navbar-link:hover {
  color: #fff;
}
.navbar-inverse .btn-link {
  color: #9d9d9d;
}
.navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link:focus {
  color: #fff;
}
.navbar-inverse .btn-link[disabled]:hover,
fieldset[disabled] .navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link[disabled]:focus,
fieldset[disabled] .navbar-inverse .btn-link:focus {
  color: #444;
}
.breadcrumb {
  padding: 8px 15px;
  margin-bottom: 18px;
  list-style: none;
  background-color: #f5f5f5;
  border-radius: 2px;
}
.breadcrumb > li {
  display: inline-block;
}
.breadcrumb > li + li:before {
  content: "/\00a0";
  padding: 0 5px;
  color: #5e5e5e;
}
.breadcrumb > .active {
  color: #777777;
}
.pagination {
  display: inline-block;
  padding-left: 0;
  margin: 18px 0;
  border-radius: 2px;
}
.pagination > li {
  display: inline;
}
.pagination > li > a,
.pagination > li > span {
  position: relative;
  float: left;
  padding: 6px 12px;
  line-height: 1.42857143;
  text-decoration: none;
  color: #337ab7;
  background-color: #fff;
  border: 1px solid #ddd;
  margin-left: -1px;
}
.pagination > li:first-child > a,
.pagination > li:first-child > span {
  margin-left: 0;
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.pagination > li:last-child > a,
.pagination > li:last-child > span {
  border-bottom-right-radius: 2px;
  border-top-right-radius: 2px;
}
.pagination > li > a:hover,
.pagination > li > span:hover,
.pagination > li > a:focus,
.pagination > li > span:focus {
  z-index: 2;
  color: #23527c;
  background-color: #eeeeee;
  border-color: #ddd;
}
.pagination > .active > a,
.pagination > .active > span,
.pagination > .active > a:hover,
.pagination > .active > span:hover,
.pagination > .active > a:focus,
.pagination > .active > span:focus {
  z-index: 3;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
  cursor: default;
}
.pagination > .disabled > span,
.pagination > .disabled > span:hover,
.pagination > .disabled > span:focus,
.pagination > .disabled > a,
.pagination > .disabled > a:hover,
.pagination > .disabled > a:focus {
  color: #777777;
  background-color: #fff;
  border-color: #ddd;
  cursor: not-allowed;
}
.pagination-lg > li > a,
.pagination-lg > li > span {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.pagination-lg > li:first-child > a,
.pagination-lg > li:first-child > span {
  border-bottom-left-radius: 3px;
  border-top-left-radius: 3px;
}
.pagination-lg > li:last-child > a,
.pagination-lg > li:last-child > span {
  border-bottom-right-radius: 3px;
  border-top-right-radius: 3px;
}
.pagination-sm > li > a,
.pagination-sm > li > span {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.pagination-sm > li:first-child > a,
.pagination-sm > li:first-child > span {
  border-bottom-left-radius: 1px;
  border-top-left-radius: 1px;
}
.pagination-sm > li:last-child > a,
.pagination-sm > li:last-child > span {
  border-bottom-right-radius: 1px;
  border-top-right-radius: 1px;
}
.pager {
  padding-left: 0;
  margin: 18px 0;
  list-style: none;
  text-align: center;
}
.pager li {
  display: inline;
}
.pager li > a,
.pager li > span {
  display: inline-block;
  padding: 5px 14px;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 15px;
}
.pager li > a:hover,
.pager li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.pager .next > a,
.pager .next > span {
  float: right;
}
.pager .previous > a,
.pager .previous > span {
  float: left;
}
.pager .disabled > a,
.pager .disabled > a:hover,
.pager .disabled > a:focus,
.pager .disabled > span {
  color: #777777;
  background-color: #fff;
  cursor: not-allowed;
}
.label {
  display: inline;
  padding: .2em .6em .3em;
  font-size: 75%;
  font-weight: bold;
  line-height: 1;
  color: #fff;
  text-align: center;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: .25em;
}
a.label:hover,
a.label:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.label:empty {
  display: none;
}
.btn .label {
  position: relative;
  top: -1px;
}
.label-default {
  background-color: #777777;
}
.label-default[href]:hover,
.label-default[href]:focus {
  background-color: #5e5e5e;
}
.label-primary {
  background-color: #337ab7;
}
.label-primary[href]:hover,
.label-primary[href]:focus {
  background-color: #286090;
}
.label-success {
  background-color: #5cb85c;
}
.label-success[href]:hover,
.label-success[href]:focus {
  background-color: #449d44;
}
.label-info {
  background-color: #5bc0de;
}
.label-info[href]:hover,
.label-info[href]:focus {
  background-color: #31b0d5;
}
.label-warning {
  background-color: #f0ad4e;
}
.label-warning[href]:hover,
.label-warning[href]:focus {
  background-color: #ec971f;
}
.label-danger {
  background-color: #d9534f;
}
.label-danger[href]:hover,
.label-danger[href]:focus {
  background-color: #c9302c;
}
.badge {
  display: inline-block;
  min-width: 10px;
  padding: 3px 7px;
  font-size: 12px;
  font-weight: bold;
  color: #fff;
  line-height: 1;
  vertical-align: middle;
  white-space: nowrap;
  text-align: center;
  background-color: #777777;
  border-radius: 10px;
}
.badge:empty {
  display: none;
}
.btn .badge {
  position: relative;
  top: -1px;
}
.btn-xs .badge,
.btn-group-xs > .btn .badge {
  top: 0;
  padding: 1px 5px;
}
a.badge:hover,
a.badge:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.list-group-item.active > .badge,
.nav-pills > .active > a > .badge {
  color: #337ab7;
  background-color: #fff;
}
.list-group-item > .badge {
  float: right;
}
.list-group-item > .badge + .badge {
  margin-right: 5px;
}
.nav-pills > li > a > .badge {
  margin-left: 3px;
}
.jumbotron {
  padding-top: 30px;
  padding-bottom: 30px;
  margin-bottom: 30px;
  color: inherit;
  background-color: #eeeeee;
}
.jumbotron h1,
.jumbotron .h1 {
  color: inherit;
}
.jumbotron p {
  margin-bottom: 15px;
  font-size: 20px;
  font-weight: 200;
}
.jumbotron > hr {
  border-top-color: #d5d5d5;
}
.container .jumbotron,
.container-fluid .jumbotron {
  border-radius: 3px;
  padding-left: 0px;
  padding-right: 0px;
}
.jumbotron .container {
  max-width: 100%;
}
@media screen and (min-width: 768px) {
  .jumbotron {
    padding-top: 48px;
    padding-bottom: 48px;
  }
  .container .jumbotron,
  .container-fluid .jumbotron {
    padding-left: 60px;
    padding-right: 60px;
  }
  .jumbotron h1,
  .jumbotron .h1 {
    font-size: 59px;
  }
}
.thumbnail {
  display: block;
  padding: 4px;
  margin-bottom: 18px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: border 0.2s ease-in-out;
  -o-transition: border 0.2s ease-in-out;
  transition: border 0.2s ease-in-out;
}
.thumbnail > img,
.thumbnail a > img {
  margin-left: auto;
  margin-right: auto;
}
a.thumbnail:hover,
a.thumbnail:focus,
a.thumbnail.active {
  border-color: #337ab7;
}
.thumbnail .caption {
  padding: 9px;
  color: #000;
}
.alert {
  padding: 15px;
  margin-bottom: 18px;
  border: 1px solid transparent;
  border-radius: 2px;
}
.alert h4 {
  margin-top: 0;
  color: inherit;
}
.alert .alert-link {
  font-weight: bold;
}
.alert > p,
.alert > ul {
  margin-bottom: 0;
}
.alert > p + p {
  margin-top: 5px;
}
.alert-dismissable,
.alert-dismissible {
  padding-right: 35px;
}
.alert-dismissable .close,
.alert-dismissible .close {
  position: relative;
  top: -2px;
  right: -21px;
  color: inherit;
}
.alert-success {
  background-color: #dff0d8;
  border-color: #d6e9c6;
  color: #3c763d;
}
.alert-success hr {
  border-top-color: #c9e2b3;
}
.alert-success .alert-link {
  color: #2b542c;
}
.alert-info {
  background-color: #d9edf7;
  border-color: #bce8f1;
  color: #31708f;
}
.alert-info hr {
  border-top-color: #a6e1ec;
}
.alert-info .alert-link {
  color: #245269;
}
.alert-warning {
  background-color: #fcf8e3;
  border-color: #faebcc;
  color: #8a6d3b;
}
.alert-warning hr {
  border-top-color: #f7e1b5;
}
.alert-warning .alert-link {
  color: #66512c;
}
.alert-danger {
  background-color: #f2dede;
  border-color: #ebccd1;
  color: #a94442;
}
.alert-danger hr {
  border-top-color: #e4b9c0;
}
.alert-danger .alert-link {
  color: #843534;
}
@-webkit-keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
@keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
.progress {
  overflow: hidden;
  height: 18px;
  margin-bottom: 18px;
  background-color: #f5f5f5;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
}
.progress-bar {
  float: left;
  width: 0%;
  height: 100%;
  font-size: 12px;
  line-height: 18px;
  color: #fff;
  text-align: center;
  background-color: #337ab7;
  -webkit-box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  -webkit-transition: width 0.6s ease;
  -o-transition: width 0.6s ease;
  transition: width 0.6s ease;
}
.progress-striped .progress-bar,
.progress-bar-striped {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-size: 40px 40px;
}
.progress.active .progress-bar,
.progress-bar.active {
  -webkit-animation: progress-bar-stripes 2s linear infinite;
  -o-animation: progress-bar-stripes 2s linear infinite;
  animation: progress-bar-stripes 2s linear infinite;
}
.progress-bar-success {
  background-color: #5cb85c;
}
.progress-striped .progress-bar-success {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-info {
  background-color: #5bc0de;
}
.progress-striped .progress-bar-info {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-warning {
  background-color: #f0ad4e;
}
.progress-striped .progress-bar-warning {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-danger {
  background-color: #d9534f;
}
.progress-striped .progress-bar-danger {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.media {
  margin-top: 15px;
}
.media:first-child {
  margin-top: 0;
}
.media,
.media-body {
  zoom: 1;
  overflow: hidden;
}
.media-body {
  width: 10000px;
}
.media-object {
  display: block;
}
.media-object.img-thumbnail {
  max-width: none;
}
.media-right,
.media > .pull-right {
  padding-left: 10px;
}
.media-left,
.media > .pull-left {
  padding-right: 10px;
}
.media-left,
.media-right,
.media-body {
  display: table-cell;
  vertical-align: top;
}
.media-middle {
  vertical-align: middle;
}
.media-bottom {
  vertical-align: bottom;
}
.media-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.media-list {
  padding-left: 0;
  list-style: none;
}
.list-group {
  margin-bottom: 20px;
  padding-left: 0;
}
.list-group-item {
  position: relative;
  display: block;
  padding: 10px 15px;
  margin-bottom: -1px;
  background-color: #fff;
  border: 1px solid #ddd;
}
.list-group-item:first-child {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
}
.list-group-item:last-child {
  margin-bottom: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
a.list-group-item,
button.list-group-item {
  color: #555;
}
a.list-group-item .list-group-item-heading,
button.list-group-item .list-group-item-heading {
  color: #333;
}
a.list-group-item:hover,
button.list-group-item:hover,
a.list-group-item:focus,
button.list-group-item:focus {
  text-decoration: none;
  color: #555;
  background-color: #f5f5f5;
}
button.list-group-item {
  width: 100%;
  text-align: left;
}
.list-group-item.disabled,
.list-group-item.disabled:hover,
.list-group-item.disabled:focus {
  background-color: #eeeeee;
  color: #777777;
  cursor: not-allowed;
}
.list-group-item.disabled .list-group-item-heading,
.list-group-item.disabled:hover .list-group-item-heading,
.list-group-item.disabled:focus .list-group-item-heading {
  color: inherit;
}
.list-group-item.disabled .list-group-item-text,
.list-group-item.disabled:hover .list-group-item-text,
.list-group-item.disabled:focus .list-group-item-text {
  color: #777777;
}
.list-group-item.active,
.list-group-item.active:hover,
.list-group-item.active:focus {
  z-index: 2;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.list-group-item.active .list-group-item-heading,
.list-group-item.active:hover .list-group-item-heading,
.list-group-item.active:focus .list-group-item-heading,
.list-group-item.active .list-group-item-heading > small,
.list-group-item.active:hover .list-group-item-heading > small,
.list-group-item.active:focus .list-group-item-heading > small,
.list-group-item.active .list-group-item-heading > .small,
.list-group-item.active:hover .list-group-item-heading > .small,
.list-group-item.active:focus .list-group-item-heading > .small {
  color: inherit;
}
.list-group-item.active .list-group-item-text,
.list-group-item.active:hover .list-group-item-text,
.list-group-item.active:focus .list-group-item-text {
  color: #c7ddef;
}
.list-group-item-success {
  color: #3c763d;
  background-color: #dff0d8;
}
a.list-group-item-success,
button.list-group-item-success {
  color: #3c763d;
}
a.list-group-item-success .list-group-item-heading,
button.list-group-item-success .list-group-item-heading {
  color: inherit;
}
a.list-group-item-success:hover,
button.list-group-item-success:hover,
a.list-group-item-success:focus,
button.list-group-item-success:focus {
  color: #3c763d;
  background-color: #d0e9c6;
}
a.list-group-item-success.active,
button.list-group-item-success.active,
a.list-group-item-success.active:hover,
button.list-group-item-success.active:hover,
a.list-group-item-success.active:focus,
button.list-group-item-success.active:focus {
  color: #fff;
  background-color: #3c763d;
  border-color: #3c763d;
}
.list-group-item-info {
  color: #31708f;
  background-color: #d9edf7;
}
a.list-group-item-info,
button.list-group-item-info {
  color: #31708f;
}
a.list-group-item-info .list-group-item-heading,
button.list-group-item-info .list-group-item-heading {
  color: inherit;
}
a.list-group-item-info:hover,
button.list-group-item-info:hover,
a.list-group-item-info:focus,
button.list-group-item-info:focus {
  color: #31708f;
  background-color: #c4e3f3;
}
a.list-group-item-info.active,
button.list-group-item-info.active,
a.list-group-item-info.active:hover,
button.list-group-item-info.active:hover,
a.list-group-item-info.active:focus,
button.list-group-item-info.active:focus {
  color: #fff;
  background-color: #31708f;
  border-color: #31708f;
}
.list-group-item-warning {
  color: #8a6d3b;
  background-color: #fcf8e3;
}
a.list-group-item-warning,
button.list-group-item-warning {
  color: #8a6d3b;
}
a.list-group-item-warning .list-group-item-heading,
button.list-group-item-warning .list-group-item-heading {
  color: inherit;
}
a.list-group-item-warning:hover,
button.list-group-item-warning:hover,
a.list-group-item-warning:focus,
button.list-group-item-warning:focus {
  color: #8a6d3b;
  background-color: #faf2cc;
}
a.list-group-item-warning.active,
button.list-group-item-warning.active,
a.list-group-item-warning.active:hover,
button.list-group-item-warning.active:hover,
a.list-group-item-warning.active:focus,
button.list-group-item-warning.active:focus {
  color: #fff;
  background-color: #8a6d3b;
  border-color: #8a6d3b;
}
.list-group-item-danger {
  color: #a94442;
  background-color: #f2dede;
}
a.list-group-item-danger,
button.list-group-item-danger {
  color: #a94442;
}
a.list-group-item-danger .list-group-item-heading,
button.list-group-item-danger .list-group-item-heading {
  color: inherit;
}
a.list-group-item-danger:hover,
button.list-group-item-danger:hover,
a.list-group-item-danger:focus,
button.list-group-item-danger:focus {
  color: #a94442;
  background-color: #ebcccc;
}
a.list-group-item-danger.active,
button.list-group-item-danger.active,
a.list-group-item-danger.active:hover,
button.list-group-item-danger.active:hover,
a.list-group-item-danger.active:focus,
button.list-group-item-danger.active:focus {
  color: #fff;
  background-color: #a94442;
  border-color: #a94442;
}
.list-group-item-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.list-group-item-text {
  margin-bottom: 0;
  line-height: 1.3;
}
.panel {
  margin-bottom: 18px;
  background-color: #fff;
  border: 1px solid transparent;
  border-radius: 2px;
  -webkit-box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
}
.panel-body {
  padding: 15px;
}
.panel-heading {
  padding: 10px 15px;
  border-bottom: 1px solid transparent;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel-heading > .dropdown .dropdown-toggle {
  color: inherit;
}
.panel-title {
  margin-top: 0;
  margin-bottom: 0;
  font-size: 15px;
  color: inherit;
}
.panel-title > a,
.panel-title > small,
.panel-title > .small,
.panel-title > small > a,
.panel-title > .small > a {
  color: inherit;
}
.panel-footer {
  padding: 10px 15px;
  background-color: #f5f5f5;
  border-top: 1px solid #ddd;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .list-group,
.panel > .panel-collapse > .list-group {
  margin-bottom: 0;
}
.panel > .list-group .list-group-item,
.panel > .panel-collapse > .list-group .list-group-item {
  border-width: 1px 0;
  border-radius: 0;
}
.panel > .list-group:first-child .list-group-item:first-child,
.panel > .panel-collapse > .list-group:first-child .list-group-item:first-child {
  border-top: 0;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .list-group:last-child .list-group-item:last-child,
.panel > .panel-collapse > .list-group:last-child .list-group-item:last-child {
  border-bottom: 0;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .panel-heading + .panel-collapse > .list-group .list-group-item:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.panel-heading + .list-group .list-group-item:first-child {
  border-top-width: 0;
}
.list-group + .panel-footer {
  border-top-width: 0;
}
.panel > .table,
.panel > .table-responsive > .table,
.panel > .panel-collapse > .table {
  margin-bottom: 0;
}
.panel > .table caption,
.panel > .table-responsive > .table caption,
.panel > .panel-collapse > .table caption {
  padding-left: 15px;
  padding-right: 15px;
}
.panel > .table:first-child,
.panel > .table-responsive:first-child > .table:first-child {
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child {
  border-top-left-radius: 1px;
  border-top-right-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:first-child {
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:last-child {
  border-top-right-radius: 1px;
}
.panel > .table:last-child,
.panel > .table-responsive:last-child > .table:last-child {
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child {
  border-bottom-left-radius: 1px;
  border-bottom-right-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:first-child {
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:last-child {
  border-bottom-right-radius: 1px;
}
.panel > .panel-body + .table,
.panel > .panel-body + .table-responsive,
.panel > .table + .panel-body,
.panel > .table-responsive + .panel-body {
  border-top: 1px solid #ddd;
}
.panel > .table > tbody:first-child > tr:first-child th,
.panel > .table > tbody:first-child > tr:first-child td {
  border-top: 0;
}
.panel > .table-bordered,
.panel > .table-responsive > .table-bordered {
  border: 0;
}
.panel > .table-bordered > thead > tr > th:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:first-child,
.panel > .table-bordered > tbody > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:first-child,
.panel > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-bordered > thead > tr > td:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:first-child,
.panel > .table-bordered > tbody > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:first-child,
.panel > .table-bordered > tfoot > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:first-child {
  border-left: 0;
}
.panel > .table-bordered > thead > tr > th:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:last-child,
.panel > .table-bordered > tbody > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:last-child,
.panel > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-bordered > thead > tr > td:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:last-child,
.panel > .table-bordered > tbody > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:last-child,
.panel > .table-bordered > tfoot > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:last-child {
  border-right: 0;
}
.panel > .table-bordered > thead > tr:first-child > td,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > td,
.panel > .table-bordered > tbody > tr:first-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > td,
.panel > .table-bordered > thead > tr:first-child > th,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > th,
.panel > .table-bordered > tbody > tr:first-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > th {
  border-bottom: 0;
}
.panel > .table-bordered > tbody > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > td,
.panel > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-bordered > tbody > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > th,
.panel > .table-bordered > tfoot > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > th {
  border-bottom: 0;
}
.panel > .table-responsive {
  border: 0;
  margin-bottom: 0;
}
.panel-group {
  margin-bottom: 18px;
}
.panel-group .panel {
  margin-bottom: 0;
  border-radius: 2px;
}
.panel-group .panel + .panel {
  margin-top: 5px;
}
.panel-group .panel-heading {
  border-bottom: 0;
}
.panel-group .panel-heading + .panel-collapse > .panel-body,
.panel-group .panel-heading + .panel-collapse > .list-group {
  border-top: 1px solid #ddd;
}
.panel-group .panel-footer {
  border-top: 0;
}
.panel-group .panel-footer + .panel-collapse .panel-body {
  border-bottom: 1px solid #ddd;
}
.panel-default {
  border-color: #ddd;
}
.panel-default > .panel-heading {
  color: #333333;
  background-color: #f5f5f5;
  border-color: #ddd;
}
.panel-default > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ddd;
}
.panel-default > .panel-heading .badge {
  color: #f5f5f5;
  background-color: #333333;
}
.panel-default > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ddd;
}
.panel-primary {
  border-color: #337ab7;
}
.panel-primary > .panel-heading {
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.panel-primary > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #337ab7;
}
.panel-primary > .panel-heading .badge {
  color: #337ab7;
  background-color: #fff;
}
.panel-primary > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #337ab7;
}
.panel-success {
  border-color: #d6e9c6;
}
.panel-success > .panel-heading {
  color: #3c763d;
  background-color: #dff0d8;
  border-color: #d6e9c6;
}
.panel-success > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #d6e9c6;
}
.panel-success > .panel-heading .badge {
  color: #dff0d8;
  background-color: #3c763d;
}
.panel-success > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #d6e9c6;
}
.panel-info {
  border-color: #bce8f1;
}
.panel-info > .panel-heading {
  color: #31708f;
  background-color: #d9edf7;
  border-color: #bce8f1;
}
.panel-info > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #bce8f1;
}
.panel-info > .panel-heading .badge {
  color: #d9edf7;
  background-color: #31708f;
}
.panel-info > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #bce8f1;
}
.panel-warning {
  border-color: #faebcc;
}
.panel-warning > .panel-heading {
  color: #8a6d3b;
  background-color: #fcf8e3;
  border-color: #faebcc;
}
.panel-warning > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #faebcc;
}
.panel-warning > .panel-heading .badge {
  color: #fcf8e3;
  background-color: #8a6d3b;
}
.panel-warning > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #faebcc;
}
.panel-danger {
  border-color: #ebccd1;
}
.panel-danger > .panel-heading {
  color: #a94442;
  background-color: #f2dede;
  border-color: #ebccd1;
}
.panel-danger > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ebccd1;
}
.panel-danger > .panel-heading .badge {
  color: #f2dede;
  background-color: #a94442;
}
.panel-danger > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ebccd1;
}
.embed-responsive {
  position: relative;
  display: block;
  height: 0;
  padding: 0;
  overflow: hidden;
}
.embed-responsive .embed-responsive-item,
.embed-responsive iframe,
.embed-responsive embed,
.embed-responsive object,
.embed-responsive video {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  height: 100%;
  width: 100%;
  border: 0;
}
.embed-responsive-16by9 {
  padding-bottom: 56.25%;
}
.embed-responsive-4by3 {
  padding-bottom: 75%;
}
.well {
  min-height: 20px;
  padding: 19px;
  margin-bottom: 20px;
  background-color: #f5f5f5;
  border: 1px solid #e3e3e3;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
}
.well blockquote {
  border-color: #ddd;
  border-color: rgba(0, 0, 0, 0.15);
}
.well-lg {
  padding: 24px;
  border-radius: 3px;
}
.well-sm {
  padding: 9px;
  border-radius: 1px;
}
.close {
  float: right;
  font-size: 19.5px;
  font-weight: bold;
  line-height: 1;
  color: #000;
  text-shadow: 0 1px 0 #fff;
  opacity: 0.2;
  filter: alpha(opacity=20);
}
.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
  opacity: 0.5;
  filter: alpha(opacity=50);
}
button.close {
  padding: 0;
  cursor: pointer;
  background: transparent;
  border: 0;
  -webkit-appearance: none;
}
.modal-open {
  overflow: hidden;
}
.modal {
  display: none;
  overflow: hidden;
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1050;
  -webkit-overflow-scrolling: touch;
  outline: 0;
}
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, -25%);
  -ms-transform: translate(0, -25%);
  -o-transform: translate(0, -25%);
  transform: translate(0, -25%);
  -webkit-transition: -webkit-transform 0.3s ease-out;
  -moz-transition: -moz-transform 0.3s ease-out;
  -o-transition: -o-transform 0.3s ease-out;
  transition: transform 0.3s ease-out;
}
.modal.in .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
.modal-open .modal {
  overflow-x: hidden;
  overflow-y: auto;
}
.modal-dialog {
  position: relative;
  width: auto;
  margin: 10px;
}
.modal-content {
  position: relative;
  background-color: #fff;
  border: 1px solid #999;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  background-clip: padding-box;
  outline: 0;
}
.modal-backdrop {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1040;
  background-color: #000;
}
.modal-backdrop.fade {
  opacity: 0;
  filter: alpha(opacity=0);
}
.modal-backdrop.in {
  opacity: 0.5;
  filter: alpha(opacity=50);
}
.modal-header {
  padding: 15px;
  border-bottom: 1px solid #e5e5e5;
}
.modal-header .close {
  margin-top: -2px;
}
.modal-title {
  margin: 0;
  line-height: 1.42857143;
}
.modal-body {
  position: relative;
  padding: 15px;
}
.modal-footer {
  padding: 15px;
  text-align: right;
  border-top: 1px solid #e5e5e5;
}
.modal-footer .btn + .btn {
  margin-left: 5px;
  margin-bottom: 0;
}
.modal-footer .btn-group .btn + .btn {
  margin-left: -1px;
}
.modal-footer .btn-block + .btn-block {
  margin-left: 0;
}
.modal-scrollbar-measure {
  position: absolute;
  top: -9999px;
  width: 50px;
  height: 50px;
  overflow: scroll;
}
@media (min-width: 768px) {
  .modal-dialog {
    width: 600px;
    margin: 30px auto;
  }
  .modal-content {
    -webkit-box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
  }
  .modal-sm {
    width: 300px;
  }
}
@media (min-width: 992px) {
  .modal-lg {
    width: 900px;
  }
}
.tooltip {
  position: absolute;
  z-index: 1070;
  display: block;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 12px;
  opacity: 0;
  filter: alpha(opacity=0);
}
.tooltip.in {
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.tooltip.top {
  margin-top: -3px;
  padding: 5px 0;
}
.tooltip.right {
  margin-left: 3px;
  padding: 0 5px;
}
.tooltip.bottom {
  margin-top: 3px;
  padding: 5px 0;
}
.tooltip.left {
  margin-left: -3px;
  padding: 0 5px;
}
.tooltip-inner {
  max-width: 200px;
  padding: 3px 8px;
  color: #fff;
  text-align: center;
  background-color: #000;
  border-radius: 2px;
}
.tooltip-arrow {
  position: absolute;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.tooltip.top .tooltip-arrow {
  bottom: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-left .tooltip-arrow {
  bottom: 0;
  right: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-right .tooltip-arrow {
  bottom: 0;
  left: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.right .tooltip-arrow {
  top: 50%;
  left: 0;
  margin-top: -5px;
  border-width: 5px 5px 5px 0;
  border-right-color: #000;
}
.tooltip.left .tooltip-arrow {
  top: 50%;
  right: 0;
  margin-top: -5px;
  border-width: 5px 0 5px 5px;
  border-left-color: #000;
}
.tooltip.bottom .tooltip-arrow {
  top: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-left .tooltip-arrow {
  top: 0;
  right: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-right .tooltip-arrow {
  top: 0;
  left: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.popover {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1060;
  display: none;
  max-width: 276px;
  padding: 1px;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 13px;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
}
.popover.top {
  margin-top: -10px;
}
.popover.right {
  margin-left: 10px;
}
.popover.bottom {
  margin-top: 10px;
}
.popover.left {
  margin-left: -10px;
}
.popover-title {
  margin: 0;
  padding: 8px 14px;
  font-size: 13px;
  background-color: #f7f7f7;
  border-bottom: 1px solid #ebebeb;
  border-radius: 2px 2px 0 0;
}
.popover-content {
  padding: 9px 14px;
}
.popover > .arrow,
.popover > .arrow:after {
  position: absolute;
  display: block;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.popover > .arrow {
  border-width: 11px;
}
.popover > .arrow:after {
  border-width: 10px;
  content: "";
}
.popover.top > .arrow {
  left: 50%;
  margin-left: -11px;
  border-bottom-width: 0;
  border-top-color: #999999;
  border-top-color: rgba(0, 0, 0, 0.25);
  bottom: -11px;
}
.popover.top > .arrow:after {
  content: " ";
  bottom: 1px;
  margin-left: -10px;
  border-bottom-width: 0;
  border-top-color: #fff;
}
.popover.right > .arrow {
  top: 50%;
  left: -11px;
  margin-top: -11px;
  border-left-width: 0;
  border-right-color: #999999;
  border-right-color: rgba(0, 0, 0, 0.25);
}
.popover.right > .arrow:after {
  content: " ";
  left: 1px;
  bottom: -10px;
  border-left-width: 0;
  border-right-color: #fff;
}
.popover.bottom > .arrow {
  left: 50%;
  margin-left: -11px;
  border-top-width: 0;
  border-bottom-color: #999999;
  border-bottom-color: rgba(0, 0, 0, 0.25);
  top: -11px;
}
.popover.bottom > .arrow:after {
  content: " ";
  top: 1px;
  margin-left: -10px;
  border-top-width: 0;
  border-bottom-color: #fff;
}
.popover.left > .arrow {
  top: 50%;
  right: -11px;
  margin-top: -11px;
  border-right-width: 0;
  border-left-color: #999999;
  border-left-color: rgba(0, 0, 0, 0.25);
}
.popover.left > .arrow:after {
  content: " ";
  right: 1px;
  border-right-width: 0;
  border-left-color: #fff;
  bottom: -10px;
}
.carousel {
  position: relative;
}
.carousel-inner {
  position: relative;
  overflow: hidden;
  width: 100%;
}
.carousel-inner > .item {
  display: none;
  position: relative;
  -webkit-transition: 0.6s ease-in-out left;
  -o-transition: 0.6s ease-in-out left;
  transition: 0.6s ease-in-out left;
}
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  line-height: 1;
}
@media all and (transform-3d), (-webkit-transform-3d) {
  .carousel-inner > .item {
    -webkit-transition: -webkit-transform 0.6s ease-in-out;
    -moz-transition: -moz-transform 0.6s ease-in-out;
    -o-transition: -o-transform 0.6s ease-in-out;
    transition: transform 0.6s ease-in-out;
    -webkit-backface-visibility: hidden;
    -moz-backface-visibility: hidden;
    backface-visibility: hidden;
    -webkit-perspective: 1000px;
    -moz-perspective: 1000px;
    perspective: 1000px;
  }
  .carousel-inner > .item.next,
  .carousel-inner > .item.active.right {
    -webkit-transform: translate3d(100%, 0, 0);
    transform: translate3d(100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.prev,
  .carousel-inner > .item.active.left {
    -webkit-transform: translate3d(-100%, 0, 0);
    transform: translate3d(-100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.next.left,
  .carousel-inner > .item.prev.right,
  .carousel-inner > .item.active {
    -webkit-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
    left: 0;
  }
}
.carousel-inner > .active,
.carousel-inner > .next,
.carousel-inner > .prev {
  display: block;
}
.carousel-inner > .active {
  left: 0;
}
.carousel-inner > .next,
.carousel-inner > .prev {
  position: absolute;
  top: 0;
  width: 100%;
}
.carousel-inner > .next {
  left: 100%;
}
.carousel-inner > .prev {
  left: -100%;
}
.carousel-inner > .next.left,
.carousel-inner > .prev.right {
  left: 0;
}
.carousel-inner > .active.left {
  left: -100%;
}
.carousel-inner > .active.right {
  left: 100%;
}
.carousel-control {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: 15%;
  opacity: 0.5;
  filter: alpha(opacity=50);
  font-size: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
  background-color: rgba(0, 0, 0, 0);
}
.carousel-control.left {
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#80000000', endColorstr='#00000000', GradientType=1);
}
.carousel-control.right {
  left: auto;
  right: 0;
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#00000000', endColorstr='#80000000', GradientType=1);
}
.carousel-control:hover,
.carousel-control:focus {
  outline: 0;
  color: #fff;
  text-decoration: none;
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.carousel-control .icon-prev,
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-left,
.carousel-control .glyphicon-chevron-right {
  position: absolute;
  top: 50%;
  margin-top: -10px;
  z-index: 5;
  display: inline-block;
}
.carousel-control .icon-prev,
.carousel-control .glyphicon-chevron-left {
  left: 50%;
  margin-left: -10px;
}
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-right {
  right: 50%;
  margin-right: -10px;
}
.carousel-control .icon-prev,
.carousel-control .icon-next {
  width: 20px;
  height: 20px;
  line-height: 1;
  font-family: serif;
}
.carousel-control .icon-prev:before {
  content: '\2039';
}
.carousel-control .icon-next:before {
  content: '\203a';
}
.carousel-indicators {
  position: absolute;
  bottom: 10px;
  left: 50%;
  z-index: 15;
  width: 60%;
  margin-left: -30%;
  padding-left: 0;
  list-style: none;
  text-align: center;
}
.carousel-indicators li {
  display: inline-block;
  width: 10px;
  height: 10px;
  margin: 1px;
  text-indent: -999px;
  border: 1px solid #fff;
  border-radius: 10px;
  cursor: pointer;
  background-color: #000 \9;
  background-color: rgba(0, 0, 0, 0);
}
.carousel-indicators .active {
  margin: 0;
  width: 12px;
  height: 12px;
  background-color: #fff;
}
.carousel-caption {
  position: absolute;
  left: 15%;
  right: 15%;
  bottom: 20px;
  z-index: 10;
  padding-top: 20px;
  padding-bottom: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
}
.carousel-caption .btn {
  text-shadow: none;
}
@media screen and (min-width: 768px) {
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-prev,
  .carousel-control .icon-next {
    width: 30px;
    height: 30px;
    margin-top: -10px;
    font-size: 30px;
  }
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .icon-prev {
    margin-left: -10px;
  }
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-next {
    margin-right: -10px;
  }
  .carousel-caption {
    left: 20%;
    right: 20%;
    padding-bottom: 30px;
  }
  .carousel-indicators {
    bottom: 20px;
  }
}
.clearfix:before,
.clearfix:after,
.dl-horizontal dd:before,
.dl-horizontal dd:after,
.container:before,
.container:after,
.container-fluid:before,
.container-fluid:after,
.row:before,
.row:after,
.form-horizontal .form-group:before,
.form-horizontal .form-group:after,
.btn-toolbar:before,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:before,
.btn-group-vertical > .btn-group:after,
.nav:before,
.nav:after,
.navbar:before,
.navbar:after,
.navbar-header:before,
.navbar-header:after,
.navbar-collapse:before,
.navbar-collapse:after,
.pager:before,
.pager:after,
.panel-body:before,
.panel-body:after,
.modal-header:before,
.modal-header:after,
.modal-footer:before,
.modal-footer:after,
.item_buttons:before,
.item_buttons:after {
  content: " ";
  display: table;
}
.clearfix:after,
.dl-horizontal dd:after,
.container:after,
.container-fluid:after,
.row:after,
.form-horizontal .form-group:after,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:after,
.nav:after,
.navbar:after,
.navbar-header:after,
.navbar-collapse:after,
.pager:after,
.panel-body:after,
.modal-header:after,
.modal-footer:after,
.item_buttons:after {
  clear: both;
}
.center-block {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.pull-right {
  float: right !important;
}
.pull-left {
  float: left !important;
}
.hide {
  display: none !important;
}
.show {
  display: block !important;
}
.invisible {
  visibility: hidden;
}
.text-hide {
  font: 0/0 a;
  color: transparent;
  text-shadow: none;
  background-color: transparent;
  border: 0;
}
.hidden {
  display: none !important;
}
.affix {
  position: fixed;
}
@-ms-viewport {
  width: device-width;
}
.visible-xs,
.visible-sm,
.visible-md,
.visible-lg {
  display: none !important;
}
.visible-xs-block,
.visible-xs-inline,
.visible-xs-inline-block,
.visible-sm-block,
.visible-sm-inline,
.visible-sm-inline-block,
.visible-md-block,
.visible-md-inline,
.visible-md-inline-block,
.visible-lg-block,
.visible-lg-inline,
.visible-lg-inline-block {
  display: none !important;
}
@media (max-width: 767px) {
  .visible-xs {
    display: block !important;
  }
  table.visible-xs {
    display: table !important;
  }
  tr.visible-xs {
    display: table-row !important;
  }
  th.visible-xs,
  td.visible-xs {
    display: table-cell !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-block {
    display: block !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline {
    display: inline !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm {
    display: block !important;
  }
  table.visible-sm {
    display: table !important;
  }
  tr.visible-sm {
    display: table-row !important;
  }
  th.visible-sm,
  td.visible-sm {
    display: table-cell !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-block {
    display: block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline {
    display: inline !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md {
    display: block !important;
  }
  table.visible-md {
    display: table !important;
  }
  tr.visible-md {
    display: table-row !important;
  }
  th.visible-md,
  td.visible-md {
    display: table-cell !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-block {
    display: block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline {
    display: inline !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg {
    display: block !important;
  }
  table.visible-lg {
    display: table !important;
  }
  tr.visible-lg {
    display: table-row !important;
  }
  th.visible-lg,
  td.visible-lg {
    display: table-cell !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-block {
    display: block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline {
    display: inline !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline-block {
    display: inline-block !important;
  }
}
@media (max-width: 767px) {
  .hidden-xs {
    display: none !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .hidden-sm {
    display: none !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .hidden-md {
    display: none !important;
  }
}
@media (min-width: 1200px) {
  .hidden-lg {
    display: none !important;
  }
}
.visible-print {
  display: none !important;
}
@media print {
  .visible-print {
    display: block !important;
  }
  table.visible-print {
    display: table !important;
  }
  tr.visible-print {
    display: table-row !important;
  }
  th.visible-print,
  td.visible-print {
    display: table-cell !important;
  }
}
.visible-print-block {
  display: none !important;
}
@media print {
  .visible-print-block {
    display: block !important;
  }
}
.visible-print-inline {
  display: none !important;
}
@media print {
  .visible-print-inline {
    display: inline !important;
  }
}
.visible-print-inline-block {
  display: none !important;
}
@media print {
  .visible-print-inline-block {
    display: inline-block !important;
  }
}
@media print {
  .hidden-print {
    display: none !important;
  }
}
/*!
*
* Font Awesome
*
*/
/*!
 *  Font Awesome 4.2.0 by @davegandy - http://fontawesome.io - @fontawesome
 *  License - http://fontawesome.io/license (Font: SIL OFL 1.1, CSS: MIT License)
 */
/* FONT PATH
 * -------------------------- */
@font-face {
  font-family: 'FontAwesome';
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?v=4.2.0');
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?#iefix&v=4.2.0') format('embedded-opentype'), url('../components/font-awesome/fonts/fontawesome-webfont.woff?v=4.2.0') format('woff'), url('../components/font-awesome/fonts/fontawesome-webfont.ttf?v=4.2.0') format('truetype'), url('../components/font-awesome/fonts/fontawesome-webfont.svg?v=4.2.0#fontawesomeregular') format('svg');
  font-weight: normal;
  font-style: normal;
}
.fa {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
/* makes the font 33% larger relative to the icon container */
.fa-lg {
  font-size: 1.33333333em;
  line-height: 0.75em;
  vertical-align: -15%;
}
.fa-2x {
  font-size: 2em;
}
.fa-3x {
  font-size: 3em;
}
.fa-4x {
  font-size: 4em;
}
.fa-5x {
  font-size: 5em;
}
.fa-fw {
  width: 1.28571429em;
  text-align: center;
}
.fa-ul {
  padding-left: 0;
  margin-left: 2.14285714em;
  list-style-type: none;
}
.fa-ul > li {
  position: relative;
}
.fa-li {
  position: absolute;
  left: -2.14285714em;
  width: 2.14285714em;
  top: 0.14285714em;
  text-align: center;
}
.fa-li.fa-lg {
  left: -1.85714286em;
}
.fa-border {
  padding: .2em .25em .15em;
  border: solid 0.08em #eee;
  border-radius: .1em;
}
.pull-right {
  float: right;
}
.pull-left {
  float: left;
}
.fa.pull-left {
  margin-right: .3em;
}
.fa.pull-right {
  margin-left: .3em;
}
.fa-spin {
  -webkit-animation: fa-spin 2s infinite linear;
  animation: fa-spin 2s infinite linear;
}
@-webkit-keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
@keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
.fa-rotate-90 {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=1);
  -webkit-transform: rotate(90deg);
  -ms-transform: rotate(90deg);
  transform: rotate(90deg);
}
.fa-rotate-180 {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=2);
  -webkit-transform: rotate(180deg);
  -ms-transform: rotate(180deg);
  transform: rotate(180deg);
}
.fa-rotate-270 {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=3);
  -webkit-transform: rotate(270deg);
  -ms-transform: rotate(270deg);
  transform: rotate(270deg);
}
.fa-flip-horizontal {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1);
  -webkit-transform: scale(-1, 1);
  -ms-transform: scale(-1, 1);
  transform: scale(-1, 1);
}
.fa-flip-vertical {
  filter: progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1);
  -webkit-transform: scale(1, -1);
  -ms-transform: scale(1, -1);
  transform: scale(1, -1);
}
:root .fa-rotate-90,
:root .fa-rotate-180,
:root .fa-rotate-270,
:root .fa-flip-horizontal,
:root .fa-flip-vertical {
  filter: none;
}
.fa-stack {
  position: relative;
  display: inline-block;
  width: 2em;
  height: 2em;
  line-height: 2em;
  vertical-align: middle;
}
.fa-stack-1x,
.fa-stack-2x {
  position: absolute;
  left: 0;
  width: 100%;
  text-align: center;
}
.fa-stack-1x {
  line-height: inherit;
}
.fa-stack-2x {
  font-size: 2em;
}
.fa-inverse {
  color: #fff;
}
/* Font Awesome uses the Unicode Private Use Area (PUA) to ensure screen
   readers do not read off random characters that represent icons */
.fa-glass:before {
  content: "\f000";
}
.fa-music:before {
  content: "\f001";
}
.fa-search:before {
  content: "\f002";
}
.fa-envelope-o:before {
  content: "\f003";
}
.fa-heart:before {
  content: "\f004";
}
.fa-star:before {
  content: "\f005";
}
.fa-star-o:before {
  content: "\f006";
}
.fa-user:before {
  content: "\f007";
}
.fa-film:before {
  content: "\f008";
}
.fa-th-large:before {
  content: "\f009";
}
.fa-th:before {
  content: "\f00a";
}
.fa-th-list:before {
  content: "\f00b";
}
.fa-check:before {
  content: "\f00c";
}
.fa-remove:before,
.fa-close:before,
.fa-times:before {
  content: "\f00d";
}
.fa-search-plus:before {
  content: "\f00e";
}
.fa-search-minus:before {
  content: "\f010";
}
.fa-power-off:before {
  content: "\f011";
}
.fa-signal:before {
  content: "\f012";
}
.fa-gear:before,
.fa-cog:before {
  content: "\f013";
}
.fa-trash-o:before {
  content: "\f014";
}
.fa-home:before {
  content: "\f015";
}
.fa-file-o:before {
  content: "\f016";
}
.fa-clock-o:before {
  content: "\f017";
}
.fa-road:before {
  content: "\f018";
}
.fa-download:before {
  content: "\f019";
}
.fa-arrow-circle-o-down:before {
  content: "\f01a";
}
.fa-arrow-circle-o-up:before {
  content: "\f01b";
}
.fa-inbox:before {
  content: "\f01c";
}
.fa-play-circle-o:before {
  content: "\f01d";
}
.fa-rotate-right:before,
.fa-repeat:before {
  content: "\f01e";
}
.fa-refresh:before {
  content: "\f021";
}
.fa-list-alt:before {
  content: "\f022";
}
.fa-lock:before {
  content: "\f023";
}
.fa-flag:before {
  content: "\f024";
}
.fa-headphones:before {
  content: "\f025";
}
.fa-volume-off:before {
  content: "\f026";
}
.fa-volume-down:before {
  content: "\f027";
}
.fa-volume-up:before {
  content: "\f028";
}
.fa-qrcode:before {
  content: "\f029";
}
.fa-barcode:before {
  content: "\f02a";
}
.fa-tag:before {
  content: "\f02b";
}
.fa-tags:before {
  content: "\f02c";
}
.fa-book:before {
  content: "\f02d";
}
.fa-bookmark:before {
  content: "\f02e";
}
.fa-print:before {
  content: "\f02f";
}
.fa-camera:before {
  content: "\f030";
}
.fa-font:before {
  content: "\f031";
}
.fa-bold:before {
  content: "\f032";
}
.fa-italic:before {
  content: "\f033";
}
.fa-text-height:before {
  content: "\f034";
}
.fa-text-width:before {
  content: "\f035";
}
.fa-align-left:before {
  content: "\f036";
}
.fa-align-center:before {
  content: "\f037";
}
.fa-align-right:before {
  content: "\f038";
}
.fa-align-justify:before {
  content: "\f039";
}
.fa-list:before {
  content: "\f03a";
}
.fa-dedent:before,
.fa-outdent:before {
  content: "\f03b";
}
.fa-indent:before {
  content: "\f03c";
}
.fa-video-camera:before {
  content: "\f03d";
}
.fa-photo:before,
.fa-image:before,
.fa-picture-o:before {
  content: "\f03e";
}
.fa-pencil:before {
  content: "\f040";
}
.fa-map-marker:before {
  content: "\f041";
}
.fa-adjust:before {
  content: "\f042";
}
.fa-tint:before {
  content: "\f043";
}
.fa-edit:before,
.fa-pencil-square-o:before {
  content: "\f044";
}
.fa-share-square-o:before {
  content: "\f045";
}
.fa-check-square-o:before {
  content: "\f046";
}
.fa-arrows:before {
  content: "\f047";
}
.fa-step-backward:before {
  content: "\f048";
}
.fa-fast-backward:before {
  content: "\f049";
}
.fa-backward:before {
  content: "\f04a";
}
.fa-play:before {
  content: "\f04b";
}
.fa-pause:before {
  content: "\f04c";
}
.fa-stop:before {
  content: "\f04d";
}
.fa-forward:before {
  content: "\f04e";
}
.fa-fast-forward:before {
  content: "\f050";
}
.fa-step-forward:before {
  content: "\f051";
}
.fa-eject:before {
  content: "\f052";
}
.fa-chevron-left:before {
  content: "\f053";
}
.fa-chevron-right:before {
  content: "\f054";
}
.fa-plus-circle:before {
  content: "\f055";
}
.fa-minus-circle:before {
  content: "\f056";
}
.fa-times-circle:before {
  content: "\f057";
}
.fa-check-circle:before {
  content: "\f058";
}
.fa-question-circle:before {
  content: "\f059";
}
.fa-info-circle:before {
  content: "\f05a";
}
.fa-crosshairs:before {
  content: "\f05b";
}
.fa-times-circle-o:before {
  content: "\f05c";
}
.fa-check-circle-o:before {
  content: "\f05d";
}
.fa-ban:before {
  content: "\f05e";
}
.fa-arrow-left:before {
  content: "\f060";
}
.fa-arrow-right:before {
  content: "\f061";
}
.fa-arrow-up:before {
  content: "\f062";
}
.fa-arrow-down:before {
  content: "\f063";
}
.fa-mail-forward:before,
.fa-share:before {
  content: "\f064";
}
.fa-expand:before {
  content: "\f065";
}
.fa-compress:before {
  content: "\f066";
}
.fa-plus:before {
  content: "\f067";
}
.fa-minus:before {
  content: "\f068";
}
.fa-asterisk:before {
  content: "\f069";
}
.fa-exclamation-circle:before {
  content: "\f06a";
}
.fa-gift:before {
  content: "\f06b";
}
.fa-leaf:before {
  content: "\f06c";
}
.fa-fire:before {
  content: "\f06d";
}
.fa-eye:before {
  content: "\f06e";
}
.fa-eye-slash:before {
  content: "\f070";
}
.fa-warning:before,
.fa-exclamation-triangle:before {
  content: "\f071";
}
.fa-plane:before {
  content: "\f072";
}
.fa-calendar:before {
  content: "\f073";
}
.fa-random:before {
  content: "\f074";
}
.fa-comment:before {
  content: "\f075";
}
.fa-magnet:before {
  content: "\f076";
}
.fa-chevron-up:before {
  content: "\f077";
}
.fa-chevron-down:before {
  content: "\f078";
}
.fa-retweet:before {
  content: "\f079";
}
.fa-shopping-cart:before {
  content: "\f07a";
}
.fa-folder:before {
  content: "\f07b";
}
.fa-folder-open:before {
  content: "\f07c";
}
.fa-arrows-v:before {
  content: "\f07d";
}
.fa-arrows-h:before {
  content: "\f07e";
}
.fa-bar-chart-o:before,
.fa-bar-chart:before {
  content: "\f080";
}
.fa-twitter-square:before {
  content: "\f081";
}
.fa-facebook-square:before {
  content: "\f082";
}
.fa-camera-retro:before {
  content: "\f083";
}
.fa-key:before {
  content: "\f084";
}
.fa-gears:before,
.fa-cogs:before {
  content: "\f085";
}
.fa-comments:before {
  content: "\f086";
}
.fa-thumbs-o-up:before {
  content: "\f087";
}
.fa-thumbs-o-down:before {
  content: "\f088";
}
.fa-star-half:before {
  content: "\f089";
}
.fa-heart-o:before {
  content: "\f08a";
}
.fa-sign-out:before {
  content: "\f08b";
}
.fa-linkedin-square:before {
  content: "\f08c";
}
.fa-thumb-tack:before {
  content: "\f08d";
}
.fa-external-link:before {
  content: "\f08e";
}
.fa-sign-in:before {
  content: "\f090";
}
.fa-trophy:before {
  content: "\f091";
}
.fa-github-square:before {
  content: "\f092";
}
.fa-upload:before {
  content: "\f093";
}
.fa-lemon-o:before {
  content: "\f094";
}
.fa-phone:before {
  content: "\f095";
}
.fa-square-o:before {
  content: "\f096";
}
.fa-bookmark-o:before {
  content: "\f097";
}
.fa-phone-square:before {
  content: "\f098";
}
.fa-twitter:before {
  content: "\f099";
}
.fa-facebook:before {
  content: "\f09a";
}
.fa-github:before {
  content: "\f09b";
}
.fa-unlock:before {
  content: "\f09c";
}
.fa-credit-card:before {
  content: "\f09d";
}
.fa-rss:before {
  content: "\f09e";
}
.fa-hdd-o:before {
  content: "\f0a0";
}
.fa-bullhorn:before {
  content: "\f0a1";
}
.fa-bell:before {
  content: "\f0f3";
}
.fa-certificate:before {
  content: "\f0a3";
}
.fa-hand-o-right:before {
  content: "\f0a4";
}
.fa-hand-o-left:before {
  content: "\f0a5";
}
.fa-hand-o-up:before {
  content: "\f0a6";
}
.fa-hand-o-down:before {
  content: "\f0a7";
}
.fa-arrow-circle-left:before {
  content: "\f0a8";
}
.fa-arrow-circle-right:before {
  content: "\f0a9";
}
.fa-arrow-circle-up:before {
  content: "\f0aa";
}
.fa-arrow-circle-down:before {
  content: "\f0ab";
}
.fa-globe:before {
  content: "\f0ac";
}
.fa-wrench:before {
  content: "\f0ad";
}
.fa-tasks:before {
  content: "\f0ae";
}
.fa-filter:before {
  content: "\f0b0";
}
.fa-briefcase:before {
  content: "\f0b1";
}
.fa-arrows-alt:before {
  content: "\f0b2";
}
.fa-group:before,
.fa-users:before {
  content: "\f0c0";
}
.fa-chain:before,
.fa-link:before {
  content: "\f0c1";
}
.fa-cloud:before {
  content: "\f0c2";
}
.fa-flask:before {
  content: "\f0c3";
}
.fa-cut:before,
.fa-scissors:before {
  content: "\f0c4";
}
.fa-copy:before,
.fa-files-o:before {
  content: "\f0c5";
}
.fa-paperclip:before {
  content: "\f0c6";
}
.fa-save:before,
.fa-floppy-o:before {
  content: "\f0c7";
}
.fa-square:before {
  content: "\f0c8";
}
.fa-navicon:before,
.fa-reorder:before,
.fa-bars:before {
  content: "\f0c9";
}
.fa-list-ul:before {
  content: "\f0ca";
}
.fa-list-ol:before {
  content: "\f0cb";
}
.fa-strikethrough:before {
  content: "\f0cc";
}
.fa-underline:before {
  content: "\f0cd";
}
.fa-table:before {
  content: "\f0ce";
}
.fa-magic:before {
  content: "\f0d0";
}
.fa-truck:before {
  content: "\f0d1";
}
.fa-pinterest:before {
  content: "\f0d2";
}
.fa-pinterest-square:before {
  content: "\f0d3";
}
.fa-google-plus-square:before {
  content: "\f0d4";
}
.fa-google-plus:before {
  content: "\f0d5";
}
.fa-money:before {
  content: "\f0d6";
}
.fa-caret-down:before {
  content: "\f0d7";
}
.fa-caret-up:before {
  content: "\f0d8";
}
.fa-caret-left:before {
  content: "\f0d9";
}
.fa-caret-right:before {
  content: "\f0da";
}
.fa-columns:before {
  content: "\f0db";
}
.fa-unsorted:before,
.fa-sort:before {
  content: "\f0dc";
}
.fa-sort-down:before,
.fa-sort-desc:before {
  content: "\f0dd";
}
.fa-sort-up:before,
.fa-sort-asc:before {
  content: "\f0de";
}
.fa-envelope:before {
  content: "\f0e0";
}
.fa-linkedin:before {
  content: "\f0e1";
}
.fa-rotate-left:before,
.fa-undo:before {
  content: "\f0e2";
}
.fa-legal:before,
.fa-gavel:before {
  content: "\f0e3";
}
.fa-dashboard:before,
.fa-tachometer:before {
  content: "\f0e4";
}
.fa-comment-o:before {
  content: "\f0e5";
}
.fa-comments-o:before {
  content: "\f0e6";
}
.fa-flash:before,
.fa-bolt:before {
  content: "\f0e7";
}
.fa-sitemap:before {
  content: "\f0e8";
}
.fa-umbrella:before {
  content: "\f0e9";
}
.fa-paste:before,
.fa-clipboard:before {
  content: "\f0ea";
}
.fa-lightbulb-o:before {
  content: "\f0eb";
}
.fa-exchange:before {
  content: "\f0ec";
}
.fa-cloud-download:before {
  content: "\f0ed";
}
.fa-cloud-upload:before {
  content: "\f0ee";
}
.fa-user-md:before {
  content: "\f0f0";
}
.fa-stethoscope:before {
  content: "\f0f1";
}
.fa-suitcase:before {
  content: "\f0f2";
}
.fa-bell-o:before {
  content: "\f0a2";
}
.fa-coffee:before {
  content: "\f0f4";
}
.fa-cutlery:before {
  content: "\f0f5";
}
.fa-file-text-o:before {
  content: "\f0f6";
}
.fa-building-o:before {
  content: "\f0f7";
}
.fa-hospital-o:before {
  content: "\f0f8";
}
.fa-ambulance:before {
  content: "\f0f9";
}
.fa-medkit:before {
  content: "\f0fa";
}
.fa-fighter-jet:before {
  content: "\f0fb";
}
.fa-beer:before {
  content: "\f0fc";
}
.fa-h-square:before {
  content: "\f0fd";
}
.fa-plus-square:before {
  content: "\f0fe";
}
.fa-angle-double-left:before {
  content: "\f100";
}
.fa-angle-double-right:before {
  content: "\f101";
}
.fa-angle-double-up:before {
  content: "\f102";
}
.fa-angle-double-down:before {
  content: "\f103";
}
.fa-angle-left:before {
  content: "\f104";
}
.fa-angle-right:before {
  content: "\f105";
}
.fa-angle-up:before {
  content: "\f106";
}
.fa-angle-down:before {
  content: "\f107";
}
.fa-desktop:before {
  content: "\f108";
}
.fa-laptop:before {
  content: "\f109";
}
.fa-tablet:before {
  content: "\f10a";
}
.fa-mobile-phone:before,
.fa-mobile:before {
  content: "\f10b";
}
.fa-circle-o:before {
  content: "\f10c";
}
.fa-quote-left:before {
  content: "\f10d";
}
.fa-quote-right:before {
  content: "\f10e";
}
.fa-spinner:before {
  content: "\f110";
}
.fa-circle:before {
  content: "\f111";
}
.fa-mail-reply:before,
.fa-reply:before {
  content: "\f112";
}
.fa-github-alt:before {
  content: "\f113";
}
.fa-folder-o:before {
  content: "\f114";
}
.fa-folder-open-o:before {
  content: "\f115";
}
.fa-smile-o:before {
  content: "\f118";
}
.fa-frown-o:before {
  content: "\f119";
}
.fa-meh-o:before {
  content: "\f11a";
}
.fa-gamepad:before {
  content: "\f11b";
}
.fa-keyboard-o:before {
  content: "\f11c";
}
.fa-flag-o:before {
  content: "\f11d";
}
.fa-flag-checkered:before {
  content: "\f11e";
}
.fa-terminal:before {
  content: "\f120";
}
.fa-code:before {
  content: "\f121";
}
.fa-mail-reply-all:before,
.fa-reply-all:before {
  content: "\f122";
}
.fa-star-half-empty:before,
.fa-star-half-full:before,
.fa-star-half-o:before {
  content: "\f123";
}
.fa-location-arrow:before {
  content: "\f124";
}
.fa-crop:before {
  content: "\f125";
}
.fa-code-fork:before {
  content: "\f126";
}
.fa-unlink:before,
.fa-chain-broken:before {
  content: "\f127";
}
.fa-question:before {
  content: "\f128";
}
.fa-info:before {
  content: "\f129";
}
.fa-exclamation:before {
  content: "\f12a";
}
.fa-superscript:before {
  content: "\f12b";
}
.fa-subscript:before {
  content: "\f12c";
}
.fa-eraser:before {
  content: "\f12d";
}
.fa-puzzle-piece:before {
  content: "\f12e";
}
.fa-microphone:before {
  content: "\f130";
}
.fa-microphone-slash:before {
  content: "\f131";
}
.fa-shield:before {
  content: "\f132";
}
.fa-calendar-o:before {
  content: "\f133";
}
.fa-fire-extinguisher:before {
  content: "\f134";
}
.fa-rocket:before {
  content: "\f135";
}
.fa-maxcdn:before {
  content: "\f136";
}
.fa-chevron-circle-left:before {
  content: "\f137";
}
.fa-chevron-circle-right:before {
  content: "\f138";
}
.fa-chevron-circle-up:before {
  content: "\f139";
}
.fa-chevron-circle-down:before {
  content: "\f13a";
}
.fa-html5:before {
  content: "\f13b";
}
.fa-css3:before {
  content: "\f13c";
}
.fa-anchor:before {
  content: "\f13d";
}
.fa-unlock-alt:before {
  content: "\f13e";
}
.fa-bullseye:before {
  content: "\f140";
}
.fa-ellipsis-h:before {
  content: "\f141";
}
.fa-ellipsis-v:before {
  content: "\f142";
}
.fa-rss-square:before {
  content: "\f143";
}
.fa-play-circle:before {
  content: "\f144";
}
.fa-ticket:before {
  content: "\f145";
}
.fa-minus-square:before {
  content: "\f146";
}
.fa-minus-square-o:before {
  content: "\f147";
}
.fa-level-up:before {
  content: "\f148";
}
.fa-level-down:before {
  content: "\f149";
}
.fa-check-square:before {
  content: "\f14a";
}
.fa-pencil-square:before {
  content: "\f14b";
}
.fa-external-link-square:before {
  content: "\f14c";
}
.fa-share-square:before {
  content: "\f14d";
}
.fa-compass:before {
  content: "\f14e";
}
.fa-toggle-down:before,
.fa-caret-square-o-down:before {
  content: "\f150";
}
.fa-toggle-up:before,
.fa-caret-square-o-up:before {
  content: "\f151";
}
.fa-toggle-right:before,
.fa-caret-square-o-right:before {
  content: "\f152";
}
.fa-euro:before,
.fa-eur:before {
  content: "\f153";
}
.fa-gbp:before {
  content: "\f154";
}
.fa-dollar:before,
.fa-usd:before {
  content: "\f155";
}
.fa-rupee:before,
.fa-inr:before {
  content: "\f156";
}
.fa-cny:before,
.fa-rmb:before,
.fa-yen:before,
.fa-jpy:before {
  content: "\f157";
}
.fa-ruble:before,
.fa-rouble:before,
.fa-rub:before {
  content: "\f158";
}
.fa-won:before,
.fa-krw:before {
  content: "\f159";
}
.fa-bitcoin:before,
.fa-btc:before {
  content: "\f15a";
}
.fa-file:before {
  content: "\f15b";
}
.fa-file-text:before {
  content: "\f15c";
}
.fa-sort-alpha-asc:before {
  content: "\f15d";
}
.fa-sort-alpha-desc:before {
  content: "\f15e";
}
.fa-sort-amount-asc:before {
  content: "\f160";
}
.fa-sort-amount-desc:before {
  content: "\f161";
}
.fa-sort-numeric-asc:before {
  content: "\f162";
}
.fa-sort-numeric-desc:before {
  content: "\f163";
}
.fa-thumbs-up:before {
  content: "\f164";
}
.fa-thumbs-down:before {
  content: "\f165";
}
.fa-youtube-square:before {
  content: "\f166";
}
.fa-youtube:before {
  content: "\f167";
}
.fa-xing:before {
  content: "\f168";
}
.fa-xing-square:before {
  content: "\f169";
}
.fa-youtube-play:before {
  content: "\f16a";
}
.fa-dropbox:before {
  content: "\f16b";
}
.fa-stack-overflow:before {
  content: "\f16c";
}
.fa-instagram:before {
  content: "\f16d";
}
.fa-flickr:before {
  content: "\f16e";
}
.fa-adn:before {
  content: "\f170";
}
.fa-bitbucket:before {
  content: "\f171";
}
.fa-bitbucket-square:before {
  content: "\f172";
}
.fa-tumblr:before {
  content: "\f173";
}
.fa-tumblr-square:before {
  content: "\f174";
}
.fa-long-arrow-down:before {
  content: "\f175";
}
.fa-long-arrow-up:before {
  content: "\f176";
}
.fa-long-arrow-left:before {
  content: "\f177";
}
.fa-long-arrow-right:before {
  content: "\f178";
}
.fa-apple:before {
  content: "\f179";
}
.fa-windows:before {
  content: "\f17a";
}
.fa-android:before {
  content: "\f17b";
}
.fa-linux:before {
  content: "\f17c";
}
.fa-dribbble:before {
  content: "\f17d";
}
.fa-skype:before {
  content: "\f17e";
}
.fa-foursquare:before {
  content: "\f180";
}
.fa-trello:before {
  content: "\f181";
}
.fa-female:before {
  content: "\f182";
}
.fa-male:before {
  content: "\f183";
}
.fa-gittip:before {
  content: "\f184";
}
.fa-sun-o:before {
  content: "\f185";
}
.fa-moon-o:before {
  content: "\f186";
}
.fa-archive:before {
  content: "\f187";
}
.fa-bug:before {
  content: "\f188";
}
.fa-vk:before {
  content: "\f189";
}
.fa-weibo:before {
  content: "\f18a";
}
.fa-renren:before {
  content: "\f18b";
}
.fa-pagelines:before {
  content: "\f18c";
}
.fa-stack-exchange:before {
  content: "\f18d";
}
.fa-arrow-circle-o-right:before {
  content: "\f18e";
}
.fa-arrow-circle-o-left:before {
  content: "\f190";
}
.fa-toggle-left:before,
.fa-caret-square-o-left:before {
  content: "\f191";
}
.fa-dot-circle-o:before {
  content: "\f192";
}
.fa-wheelchair:before {
  content: "\f193";
}
.fa-vimeo-square:before {
  content: "\f194";
}
.fa-turkish-lira:before,
.fa-try:before {
  content: "\f195";
}
.fa-plus-square-o:before {
  content: "\f196";
}
.fa-space-shuttle:before {
  content: "\f197";
}
.fa-slack:before {
  content: "\f198";
}
.fa-envelope-square:before {
  content: "\f199";
}
.fa-wordpress:before {
  content: "\f19a";
}
.fa-openid:before {
  content: "\f19b";
}
.fa-institution:before,
.fa-bank:before,
.fa-university:before {
  content: "\f19c";
}
.fa-mortar-board:before,
.fa-graduation-cap:before {
  content: "\f19d";
}
.fa-yahoo:before {
  content: "\f19e";
}
.fa-google:before {
  content: "\f1a0";
}
.fa-reddit:before {
  content: "\f1a1";
}
.fa-reddit-square:before {
  content: "\f1a2";
}
.fa-stumbleupon-circle:before {
  content: "\f1a3";
}
.fa-stumbleupon:before {
  content: "\f1a4";
}
.fa-delicious:before {
  content: "\f1a5";
}
.fa-digg:before {
  content: "\f1a6";
}
.fa-pied-piper:before {
  content: "\f1a7";
}
.fa-pied-piper-alt:before {
  content: "\f1a8";
}
.fa-drupal:before {
  content: "\f1a9";
}
.fa-joomla:before {
  content: "\f1aa";
}
.fa-language:before {
  content: "\f1ab";
}
.fa-fax:before {
  content: "\f1ac";
}
.fa-building:before {
  content: "\f1ad";
}
.fa-child:before {
  content: "\f1ae";
}
.fa-paw:before {
  content: "\f1b0";
}
.fa-spoon:before {
  content: "\f1b1";
}
.fa-cube:before {
  content: "\f1b2";
}
.fa-cubes:before {
  content: "\f1b3";
}
.fa-behance:before {
  content: "\f1b4";
}
.fa-behance-square:before {
  content: "\f1b5";
}
.fa-steam:before {
  content: "\f1b6";
}
.fa-steam-square:before {
  content: "\f1b7";
}
.fa-recycle:before {
  content: "\f1b8";
}
.fa-automobile:before,
.fa-car:before {
  content: "\f1b9";
}
.fa-cab:before,
.fa-taxi:before {
  content: "\f1ba";
}
.fa-tree:before {
  content: "\f1bb";
}
.fa-spotify:before {
  content: "\f1bc";
}
.fa-deviantart:before {
  content: "\f1bd";
}
.fa-soundcloud:before {
  content: "\f1be";
}
.fa-database:before {
  content: "\f1c0";
}
.fa-file-pdf-o:before {
  content: "\f1c1";
}
.fa-file-word-o:before {
  content: "\f1c2";
}
.fa-file-excel-o:before {
  content: "\f1c3";
}
.fa-file-powerpoint-o:before {
  content: "\f1c4";
}
.fa-file-photo-o:before,
.fa-file-picture-o:before,
.fa-file-image-o:before {
  content: "\f1c5";
}
.fa-file-zip-o:before,
.fa-file-archive-o:before {
  content: "\f1c6";
}
.fa-file-sound-o:before,
.fa-file-audio-o:before {
  content: "\f1c7";
}
.fa-file-movie-o:before,
.fa-file-video-o:before {
  content: "\f1c8";
}
.fa-file-code-o:before {
  content: "\f1c9";
}
.fa-vine:before {
  content: "\f1ca";
}
.fa-codepen:before {
  content: "\f1cb";
}
.fa-jsfiddle:before {
  content: "\f1cc";
}
.fa-life-bouy:before,
.fa-life-buoy:before,
.fa-life-saver:before,
.fa-support:before,
.fa-life-ring:before {
  content: "\f1cd";
}
.fa-circle-o-notch:before {
  content: "\f1ce";
}
.fa-ra:before,
.fa-rebel:before {
  content: "\f1d0";
}
.fa-ge:before,
.fa-empire:before {
  content: "\f1d1";
}
.fa-git-square:before {
  content: "\f1d2";
}
.fa-git:before {
  content: "\f1d3";
}
.fa-hacker-news:before {
  content: "\f1d4";
}
.fa-tencent-weibo:before {
  content: "\f1d5";
}
.fa-qq:before {
  content: "\f1d6";
}
.fa-wechat:before,
.fa-weixin:before {
  content: "\f1d7";
}
.fa-send:before,
.fa-paper-plane:before {
  content: "\f1d8";
}
.fa-send-o:before,
.fa-paper-plane-o:before {
  content: "\f1d9";
}
.fa-history:before {
  content: "\f1da";
}
.fa-circle-thin:before {
  content: "\f1db";
}
.fa-header:before {
  content: "\f1dc";
}
.fa-paragraph:before {
  content: "\f1dd";
}
.fa-sliders:before {
  content: "\f1de";
}
.fa-share-alt:before {
  content: "\f1e0";
}
.fa-share-alt-square:before {
  content: "\f1e1";
}
.fa-bomb:before {
  content: "\f1e2";
}
.fa-soccer-ball-o:before,
.fa-futbol-o:before {
  content: "\f1e3";
}
.fa-tty:before {
  content: "\f1e4";
}
.fa-binoculars:before {
  content: "\f1e5";
}
.fa-plug:before {
  content: "\f1e6";
}
.fa-slideshare:before {
  content: "\f1e7";
}
.fa-twitch:before {
  content: "\f1e8";
}
.fa-yelp:before {
  content: "\f1e9";
}
.fa-newspaper-o:before {
  content: "\f1ea";
}
.fa-wifi:before {
  content: "\f1eb";
}
.fa-calculator:before {
  content: "\f1ec";
}
.fa-paypal:before {
  content: "\f1ed";
}
.fa-google-wallet:before {
  content: "\f1ee";
}
.fa-cc-visa:before {
  content: "\f1f0";
}
.fa-cc-mastercard:before {
  content: "\f1f1";
}
.fa-cc-discover:before {
  content: "\f1f2";
}
.fa-cc-amex:before {
  content: "\f1f3";
}
.fa-cc-paypal:before {
  content: "\f1f4";
}
.fa-cc-stripe:before {
  content: "\f1f5";
}
.fa-bell-slash:before {
  content: "\f1f6";
}
.fa-bell-slash-o:before {
  content: "\f1f7";
}
.fa-trash:before {
  content: "\f1f8";
}
.fa-copyright:before {
  content: "\f1f9";
}
.fa-at:before {
  content: "\f1fa";
}
.fa-eyedropper:before {
  content: "\f1fb";
}
.fa-paint-brush:before {
  content: "\f1fc";
}
.fa-birthday-cake:before {
  content: "\f1fd";
}
.fa-area-chart:before {
  content: "\f1fe";
}
.fa-pie-chart:before {
  content: "\f200";
}
.fa-line-chart:before {
  content: "\f201";
}
.fa-lastfm:before {
  content: "\f202";
}
.fa-lastfm-square:before {
  content: "\f203";
}
.fa-toggle-off:before {
  content: "\f204";
}
.fa-toggle-on:before {
  content: "\f205";
}
.fa-bicycle:before {
  content: "\f206";
}
.fa-bus:before {
  content: "\f207";
}
.fa-ioxhost:before {
  content: "\f208";
}
.fa-angellist:before {
  content: "\f209";
}
.fa-cc:before {
  content: "\f20a";
}
.fa-shekel:before,
.fa-sheqel:before,
.fa-ils:before {
  content: "\f20b";
}
.fa-meanpath:before {
  content: "\f20c";
}
/*!
*
* IPython base
*
*/
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
code {
  color: #000;
}
pre {
  font-size: inherit;
  line-height: inherit;
}
label {
  font-weight: normal;
}
/* Make the page background atleast 100% the height of the view port */
/* Make the page itself atleast 70% the height of the view port */
.border-box-sizing {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.corner-all {
  border-radius: 2px;
}
.no-padding {
  padding: 0px;
}
/* Flexible box model classes */
/* Taken from Alex Russell http://infrequently.org/2009/08/css-3-progress/ */
/* This file is a compatability layer.  It allows the usage of flexible box 
model layouts accross multiple browsers, including older browsers.  The newest,
universal implementation of the flexible box model is used when available (see
`Modern browsers` comments below).  Browsers that are known to implement this 
new spec completely include:

    Firefox 28.0+
    Chrome 29.0+
    Internet Explorer 11+ 
    Opera 17.0+

Browsers not listed, including Safari, are supported via the styling under the
`Old browsers` comments below.
*/
.hbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
.hbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.vbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
.vbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.hbox.reverse,
.vbox.reverse,
.reverse {
  /* Old browsers */
  -webkit-box-direction: reverse;
  -moz-box-direction: reverse;
  box-direction: reverse;
  /* Modern browsers */
  flex-direction: row-reverse;
}
.hbox.box-flex0,
.vbox.box-flex0,
.box-flex0 {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
  width: auto;
}
.hbox.box-flex1,
.vbox.box-flex1,
.box-flex1 {
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex,
.vbox.box-flex,
.box-flex {
  /* Old browsers */
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex2,
.vbox.box-flex2,
.box-flex2 {
  /* Old browsers */
  -webkit-box-flex: 2;
  -moz-box-flex: 2;
  box-flex: 2;
  /* Modern browsers */
  flex: 2;
}
.box-group1 {
  /*  Deprecated */
  -webkit-box-flex-group: 1;
  -moz-box-flex-group: 1;
  box-flex-group: 1;
}
.box-group2 {
  /* Deprecated */
  -webkit-box-flex-group: 2;
  -moz-box-flex-group: 2;
  box-flex-group: 2;
}
.hbox.start,
.vbox.start,
.start {
  /* Old browsers */
  -webkit-box-pack: start;
  -moz-box-pack: start;
  box-pack: start;
  /* Modern browsers */
  justify-content: flex-start;
}
.hbox.end,
.vbox.end,
.end {
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
}
.hbox.center,
.vbox.center,
.center {
  /* Old browsers */
  -webkit-box-pack: center;
  -moz-box-pack: center;
  box-pack: center;
  /* Modern browsers */
  justify-content: center;
}
.hbox.baseline,
.vbox.baseline,
.baseline {
  /* Old browsers */
  -webkit-box-pack: baseline;
  -moz-box-pack: baseline;
  box-pack: baseline;
  /* Modern browsers */
  justify-content: baseline;
}
.hbox.stretch,
.vbox.stretch,
.stretch {
  /* Old browsers */
  -webkit-box-pack: stretch;
  -moz-box-pack: stretch;
  box-pack: stretch;
  /* Modern browsers */
  justify-content: stretch;
}
.hbox.align-start,
.vbox.align-start,
.align-start {
  /* Old browsers */
  -webkit-box-align: start;
  -moz-box-align: start;
  box-align: start;
  /* Modern browsers */
  align-items: flex-start;
}
.hbox.align-end,
.vbox.align-end,
.align-end {
  /* Old browsers */
  -webkit-box-align: end;
  -moz-box-align: end;
  box-align: end;
  /* Modern browsers */
  align-items: flex-end;
}
.hbox.align-center,
.vbox.align-center,
.align-center {
  /* Old browsers */
  -webkit-box-align: center;
  -moz-box-align: center;
  box-align: center;
  /* Modern browsers */
  align-items: center;
}
.hbox.align-baseline,
.vbox.align-baseline,
.align-baseline {
  /* Old browsers */
  -webkit-box-align: baseline;
  -moz-box-align: baseline;
  box-align: baseline;
  /* Modern browsers */
  align-items: baseline;
}
.hbox.align-stretch,
.vbox.align-stretch,
.align-stretch {
  /* Old browsers */
  -webkit-box-align: stretch;
  -moz-box-align: stretch;
  box-align: stretch;
  /* Modern browsers */
  align-items: stretch;
}
div.error {
  margin: 2em;
  text-align: center;
}
div.error > h1 {
  font-size: 500%;
  line-height: normal;
}
div.error > p {
  font-size: 200%;
  line-height: normal;
}
div.traceback-wrapper {
  text-align: left;
  max-width: 800px;
  margin: auto;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
body {
  background-color: #fff;
  /* This makes sure that the body covers the entire window and needs to
       be in a different element than the display: box in wrapper below */
  position: absolute;
  left: 0px;
  right: 0px;
  top: 0px;
  bottom: 0px;
  overflow: visible;
}
body > #header {
  /* Initially hidden to prevent FLOUC */
  display: none;
  background-color: #fff;
  /* Display over codemirror */
  position: relative;
  z-index: 100;
}
body > #header #header-container {
  padding-bottom: 5px;
  padding-top: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
body > #header .header-bar {
  width: 100%;
  height: 1px;
  background: #e7e7e7;
  margin-bottom: -1px;
}
@media print {
  body > #header {
    display: none !important;
  }
}
#header-spacer {
  width: 100%;
  visibility: hidden;
}
@media print {
  #header-spacer {
    display: none;
  }
}
#ipython_notebook {
  padding-left: 0px;
  padding-top: 1px;
  padding-bottom: 1px;
}
@media (max-width: 991px) {
  #ipython_notebook {
    margin-left: 10px;
  }
}
[dir="rtl"] #ipython_notebook {
  float: right !important;
}
#noscript {
  width: auto;
  padding-top: 16px;
  padding-bottom: 16px;
  text-align: center;
  font-size: 22px;
  color: red;
  font-weight: bold;
}
#ipython_notebook img {
  height: 28px;
}
#site {
  width: 100%;
  display: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  overflow: auto;
}
@media print {
  #site {
    height: auto !important;
  }
}
/* Smaller buttons */
.ui-button .ui-button-text {
  padding: 0.2em 0.8em;
  font-size: 77%;
}
input.ui-button {
  padding: 0.3em 0.9em;
}
span#login_widget {
  float: right;
}
span#login_widget > .button,
#logout {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button:focus,
#logout:focus,
span#login_widget > .button.focus,
#logout.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
span#login_widget > .button:hover,
#logout:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active:hover,
#logout:active:hover,
span#login_widget > .button.active:hover,
#logout.active:hover,
.open > .dropdown-togglespan#login_widget > .button:hover,
.open > .dropdown-toggle#logout:hover,
span#login_widget > .button:active:focus,
#logout:active:focus,
span#login_widget > .button.active:focus,
#logout.active:focus,
.open > .dropdown-togglespan#login_widget > .button:focus,
.open > .dropdown-toggle#logout:focus,
span#login_widget > .button:active.focus,
#logout:active.focus,
span#login_widget > .button.active.focus,
#logout.active.focus,
.open > .dropdown-togglespan#login_widget > .button.focus,
.open > .dropdown-toggle#logout.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  background-image: none;
}
span#login_widget > .button.disabled:hover,
#logout.disabled:hover,
span#login_widget > .button[disabled]:hover,
#logout[disabled]:hover,
fieldset[disabled] span#login_widget > .button:hover,
fieldset[disabled] #logout:hover,
span#login_widget > .button.disabled:focus,
#logout.disabled:focus,
span#login_widget > .button[disabled]:focus,
#logout[disabled]:focus,
fieldset[disabled] span#login_widget > .button:focus,
fieldset[disabled] #logout:focus,
span#login_widget > .button.disabled.focus,
#logout.disabled.focus,
span#login_widget > .button[disabled].focus,
#logout[disabled].focus,
fieldset[disabled] span#login_widget > .button.focus,
fieldset[disabled] #logout.focus {
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button .badge,
#logout .badge {
  color: #fff;
  background-color: #333;
}
.nav-header {
  text-transform: none;
}
#header > span {
  margin-top: 10px;
}
.modal_stretch .modal-dialog {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  min-height: 80vh;
}
.modal_stretch .modal-dialog .modal-body {
  max-height: calc(100vh - 200px);
  overflow: auto;
  flex: 1;
}
@media (min-width: 768px) {
  .modal .modal-dialog {
    width: 700px;
  }
}
@media (min-width: 768px) {
  select.form-control {
    margin-left: 12px;
    margin-right: 12px;
  }
}
/*!
*
* IPython auth
*
*/
.center-nav {
  display: inline-block;
  margin-bottom: -4px;
}
/*!
*
* IPython tree view
*
*/
/* We need an invisible input field on top of the sentense*/
/* "Drag file onto the list ..." */
.alternate_upload {
  background-color: none;
  display: inline;
}
.alternate_upload.form {
  padding: 0;
  margin: 0;
}
.alternate_upload input.fileinput {
  text-align: center;
  vertical-align: middle;
  display: inline;
  opacity: 0;
  z-index: 2;
  width: 12ex;
  margin-right: -12ex;
}
.alternate_upload .btn-upload {
  height: 22px;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
[dir="rtl"] #tabs li {
  float: right;
}
ul#tabs {
  margin-bottom: 4px;
}
[dir="rtl"] ul#tabs {
  margin-right: 0px;
}
ul#tabs a {
  padding-top: 6px;
  padding-bottom: 4px;
}
ul.breadcrumb a:focus,
ul.breadcrumb a:hover {
  text-decoration: none;
}
ul.breadcrumb i.icon-home {
  font-size: 16px;
  margin-right: 4px;
}
ul.breadcrumb span {
  color: #5e5e5e;
}
.list_toolbar {
  padding: 4px 0 4px 0;
  vertical-align: middle;
}
.list_toolbar .tree-buttons {
  padding-top: 1px;
}
[dir="rtl"] .list_toolbar .tree-buttons {
  float: left !important;
}
[dir="rtl"] .list_toolbar .pull-right {
  padding-top: 1px;
  float: left !important;
}
[dir="rtl"] .list_toolbar .pull-left {
  float: right !important;
}
.dynamic-buttons {
  padding-top: 3px;
  display: inline-block;
}
.list_toolbar [class*="span"] {
  min-height: 24px;
}
.list_header {
  font-weight: bold;
  background-color: #EEE;
}
.list_placeholder {
  font-weight: bold;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
}
.list_container {
  margin-top: 4px;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 2px;
}
.list_container > div {
  border-bottom: 1px solid #ddd;
}
.list_container > div:hover .list-item {
  background-color: red;
}
.list_container > div:last-child {
  border: none;
}
.list_item:hover .list_item {
  background-color: #ddd;
}
.list_item a {
  text-decoration: none;
}
.list_item:hover {
  background-color: #fafafa;
}
.list_header > div,
.list_item > div {
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
.list_header > div input,
.list_item > div input {
  margin-right: 7px;
  margin-left: 14px;
  vertical-align: baseline;
  line-height: 22px;
  position: relative;
  top: -1px;
}
.list_header > div .item_link,
.list_item > div .item_link {
  margin-left: -1px;
  vertical-align: baseline;
  line-height: 22px;
}
.new-file input[type=checkbox] {
  visibility: hidden;
}
.item_name {
  line-height: 22px;
  height: 24px;
}
.item_icon {
  font-size: 14px;
  color: #5e5e5e;
  margin-right: 7px;
  margin-left: 7px;
  line-height: 22px;
  vertical-align: baseline;
}
.item_buttons {
  line-height: 1em;
  margin-left: -5px;
}
.item_buttons .btn,
.item_buttons .btn-group,
.item_buttons .input-group {
  float: left;
}
.item_buttons > .btn,
.item_buttons > .btn-group,
.item_buttons > .input-group {
  margin-left: 5px;
}
.item_buttons .btn {
  min-width: 13ex;
}
.item_buttons .running-indicator {
  padding-top: 4px;
  color: #5cb85c;
}
.item_buttons .kernel-name {
  padding-top: 4px;
  color: #5bc0de;
  margin-right: 7px;
  float: left;
}
.toolbar_info {
  height: 24px;
  line-height: 24px;
}
.list_item input:not([type=checkbox]) {
  padding-top: 3px;
  padding-bottom: 3px;
  height: 22px;
  line-height: 14px;
  margin: 0px;
}
.highlight_text {
  color: blue;
}
#project_name {
  display: inline-block;
  padding-left: 7px;
  margin-left: -2px;
}
#project_name > .breadcrumb {
  padding: 0px;
  margin-bottom: 0px;
  background-color: transparent;
  font-weight: bold;
}
#tree-selector {
  padding-right: 0px;
}
[dir="rtl"] #tree-selector a {
  float: right;
}
#button-select-all {
  min-width: 50px;
}
#select-all {
  margin-left: 7px;
  margin-right: 2px;
}
.menu_icon {
  margin-right: 2px;
}
.tab-content .row {
  margin-left: 0px;
  margin-right: 0px;
}
.folder_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f114";
}
.folder_icon:before.pull-left {
  margin-right: .3em;
}
.folder_icon:before.pull-right {
  margin-left: .3em;
}
.notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
}
.notebook_icon:before.pull-left {
  margin-right: .3em;
}
.notebook_icon:before.pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
  color: #5cb85c;
}
.running_notebook_icon:before.pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.pull-right {
  margin-left: .3em;
}
.file_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f016";
  position: relative;
  top: -2px;
}
.file_icon:before.pull-left {
  margin-right: .3em;
}
.file_icon:before.pull-right {
  margin-left: .3em;
}
#notebook_toolbar .pull-right {
  padding-top: 0px;
  margin-right: -1px;
}
ul#new-menu {
  left: auto;
  right: 0;
}
[dir="rtl"] #new-menu {
  text-align: right;
}
.kernel-menu-icon {
  padding-right: 12px;
  width: 24px;
  content: "\f096";
}
.kernel-menu-icon:before {
  content: "\f096";
}
.kernel-menu-icon-current:before {
  content: "\f00c";
}
#tab_content {
  padding-top: 20px;
}
#running .panel-group .panel {
  margin-top: 3px;
  margin-bottom: 1em;
}
#running .panel-group .panel .panel-heading {
  background-color: #EEE;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
#running .panel-group .panel .panel-heading a:focus,
#running .panel-group .panel .panel-heading a:hover {
  text-decoration: none;
}
#running .panel-group .panel .panel-body {
  padding: 0px;
}
#running .panel-group .panel .panel-body .list_container {
  margin-top: 0px;
  margin-bottom: 0px;
  border: 0px;
  border-radius: 0px;
}
#running .panel-group .panel .panel-body .list_container .list_item {
  border-bottom: 1px solid #ddd;
}
#running .panel-group .panel .panel-body .list_container .list_item:last-child {
  border-bottom: 0px;
}
[dir="rtl"] #running .col-sm-8 {
  float: right !important;
}
.delete-button {
  display: none;
}
.duplicate-button {
  display: none;
}
.rename-button {
  display: none;
}
.shutdown-button {
  display: none;
}
.dynamic-instructions {
  display: inline-block;
  padding-top: 4px;
}
/*!
*
* IPython text editor webapp
*
*/
.selected-keymap i.fa {
  padding: 0px 5px;
}
.selected-keymap i.fa:before {
  content: "\f00c";
}
#mode-menu {
  overflow: auto;
  max-height: 20em;
}
.edit_app #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.edit_app #menubar .navbar {
  /* Use a negative 1 bottom margin, so the border overlaps the border of the
    header */
  margin-bottom: -1px;
}
.dirty-indicator {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator.pull-left {
  margin-right: .3em;
}
.dirty-indicator.pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-dirty.pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-clean.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f00c";
}
.dirty-indicator-clean:before.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.pull-right {
  margin-left: .3em;
}
#filename {
  font-size: 16pt;
  display: table;
  padding: 0px 5px;
}
#current-mode {
  padding-left: 5px;
  padding-right: 5px;
}
#texteditor-backdrop {
  padding-top: 20px;
  padding-bottom: 20px;
}
@media not print {
  #texteditor-backdrop {
    background-color: #EEE;
  }
}
@media print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container {
    padding: 0px;
    background-color: #fff;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
/*!
*
* IPython notebook
*
*/
/* CSS font colors for translated ANSI colors. */
.ansibold {
  font-weight: bold;
}
/* use dark versions for foreground, to improve visibility */
.ansiblack {
  color: black;
}
.ansired {
  color: darkred;
}
.ansigreen {
  color: darkgreen;
}
.ansiyellow {
  color: #c4a000;
}
.ansiblue {
  color: darkblue;
}
.ansipurple {
  color: darkviolet;
}
.ansicyan {
  color: steelblue;
}
.ansigray {
  color: gray;
}
/* and light for background, for the same reason */
.ansibgblack {
  background-color: black;
}
.ansibgred {
  background-color: red;
}
.ansibggreen {
  background-color: green;
}
.ansibgyellow {
  background-color: yellow;
}
.ansibgblue {
  background-color: blue;
}
.ansibgpurple {
  background-color: magenta;
}
.ansibgcyan {
  background-color: cyan;
}
.ansibggray {
  background-color: gray;
}
div.cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  border-radius: 2px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  border-width: 1px;
  border-style: solid;
  border-color: transparent;
  width: 100%;
  padding: 5px;
  /* This acts as a spacer between cells, that is outside the border */
  margin: 0px;
  outline: none;
  border-left-width: 1px;
  padding-left: 5px;
  background: linear-gradient(to right, transparent -40px, transparent 1px, transparent 1px, transparent 100%);
}
div.cell.jupyter-soft-selected {
  border-left-color: #90CAF9;
  border-left-color: #E3F2FD;
  border-left-width: 1px;
  padding-left: 5px;
  border-right-color: #E3F2FD;
  border-right-width: 1px;
  background: #E3F2FD;
}
@media print {
  div.cell.jupyter-soft-selected {
    border-color: transparent;
  }
}
div.cell.selected {
  border-color: #ababab;
  border-left-width: 0px;
  padding-left: 6px;
  background: linear-gradient(to right, #42A5F5 -40px, #42A5F5 5px, transparent 5px, transparent 100%);
}
@media print {
  div.cell.selected {
    border-color: transparent;
  }
}
div.cell.selected.jupyter-soft-selected {
  border-left-width: 0;
  padding-left: 6px;
  background: linear-gradient(to right, #42A5F5 -40px, #42A5F5 7px, #E3F2FD 7px, #E3F2FD 100%);
}
.edit_mode div.cell.selected {
  border-color: #66BB6A;
  border-left-width: 0px;
  padding-left: 6px;
  background: linear-gradient(to right, #66BB6A -40px, #66BB6A 5px, transparent 5px, transparent 100%);
}
@media print {
  .edit_mode div.cell.selected {
    border-color: transparent;
  }
}
.prompt {
  /* This needs to be wide enough for 3 digit prompt numbers: In[100]: */
  min-width: 14ex;
  /* This padding is tuned to match the padding on the CodeMirror editor. */
  padding: 0.4em;
  margin: 0px;
  font-family: monospace;
  text-align: right;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
  /* Don't highlight prompt number selection */
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  /* Use default cursor */
  cursor: default;
}
@media (max-width: 540px) {
  .prompt {
    text-align: left;
  }
}
div.inner_cell {
  min-width: 0;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_area {
  border: 1px solid #cfcfcf;
  border-radius: 2px;
  background: #f7f7f7;
  line-height: 1.21429em;
}
/* This is needed so that empty prompt areas can collapse to zero height when there
   is no content in the output_subarea and the prompt. The main purpose of this is
   to make sure that empty JavaScript output_subareas have no height. */
div.prompt:empty {
  padding-top: 0;
  padding-bottom: 0;
}
div.unrecognized_cell {
  padding: 5px 5px 5px 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.unrecognized_cell .inner_cell {
  border-radius: 2px;
  padding: 5px;
  font-weight: bold;
  color: red;
  border: 1px solid #cfcfcf;
  background: #eaeaea;
}
div.unrecognized_cell .inner_cell a {
  color: inherit;
  text-decoration: none;
}
div.unrecognized_cell .inner_cell a:hover {
  color: inherit;
  text-decoration: none;
}
@media (max-width: 540px) {
  div.unrecognized_cell > div.prompt {
    display: none;
  }
}
div.code_cell {
  /* avoid page breaking on code cells when printing */
}
@media print {
  div.code_cell {
    page-break-inside: avoid;
  }
}
/* any special styling for code cells that are currently running goes here */
div.input {
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.input {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_prompt {
  color: #303F9F;
  border-top: 1px solid transparent;
}
div.input_area > div.highlight {
  margin: 0.4em;
  border: none;
  padding: 0px;
  background-color: transparent;
}
div.input_area > div.highlight > pre {
  margin: 0px;
  border: none;
  padding: 0px;
  background-color: transparent;
}
/* The following gets added to the <head> if it is detected that the user has a
 * monospace font with inconsistent normal/bold/italic height.  See
 * notebookmain.js.  Such fonts will have keywords vertically offset with
 * respect to the rest of the text.  The user should select a better font.
 * See: https://github.com/ipython/ipython/issues/1503
 *
 * .CodeMirror span {
 *      vertical-align: bottom;
 * }
 */
.CodeMirror {
  line-height: 1.21429em;
  /* Changed from 1em to our global default */
  font-size: 14px;
  height: auto;
  /* Changed to auto to autogrow */
  background: none;
  /* Changed from white to allow our bg to show through */
}
.CodeMirror-scroll {
  /*  The CodeMirror docs are a bit fuzzy on if overflow-y should be hidden or visible.*/
  /*  We have found that if it is visible, vertical scrollbars appear with font size changes.*/
  overflow-y: hidden;
  overflow-x: auto;
}
.CodeMirror-lines {
  /* In CM2, this used to be 0.4em, but in CM3 it went to 4px. We need the em value because */
  /* we have set a different line-height and want this to scale with that. */
  padding: 0.4em;
}
.CodeMirror-linenumber {
  padding: 0 8px 0 4px;
}
.CodeMirror-gutters {
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.CodeMirror pre {
  /* In CM3 this went to 4px from 0 in CM2. We need the 0 value because of how we size */
  /* .CodeMirror-lines */
  padding: 0;
  border: 0;
  border-radius: 0;
}
/*

Original style from softwaremaniacs.org (c) Ivan Sagalaev <Maniac@SoftwareManiacs.Org>
Adapted from GitHub theme

*/
.highlight-base {
  color: #000;
}
.highlight-variable {
  color: #000;
}
.highlight-variable-2 {
  color: #1a1a1a;
}
.highlight-variable-3 {
  color: #333333;
}
.highlight-string {
  color: #BA2121;
}
.highlight-comment {
  color: #408080;
  font-style: italic;
}
.highlight-number {
  color: #080;
}
.highlight-atom {
  color: #88F;
}
.highlight-keyword {
  color: #008000;
  font-weight: bold;
}
.highlight-builtin {
  color: #008000;
}
.highlight-error {
  color: #f00;
}
.highlight-operator {
  color: #AA22FF;
  font-weight: bold;
}
.highlight-meta {
  color: #AA22FF;
}
/* previously not defined, copying from default codemirror */
.highlight-def {
  color: #00f;
}
.highlight-string-2 {
  color: #f50;
}
.highlight-qualifier {
  color: #555;
}
.highlight-bracket {
  color: #997;
}
.highlight-tag {
  color: #170;
}
.highlight-attribute {
  color: #00c;
}
.highlight-header {
  color: blue;
}
.highlight-quote {
  color: #090;
}
.highlight-link {
  color: #00c;
}
/* apply the same style to codemirror */
.cm-s-ipython span.cm-keyword {
  color: #008000;
  font-weight: bold;
}
.cm-s-ipython span.cm-atom {
  color: #88F;
}
.cm-s-ipython span.cm-number {
  color: #080;
}
.cm-s-ipython span.cm-def {
  color: #00f;
}
.cm-s-ipython span.cm-variable {
  color: #000;
}
.cm-s-ipython span.cm-operator {
  color: #AA22FF;
  font-weight: bold;
}
.cm-s-ipython span.cm-variable-2 {
  color: #1a1a1a;
}
.cm-s-ipython span.cm-variable-3 {
  color: #333333;
}
.cm-s-ipython span.cm-comment {
  color: #408080;
  font-style: italic;
}
.cm-s-ipython span.cm-string {
  color: #BA2121;
}
.cm-s-ipython span.cm-string-2 {
  color: #f50;
}
.cm-s-ipython span.cm-meta {
  color: #AA22FF;
}
.cm-s-ipython span.cm-qualifier {
  color: #555;
}
.cm-s-ipython span.cm-builtin {
  color: #008000;
}
.cm-s-ipython span.cm-bracket {
  color: #997;
}
.cm-s-ipython span.cm-tag {
  color: #170;
}
.cm-s-ipython span.cm-attribute {
  color: #00c;
}
.cm-s-ipython span.cm-header {
  color: blue;
}
.cm-s-ipython span.cm-quote {
  color: #090;
}
.cm-s-ipython span.cm-link {
  color: #00c;
}
.cm-s-ipython span.cm-error {
  color: #f00;
}
.cm-s-ipython span.cm-tab {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAMCAYAAAAkuj5RAAAAAXNSR0IArs4c6QAAAGFJREFUSMft1LsRQFAQheHPowAKoACx3IgEKtaEHujDjORSgWTH/ZOdnZOcM/sgk/kFFWY0qV8foQwS4MKBCS3qR6ixBJvElOobYAtivseIE120FaowJPN75GMu8j/LfMwNjh4HUpwg4LUAAAAASUVORK5CYII=);
  background-position: right;
  background-repeat: no-repeat;
}
div.output_wrapper {
  /* this position must be relative to enable descendents to be absolute within it */
  position: relative;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  z-index: 1;
}
/* class for the output area when it should be height-limited */
div.output_scroll {
  /* ideally, this would be max-height, but FF barfs all over that */
  height: 24em;
  /* FF needs this *and the wrapper* to specify full width, or it will shrinkwrap */
  width: 100%;
  overflow: auto;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  display: block;
}
/* output div while it is collapsed */
div.output_collapsed {
  margin: 0px;
  padding: 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
div.out_prompt_overlay {
  height: 100%;
  padding: 0px 0.4em;
  position: absolute;
  border-radius: 2px;
}
div.out_prompt_overlay:hover {
  /* use inner shadow to get border that is computed the same on WebKit/FF */
  -webkit-box-shadow: inset 0 0 1px #000;
  box-shadow: inset 0 0 1px #000;
  background: rgba(240, 240, 240, 0.5);
}
div.output_prompt {
  color: #D84315;
}
/* This class is the outer container of all output sections. */
div.output_area {
  padding: 0px;
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.output_area .MathJax_Display {
  text-align: left !important;
}
div.output_area .rendered_html table {
  margin-left: 0;
  margin-right: 0;
}
div.output_area .rendered_html img {
  margin-left: 0;
  margin-right: 0;
}
div.output_area img,
div.output_area svg {
  max-width: 100%;
  height: auto;
}
div.output_area img.unconfined,
div.output_area svg.unconfined {
  max-width: none;
}
/* This is needed to protect the pre formating from global settings such
   as that of bootstrap */
.output {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.output_area {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
div.output_area pre {
  margin: 0;
  padding: 0;
  border: 0;
  vertical-align: baseline;
  color: black;
  background-color: transparent;
  border-radius: 0;
}
/* This class is for the output subarea inside the output_area and after
   the prompt div. */
div.output_subarea {
  overflow-x: auto;
  padding: 0.4em;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
  max-width: calc(100% - 14ex);
}
div.output_scroll div.output_subarea {
  overflow-x: visible;
}
/* The rest of the output_* classes are for special styling of the different
   output types */
/* all text output has this class: */
div.output_text {
  text-align: left;
  color: #000;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
}
/* stdout/stderr are 'text' as well as 'stream', but execute_result/error are *not* streams */
div.output_stderr {
  background: #fdd;
  /* very light red background for stderr */
}
div.output_latex {
  text-align: left;
}
/* Empty output_javascript divs should have no height */
div.output_javascript:empty {
  padding: 0;
}
.js-error {
  color: darkred;
}
/* raw_input styles */
div.raw_input_container {
  line-height: 1.21429em;
  padding-top: 5px;
}
pre.raw_input_prompt {
  /* nothing needed here. */
}
input.raw_input {
  font-family: monospace;
  font-size: inherit;
  color: inherit;
  width: auto;
  /* make sure input baseline aligns with prompt */
  vertical-align: baseline;
  /* padding + margin = 0.5em between prompt and cursor */
  padding: 0em 0.25em;
  margin: 0em 0.25em;
}
input.raw_input:focus {
  box-shadow: none;
}
p.p-space {
  margin-bottom: 10px;
}
div.output_unrecognized {
  padding: 5px;
  font-weight: bold;
  color: red;
}
div.output_unrecognized a {
  color: inherit;
  text-decoration: none;
}
div.output_unrecognized a:hover {
  color: inherit;
  text-decoration: none;
}
.rendered_html {
  color: #000;
  /* any extras will just be numbers: */
}
.rendered_html em {
  font-style: italic;
}
.rendered_html strong {
  font-weight: bold;
}
.rendered_html u {
  text-decoration: underline;
}
.rendered_html :link {
  text-decoration: underline;
}
.rendered_html :visited {
  text-decoration: underline;
}
.rendered_html h1 {
  font-size: 185.7%;
  margin: 1.08em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h2 {
  font-size: 157.1%;
  margin: 1.27em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h3 {
  font-size: 128.6%;
  margin: 1.55em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h4 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h5 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h6 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h1:first-child {
  margin-top: 0.538em;
}
.rendered_html h2:first-child {
  margin-top: 0.636em;
}
.rendered_html h3:first-child {
  margin-top: 0.777em;
}
.rendered_html h4:first-child {
  margin-top: 1em;
}
.rendered_html h5:first-child {
  margin-top: 1em;
}
.rendered_html h6:first-child {
  margin-top: 1em;
}
.rendered_html ul {
  list-style: disc;
  margin: 0em 2em;
  padding-left: 0px;
}
.rendered_html ul ul {
  list-style: square;
  margin: 0em 2em;
}
.rendered_html ul ul ul {
  list-style: circle;
  margin: 0em 2em;
}
.rendered_html ol {
  list-style: decimal;
  margin: 0em 2em;
  padding-left: 0px;
}
.rendered_html ol ol {
  list-style: upper-alpha;
  margin: 0em 2em;
}
.rendered_html ol ol ol {
  list-style: lower-alpha;
  margin: 0em 2em;
}
.rendered_html ol ol ol ol {
  list-style: lower-roman;
  margin: 0em 2em;
}
.rendered_html ol ol ol ol ol {
  list-style: decimal;
  margin: 0em 2em;
}
.rendered_html * + ul {
  margin-top: 1em;
}
.rendered_html * + ol {
  margin-top: 1em;
}
.rendered_html hr {
  color: black;
  background-color: black;
}
.rendered_html pre {
  margin: 1em 2em;
}
.rendered_html pre,
.rendered_html code {
  border: 0;
  background-color: #fff;
  color: #000;
  font-size: 100%;
  padding: 0px;
}
.rendered_html blockquote {
  margin: 1em 2em;
}
.rendered_html table {
  margin-left: auto;
  margin-right: auto;
  border: 1px solid black;
  border-collapse: collapse;
}
.rendered_html tr,
.rendered_html th,
.rendered_html td {
  border: 1px solid black;
  border-collapse: collapse;
  margin: 1em 2em;
}
.rendered_html td,
.rendered_html th {
  text-align: left;
  vertical-align: middle;
  padding: 4px;
}
.rendered_html th {
  font-weight: bold;
}
.rendered_html * + table {
  margin-top: 1em;
}
.rendered_html p {
  text-align: left;
}
.rendered_html * + p {
  margin-top: 1em;
}
.rendered_html img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.rendered_html * + img {
  margin-top: 1em;
}
.rendered_html img,
.rendered_html svg {
  max-width: 100%;
  height: auto;
}
.rendered_html img.unconfined,
.rendered_html svg.unconfined {
  max-width: none;
}
div.text_cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.text_cell > div.prompt {
    display: none;
  }
}
div.text_cell_render {
  /*font-family: "Helvetica Neue", Arial, Helvetica, Geneva, sans-serif;*/
  outline: none;
  resize: none;
  width: inherit;
  border-style: none;
  padding: 0.5em 0.5em 0.5em 0.4em;
  color: #000;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
a.anchor-link:link {
  text-decoration: none;
  padding: 0px 20px;
  visibility: hidden;
}
h1:hover .anchor-link,
h2:hover .anchor-link,
h3:hover .anchor-link,
h4:hover .anchor-link,
h5:hover .anchor-link,
h6:hover .anchor-link {
  visibility: visible;
}
.text_cell.rendered .input_area {
  display: none;
}
.text_cell.rendered .rendered_html {
  overflow-x: auto;
  overflow-y: hidden;
}
.text_cell.unrendered .text_cell_render {
  display: none;
}
.cm-header-1,
.cm-header-2,
.cm-header-3,
.cm-header-4,
.cm-header-5,
.cm-header-6 {
  font-weight: bold;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
.cm-header-1 {
  font-size: 185.7%;
}
.cm-header-2 {
  font-size: 157.1%;
}
.cm-header-3 {
  font-size: 128.6%;
}
.cm-header-4 {
  font-size: 110%;
}
.cm-header-5 {
  font-size: 100%;
  font-style: italic;
}
.cm-header-6 {
  font-size: 100%;
  font-style: italic;
}
/*!
*
* IPython notebook webapp
*
*/
@media (max-width: 767px) {
  .notebook_app {
    padding-left: 0px;
    padding-right: 0px;
  }
}
#ipython-main-app {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook_panel {
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook {
  font-size: 14px;
  line-height: 20px;
  overflow-y: hidden;
  overflow-x: auto;
  width: 100%;
  /* This spaces the page away from the edge of the notebook area */
  padding-top: 20px;
  margin: 0px;
  outline: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  min-height: 100%;
}
@media not print {
  #notebook-container {
    padding: 15px;
    background-color: #fff;
    min-height: 0;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
@media print {
  #notebook-container {
    width: 100%;
  }
}
div.ui-widget-content {
  border: 1px solid #ababab;
  outline: none;
}
pre.dialog {
  background-color: #f7f7f7;
  border: 1px solid #ddd;
  border-radius: 2px;
  padding: 0.4em;
  padding-left: 2em;
}
p.dialog {
  padding: 0.2em;
}
/* Word-wrap output correctly.  This is the CSS3 spelling, though Firefox seems
   to not honor it correctly.  Webkit browsers (Chrome, rekonq, Safari) do.
 */
pre,
code,
kbd,
samp {
  white-space: pre-wrap;
}
#fonttest {
  font-family: monospace;
}
p {
  margin-bottom: 0;
}
.end_space {
  min-height: 100px;
  transition: height .2s ease;
}
.notebook_app > #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
@media not print {
  .notebook_app {
    background-color: #EEE;
  }
}
kbd {
  border-style: solid;
  border-width: 1px;
  box-shadow: none;
  margin: 2px;
  padding-left: 2px;
  padding-right: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
/* CSS for the cell toolbar */
.celltoolbar {
  border: thin solid #CFCFCF;
  border-bottom: none;
  background: #EEE;
  border-radius: 2px 2px 0px 0px;
  width: 100%;
  height: 29px;
  padding-right: 4px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
  display: -webkit-flex;
}
@media print {
  .celltoolbar {
    display: none;
  }
}
.ctb_hideshow {
  display: none;
  vertical-align: bottom;
}
/* ctb_show is added to the ctb_hideshow div to show the cell toolbar.
   Cell toolbars are only shown when the ctb_global_show class is also set.
*/
.ctb_global_show .ctb_show.ctb_hideshow {
  display: block;
}
.ctb_global_show .ctb_show + .input_area,
.ctb_global_show .ctb_show + div.text_cell_input,
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border-top-right-radius: 0px;
  border-top-left-radius: 0px;
}
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border: 1px solid #cfcfcf;
}
.celltoolbar {
  font-size: 87%;
  padding-top: 3px;
}
.celltoolbar select {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  width: inherit;
  font-size: inherit;
  height: 22px;
  padding: 0px;
  display: inline-block;
}
.celltoolbar select:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.celltoolbar select::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.celltoolbar select:-ms-input-placeholder {
  color: #999;
}
.celltoolbar select::-webkit-input-placeholder {
  color: #999;
}
.celltoolbar select::-ms-expand {
  border: 0;
  background-color: transparent;
}
.celltoolbar select[disabled],
.celltoolbar select[readonly],
fieldset[disabled] .celltoolbar select {
  background-color: #eeeeee;
  opacity: 1;
}
.celltoolbar select[disabled],
fieldset[disabled] .celltoolbar select {
  cursor: not-allowed;
}
textarea.celltoolbar select {
  height: auto;
}
select.celltoolbar select {
  height: 30px;
  line-height: 30px;
}
textarea.celltoolbar select,
select[multiple].celltoolbar select {
  height: auto;
}
.celltoolbar label {
  margin-left: 5px;
  margin-right: 5px;
}
.completions {
  position: absolute;
  z-index: 110;
  overflow: hidden;
  border: 1px solid #ababab;
  border-radius: 2px;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  line-height: 1;
}
.completions select {
  background: white;
  outline: none;
  border: none;
  padding: 0px;
  margin: 0px;
  overflow: auto;
  font-family: monospace;
  font-size: 110%;
  color: #000;
  width: auto;
}
.completions select option.context {
  color: #286090;
}
#kernel_logo_widget {
  float: right !important;
  float: right;
}
#kernel_logo_widget .current_kernel_logo {
  display: none;
  margin-top: -1px;
  margin-bottom: -1px;
  width: 32px;
  height: 32px;
}
#menubar {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  margin-top: 1px;
}
#menubar .navbar {
  border-top: 1px;
  border-radius: 0px 0px 2px 2px;
  margin-bottom: 0px;
}
#menubar .navbar-toggle {
  float: left;
  padding-top: 7px;
  padding-bottom: 7px;
  border: none;
}
#menubar .navbar-collapse {
  clear: left;
}
.nav-wrapper {
  border-bottom: 1px solid #e7e7e7;
}
i.menu-icon {
  padding-top: 4px;
}
ul#help_menu li a {
  overflow: hidden;
  padding-right: 2.2em;
}
ul#help_menu li a i {
  margin-right: -1.2em;
}
.dropdown-submenu {
  position: relative;
}
.dropdown-submenu > .dropdown-menu {
  top: 0;
  left: 100%;
  margin-top: -6px;
  margin-left: -1px;
}
.dropdown-submenu:hover > .dropdown-menu {
  display: block;
}
.dropdown-submenu > a:after {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: block;
  content: "\f0da";
  float: right;
  color: #333333;
  margin-top: 2px;
  margin-right: -10px;
}
.dropdown-submenu > a:after.pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.pull-right {
  margin-left: .3em;
}
.dropdown-submenu:hover > a:after {
  color: #262626;
}
.dropdown-submenu.pull-left {
  float: none;
}
.dropdown-submenu.pull-left > .dropdown-menu {
  left: -100%;
  margin-left: 10px;
}
#notification_area {
  float: right !important;
  float: right;
  z-index: 10;
}
.indicator_area {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
#kernel_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  border-left: 1px solid;
}
#kernel_indicator .kernel_indicator_name {
  padding-left: 5px;
  padding-right: 5px;
}
#modal_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
#readonly-indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  margin-top: 2px;
  margin-bottom: 0px;
  margin-left: 0px;
  margin-right: 0px;
  display: none;
}
.modal_indicator:before {
  width: 1.28571429em;
  text-align: center;
}
.edit_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f040";
}
.edit_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: ' ';
}
.command_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f10c";
}
.kernel_idle_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f111";
}
.kernel_busy_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f1e2";
}
.kernel_dead_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f127";
}
.kernel_disconnected_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.pull-right {
  margin-left: .3em;
}
.notification_widget {
  color: #777;
  z-index: 10;
  background: rgba(240, 240, 240, 0.5);
  margin-right: 4px;
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget:focus,
.notification_widget.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.notification_widget:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active:hover,
.notification_widget.active:hover,
.open > .dropdown-toggle.notification_widget:hover,
.notification_widget:active:focus,
.notification_widget.active:focus,
.open > .dropdown-toggle.notification_widget:focus,
.notification_widget:active.focus,
.notification_widget.active.focus,
.open > .dropdown-toggle.notification_widget.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  background-image: none;
}
.notification_widget.disabled:hover,
.notification_widget[disabled]:hover,
fieldset[disabled] .notification_widget:hover,
.notification_widget.disabled:focus,
.notification_widget[disabled]:focus,
fieldset[disabled] .notification_widget:focus,
.notification_widget.disabled.focus,
.notification_widget[disabled].focus,
fieldset[disabled] .notification_widget.focus {
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget .badge {
  color: #fff;
  background-color: #333;
}
.notification_widget.warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning:focus,
.notification_widget.warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.notification_widget.warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active:hover,
.notification_widget.warning.active:hover,
.open > .dropdown-toggle.notification_widget.warning:hover,
.notification_widget.warning:active:focus,
.notification_widget.warning.active:focus,
.open > .dropdown-toggle.notification_widget.warning:focus,
.notification_widget.warning:active.focus,
.notification_widget.warning.active.focus,
.open > .dropdown-toggle.notification_widget.warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  background-image: none;
}
.notification_widget.warning.disabled:hover,
.notification_widget.warning[disabled]:hover,
fieldset[disabled] .notification_widget.warning:hover,
.notification_widget.warning.disabled:focus,
.notification_widget.warning[disabled]:focus,
fieldset[disabled] .notification_widget.warning:focus,
.notification_widget.warning.disabled.focus,
.notification_widget.warning[disabled].focus,
fieldset[disabled] .notification_widget.warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.notification_widget.success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success:focus,
.notification_widget.success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.notification_widget.success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active:hover,
.notification_widget.success.active:hover,
.open > .dropdown-toggle.notification_widget.success:hover,
.notification_widget.success:active:focus,
.notification_widget.success.active:focus,
.open > .dropdown-toggle.notification_widget.success:focus,
.notification_widget.success:active.focus,
.notification_widget.success.active.focus,
.open > .dropdown-toggle.notification_widget.success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  background-image: none;
}
.notification_widget.success.disabled:hover,
.notification_widget.success[disabled]:hover,
fieldset[disabled] .notification_widget.success:hover,
.notification_widget.success.disabled:focus,
.notification_widget.success[disabled]:focus,
fieldset[disabled] .notification_widget.success:focus,
.notification_widget.success.disabled.focus,
.notification_widget.success[disabled].focus,
fieldset[disabled] .notification_widget.success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.notification_widget.info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info:focus,
.notification_widget.info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.notification_widget.info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active:hover,
.notification_widget.info.active:hover,
.open > .dropdown-toggle.notification_widget.info:hover,
.notification_widget.info:active:focus,
.notification_widget.info.active:focus,
.open > .dropdown-toggle.notification_widget.info:focus,
.notification_widget.info:active.focus,
.notification_widget.info.active.focus,
.open > .dropdown-toggle.notification_widget.info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  background-image: none;
}
.notification_widget.info.disabled:hover,
.notification_widget.info[disabled]:hover,
fieldset[disabled] .notification_widget.info:hover,
.notification_widget.info.disabled:focus,
.notification_widget.info[disabled]:focus,
fieldset[disabled] .notification_widget.info:focus,
.notification_widget.info.disabled.focus,
.notification_widget.info[disabled].focus,
fieldset[disabled] .notification_widget.info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.notification_widget.danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger:focus,
.notification_widget.danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.notification_widget.danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active:hover,
.notification_widget.danger.active:hover,
.open > .dropdown-toggle.notification_widget.danger:hover,
.notification_widget.danger:active:focus,
.notification_widget.danger.active:focus,
.open > .dropdown-toggle.notification_widget.danger:focus,
.notification_widget.danger:active.focus,
.notification_widget.danger.active.focus,
.open > .dropdown-toggle.notification_widget.danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  background-image: none;
}
.notification_widget.danger.disabled:hover,
.notification_widget.danger[disabled]:hover,
fieldset[disabled] .notification_widget.danger:hover,
.notification_widget.danger.disabled:focus,
.notification_widget.danger[disabled]:focus,
fieldset[disabled] .notification_widget.danger:focus,
.notification_widget.danger.disabled.focus,
.notification_widget.danger[disabled].focus,
fieldset[disabled] .notification_widget.danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger .badge {
  color: #d9534f;
  background-color: #fff;
}
div#pager {
  background-color: #fff;
  font-size: 14px;
  line-height: 20px;
  overflow: hidden;
  display: none;
  position: fixed;
  bottom: 0px;
  width: 100%;
  max-height: 50%;
  padding-top: 8px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  /* Display over codemirror */
  z-index: 100;
  /* Hack which prevents jquery ui resizable from changing top. */
  top: auto !important;
}
div#pager pre {
  line-height: 1.21429em;
  color: #000;
  background-color: #f7f7f7;
  padding: 0.4em;
}
div#pager #pager-button-area {
  position: absolute;
  top: 8px;
  right: 20px;
}
div#pager #pager-contents {
  position: relative;
  overflow: auto;
  width: 100%;
  height: 100%;
}
div#pager #pager-contents #pager-container {
  position: relative;
  padding: 15px 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
div#pager .ui-resizable-handle {
  top: 0px;
  height: 8px;
  background: #f7f7f7;
  border-top: 1px solid #cfcfcf;
  border-bottom: 1px solid #cfcfcf;
  /* This injects handle bars (a short, wide = symbol) for 
        the resize handle. */
}
div#pager .ui-resizable-handle::after {
  content: '';
  top: 2px;
  left: 50%;
  height: 3px;
  width: 30px;
  margin-left: -15px;
  position: absolute;
  border-top: 1px solid #cfcfcf;
}
.quickhelp {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  line-height: 1.8em;
}
.shortcut_key {
  display: inline-block;
  width: 21ex;
  text-align: right;
  font-family: monospace;
}
.shortcut_descr {
  display: inline-block;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
span.save_widget {
  margin-top: 6px;
}
span.save_widget span.filename {
  height: 1em;
  line-height: 1em;
  padding: 3px;
  margin-left: 16px;
  border: none;
  font-size: 146.5%;
  border-radius: 2px;
}
span.save_widget span.filename:hover {
  background-color: #e6e6e6;
}
span.checkpoint_status,
span.autosave_status {
  font-size: small;
}
@media (max-width: 767px) {
  span.save_widget {
    font-size: small;
  }
  span.checkpoint_status,
  span.autosave_status {
    display: none;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  span.checkpoint_status {
    display: none;
  }
  span.autosave_status {
    font-size: x-small;
  }
}
.toolbar {
  padding: 0px;
  margin-left: -5px;
  margin-top: 2px;
  margin-bottom: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.toolbar select,
.toolbar label {
  width: auto;
  vertical-align: middle;
  margin-right: 2px;
  margin-bottom: 0px;
  display: inline;
  font-size: 92%;
  margin-left: 0.3em;
  margin-right: 0.3em;
  padding: 0px;
  padding-top: 3px;
}
.toolbar .btn {
  padding: 2px 8px;
}
.toolbar .btn-group {
  margin-top: 0px;
  margin-left: 5px;
}
#maintoolbar {
  margin-bottom: -3px;
  margin-top: -8px;
  border: 0px;
  min-height: 27px;
  margin-left: 0px;
  padding-top: 11px;
  padding-bottom: 3px;
}
#maintoolbar .navbar-text {
  float: none;
  vertical-align: middle;
  text-align: right;
  margin-left: 5px;
  margin-right: 0px;
  margin-top: 0px;
}
.select-xs {
  height: 24px;
}
.pulse,
.dropdown-menu > li > a.pulse,
li.pulse > a.dropdown-toggle,
li.pulse.open > a.dropdown-toggle {
  background-color: #F37626;
  color: white;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
/** WARNING IF YOU ARE EDITTING THIS FILE, if this is a .css file, It has a lot
 * of chance of beeing generated from the ../less/[samename].less file, you can
 * try to get back the less file by reverting somme commit in history
 **/
/*
 * We'll try to get something pretty, so we
 * have some strange css to have the scroll bar on
 * the left with fix button on the top right of the tooltip
 */
@-moz-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-webkit-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-moz-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
@-webkit-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
/*properties of tooltip after "expand"*/
.bigtooltip {
  overflow: auto;
  height: 200px;
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
}
/*properties of tooltip before "expand"*/
.smalltooltip {
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
  text-overflow: ellipsis;
  overflow: hidden;
  height: 80px;
}
.tooltipbuttons {
  position: absolute;
  padding-right: 15px;
  top: 0px;
  right: 0px;
}
.tooltiptext {
  /*avoid the button to overlap on some docstring*/
  padding-right: 30px;
}
.ipython_tooltip {
  max-width: 700px;
  /*fade-in animation when inserted*/
  -webkit-animation: fadeOut 400ms;
  -moz-animation: fadeOut 400ms;
  animation: fadeOut 400ms;
  -webkit-animation: fadeIn 400ms;
  -moz-animation: fadeIn 400ms;
  animation: fadeIn 400ms;
  vertical-align: middle;
  background-color: #f7f7f7;
  overflow: visible;
  border: #ababab 1px solid;
  outline: none;
  padding: 3px;
  margin: 0px;
  padding-left: 7px;
  font-family: monospace;
  min-height: 50px;
  -moz-box-shadow: 0px 6px 10px -1px #adadad;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  border-radius: 2px;
  position: absolute;
  z-index: 1000;
}
.ipython_tooltip a {
  float: right;
}
.ipython_tooltip .tooltiptext pre {
  border: 0;
  border-radius: 0;
  font-size: 100%;
  background-color: #f7f7f7;
}
.pretooltiparrow {
  left: 0px;
  margin: 0px;
  top: -16px;
  width: 40px;
  height: 16px;
  overflow: hidden;
  position: absolute;
}
.pretooltiparrow:before {
  background-color: #f7f7f7;
  border: 1px #ababab solid;
  z-index: 11;
  content: "";
  position: absolute;
  left: 15px;
  top: 10px;
  width: 25px;
  height: 25px;
  -webkit-transform: rotate(45deg);
  -moz-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  -o-transform: rotate(45deg);
}
ul.typeahead-list i {
  margin-left: -10px;
  width: 18px;
}
ul.typeahead-list {
  max-height: 80vh;
  overflow: auto;
}
ul.typeahead-list > li > a {
  /** Firefox bug **/
  /* see https://github.com/jupyter/notebook/issues/559 */
  white-space: normal;
}
.cmd-palette .modal-body {
  padding: 7px;
}
.cmd-palette form {
  background: white;
}
.cmd-palette input {
  outline: none;
}
.no-shortcut {
  display: none;
}
.command-shortcut:before {
  content: "(command)";
  padding-right: 3px;
  color: #777777;
}
.edit-shortcut:before {
  content: "(edit)";
  padding-right: 3px;
  color: #777777;
}
#find-and-replace #replace-preview .match,
#find-and-replace #replace-preview .insert {
  background-color: #BBDEFB;
  border-color: #90CAF9;
  border-style: solid;
  border-width: 1px;
  border-radius: 0px;
}
#find-and-replace #replace-preview .replace .match {
  background-color: #FFCDD2;
  border-color: #EF9A9A;
  border-radius: 0px;
}
#find-and-replace #replace-preview .replace .insert {
  background-color: #C8E6C9;
  border-color: #A5D6A7;
  border-radius: 0px;
}
#find-and-replace #replace-preview {
  max-height: 60vh;
  overflow: auto;
}
#find-and-replace #replace-preview pre {
  padding: 5px 10px;
}
.terminal-app {
  background: #EEE;
}
.terminal-app #header {
  background: #fff;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.terminal-app .terminal {
  width: 100%;
  float: left;
  font-family: monospace;
  color: white;
  background: black;
  padding: 0.4em;
  border-radius: 2px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
}
.terminal-app .terminal,
.terminal-app .terminal dummy-screen {
  line-height: 1em;
  font-size: 14px;
}
.terminal-app .terminal .xterm-rows {
  padding: 10px;
}
.terminal-app .terminal-cursor {
  color: black;
  background: white;
}
.terminal-app #terminado-container {
  margin-top: 20px;
}
/*# sourceMappingURL=style.min.css.map */
    </style>
<style type="text/css">
    .highlight .hll { background-color: #ffffcc }
.highlight  { background: #f8f8f8; }
.highlight .c { color: #408080; font-style: italic } /* Comment */
.highlight .err { border: 1px solid #FF0000 } /* Error */
.highlight .k { color: #008000; font-weight: bold } /* Keyword */
.highlight .o { color: #666666 } /* Operator */
.highlight .ch { color: #408080; font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: #408080; font-style: italic } /* Comment.Multiline */
.highlight .cp { color: #BC7A00 } /* Comment.Preproc */
.highlight .cpf { color: #408080; font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: #408080; font-style: italic } /* Comment.Single */
.highlight .cs { color: #408080; font-style: italic } /* Comment.Special */
.highlight .gd { color: #A00000 } /* Generic.Deleted */
.highlight .ge { font-style: italic } /* Generic.Emph */
.highlight .gr { color: #FF0000 } /* Generic.Error */
.highlight .gh { color: #000080; font-weight: bold } /* Generic.Heading */
.highlight .gi { color: #00A000 } /* Generic.Inserted */
.highlight .go { color: #888888 } /* Generic.Output */
.highlight .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.highlight .gs { font-weight: bold } /* Generic.Strong */
.highlight .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.highlight .gt { color: #0044DD } /* Generic.Traceback */
.highlight .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: #008000 } /* Keyword.Pseudo */
.highlight .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: #B00040 } /* Keyword.Type */
.highlight .m { color: #666666 } /* Literal.Number */
.highlight .s { color: #BA2121 } /* Literal.String */
.highlight .na { color: #7D9029 } /* Name.Attribute */
.highlight .nb { color: #008000 } /* Name.Builtin */
.highlight .nc { color: #0000FF; font-weight: bold } /* Name.Class */
.highlight .no { color: #880000 } /* Name.Constant */
.highlight .nd { color: #AA22FF } /* Name.Decorator */
.highlight .ni { color: #999999; font-weight: bold } /* Name.Entity */
.highlight .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
.highlight .nf { color: #0000FF } /* Name.Function */
.highlight .nl { color: #A0A000 } /* Name.Label */
.highlight .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
.highlight .nt { color: #008000; font-weight: bold } /* Name.Tag */
.highlight .nv { color: #19177C } /* Name.Variable */
.highlight .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
.highlight .w { color: #bbbbbb } /* Text.Whitespace */
.highlight .mb { color: #666666 } /* Literal.Number.Bin */
.highlight .mf { color: #666666 } /* Literal.Number.Float */
.highlight .mh { color: #666666 } /* Literal.Number.Hex */
.highlight .mi { color: #666666 } /* Literal.Number.Integer */
.highlight .mo { color: #666666 } /* Literal.Number.Oct */
.highlight .sa { color: #BA2121 } /* Literal.String.Affix */
.highlight .sb { color: #BA2121 } /* Literal.String.Backtick */
.highlight .sc { color: #BA2121 } /* Literal.String.Char */
.highlight .dl { color: #BA2121 } /* Literal.String.Delimiter */
.highlight .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
.highlight .s2 { color: #BA2121 } /* Literal.String.Double */
.highlight .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
.highlight .sh { color: #BA2121 } /* Literal.String.Heredoc */
.highlight .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
.highlight .sx { color: #008000 } /* Literal.String.Other */
.highlight .sr { color: #BB6688 } /* Literal.String.Regex */
.highlight .s1 { color: #BA2121 } /* Literal.String.Single */
.highlight .ss { color: #19177C } /* Literal.String.Symbol */
.highlight .bp { color: #008000 } /* Name.Builtin.Pseudo */
.highlight .fm { color: #0000FF } /* Name.Function.Magic */
.highlight .vc { color: #19177C } /* Name.Variable.Class */
.highlight .vg { color: #19177C } /* Name.Variable.Global */
.highlight .vi { color: #19177C } /* Name.Variable.Instance */
.highlight .vm { color: #19177C } /* Name.Variable.Magic */
.highlight .il { color: #666666 } /* Literal.Number.Integer.Long */
    </style>
<style type="text/css">
    
/* Temporary definitions which will become obsolete with Notebook release 5.0 */
.ansi-black-fg { color: #3E424D; }
.ansi-black-bg { background-color: #3E424D; }
.ansi-black-intense-fg { color: #282C36; }
.ansi-black-intense-bg { background-color: #282C36; }
.ansi-red-fg { color: #E75C58; }
.ansi-red-bg { background-color: #E75C58; }
.ansi-red-intense-fg { color: #B22B31; }
.ansi-red-intense-bg { background-color: #B22B31; }
.ansi-green-fg { color: #00A250; }
.ansi-green-bg { background-color: #00A250; }
.ansi-green-intense-fg { color: #007427; }
.ansi-green-intense-bg { background-color: #007427; }
.ansi-yellow-fg { color: #DDB62B; }
.ansi-yellow-bg { background-color: #DDB62B; }
.ansi-yellow-intense-fg { color: #B27D12; }
.ansi-yellow-intense-bg { background-color: #B27D12; }
.ansi-blue-fg { color: #208FFB; }
.ansi-blue-bg { background-color: #208FFB; }
.ansi-blue-intense-fg { color: #0065CA; }
.ansi-blue-intense-bg { background-color: #0065CA; }
.ansi-magenta-fg { color: #D160C4; }
.ansi-magenta-bg { background-color: #D160C4; }
.ansi-magenta-intense-fg { color: #A03196; }
.ansi-magenta-intense-bg { background-color: #A03196; }
.ansi-cyan-fg { color: #60C6C8; }
.ansi-cyan-bg { background-color: #60C6C8; }
.ansi-cyan-intense-fg { color: #258F8F; }
.ansi-cyan-intense-bg { background-color: #258F8F; }
.ansi-white-fg { color: #C5C1B4; }
.ansi-white-bg { background-color: #C5C1B4; }
.ansi-white-intense-fg { color: #A1A6B2; }
.ansi-white-intense-bg { background-color: #A1A6B2; }

.ansi-bold { font-weight: bold; }

    </style>


<style type="text/css">
/* Overrides of notebook CSS for static HTML export */
body {
  overflow: visible;
  padding: 8px;
}

div#notebook {
  overflow: visible;
  border-top: none;
}@media print {
  div.cell {
    display: block;
    page-break-inside: avoid;
  } 
  div.output_wrapper { 
    display: block;
    page-break-inside: avoid; 
  }
  div.output { 
    display: block;
    page-break-inside: avoid; 
  }
}
</style>

<!-- Custom stylesheet, it must be in the same directory as the html file -->
<link rel="stylesheet" href="custom.css">

<!-- Loading mathjax macro -->
<!-- Load mathjax -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS_HTML"></script>
    <!-- MathJax configuration -->
    <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        tex2jax: {
            inlineMath: [ ['$','$'], ["\\(","\\)"] ],
            displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
            processEscapes: true,
            processEnvironments: true
        },
        // Center justify equations in code and markdown cells. Elsewhere
        // we use CSS to left justify single line equations in code cells.
        displayAlign: 'center',
        "HTML-CSS": {
            styles: {'.MathJax_Display': {"margin": 0}},
            linebreaks: { automatic: true }
        }
    });
    </script>
    <!-- End of mathjax configuration --></head>
<body>
  <div tabindex="-1" id="notebook" class="border-box-sizing">
    <div class="container" id="notebook-container">

<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Bayesian-inference">Bayesian inference<a class="anchor-link" href="#Bayesian-inference">&#182;</a></h1><p>Bayesian inference is a way to estimate parameters from your data using probability to account for uncertainty in these parameters.  These parameters could be the mean and variance of a Gaussian distribution fit to your dataset or they could be the intercept and slopes of a linear regression model.</p>
<p>There are <a href="https://www.datascience.com/blog/introduction-to-bayesian-inference-learn-data-science-tutorials">many</a> <a href="https://link.springer.com/article/10.3758/s13423-017-1262-3">interesting</a> <a href="https://www.youtube.com/watch?v=0LQmZXCWMFI">introductions</a> to the <a href="http://www.inference.org.uk/itila/">theory</a> behind Bayesian inference.</p>
<h2 id="Bayes-theorem,-briefly">Bayes theorem, briefly<a class="anchor-link" href="#Bayes-theorem,-briefly">&#182;</a></h2><p>Bayes theorem states that:
$$P(\theta | y,H) = \frac{P(y | \theta,H)P(\theta|H)}{P(y,H)}$$</p>
<p>where $\theta$ is a vector of parameters that we are trying to infer, $y$ is the data and $H$ is the set of hypotheses that we are using to build our probability model.  The physical meaning of the parameters $\theta$ depends on the problem that we are trying to solve.  They could be the mean and variance of a Gaussian distribution or they could be the intercept and slopes of a linear regression.</p>
<p>The goal of Bayesian inference is to estimate the left-hand side of Bayes theorem - this is referred to as the <em>posterior</em> distribution of the parameters given the data and model.  The first term above the line on the right hand side is the <em>likelihood</em> of the parameters.  This is where we assess how will given parameters fit the data. The second term above the line is the <em>prior</em> distribution of the parameters - this reflects our estimates for the parameters before we gather the data.  The term below the line is the <em>evidence</em> of the model. In the problem considered below this is simply a normalising constant and so we will not discuss it further.</p>
<p>In this notebook we look at a practical example of how Bayesian inference can go far beyond coin tosses to be of practical use in oceanography.  In particular, we'll try to characterise the variability in a dataset by fitting Bayesian models.  Subsequent workbooks will look at other problems such as making forecasts of time series.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Dataset">Dataset<a class="anchor-link" href="#Dataset">&#182;</a></h1><p>For this notebook, we use a central dataset in modern oceanography - the estimated Meridional Overturning Circulation in the Atlantic Ocean at 40N.  Our aim is to understand the variability in this time series by fitting statistical models to it.  Data from the RAPID-WATCH MOC monitoring project are funded by the Natural Environment Research Council and are freely available from <a href="www.rapid.ac.uk/rapidmoc">the RAPID website</a>.</p>
<p>Thanks RAPID people for gathering the data and making it so easy to download!</p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Software">Software<a class="anchor-link" href="#Software">&#182;</a></h1><p>The analysis will be carried out in python with the Bayesian inference carried out using the <a href="http://docs.pymc.io/">PyMC3</a> package.  We also use the <a href="http://xarray.pydata.org/en/stable/">xarray</a> package for easy handling of NetCDF files, <a href="http://pandas.pydata.org/">pandas</a> to make time series operations easier.  Thanks to all those who contributed to developing the open source packages used below.</p>
<p>All the necessary imports are set out in the cell below.  These packages can all be installed using 'conda install package_name'.  This notebook uses python 3.6.1.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[1]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="kn">import</span> <span class="nn">xarray</span> <span class="k">as</span> <span class="nn">xr</span>
<span class="kn">import</span> <span class="nn">pymc3</span> <span class="k">as</span> <span class="nn">pm</span>
<span class="kn">import</span> <span class="nn">theano</span>
<span class="kn">from</span> <span class="nn">scipy</span> <span class="k">import</span> <span class="n">signal</span>

<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="kn">import</span> <span class="nn">seaborn</span> <span class="k">as</span> <span class="nn">sns</span>

<span class="o">%</span><span class="k">matplotlib</span> inline
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Load-and-inspect-the-dataset">Load and inspect the dataset<a class="anchor-link" href="#Load-and-inspect-the-dataset">&#182;</a></h1><p>First, we load and inspect the dataset. I've saved it in a sub-directory called 'data', you'll need to add your own path to the data here if you are doing this interactively.  Loading the data is made very easy by the xarray package.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[2]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">ds</span> <span class="o">=</span> <span class="n">xr</span><span class="o">.</span><span class="n">open_dataset</span><span class="p">(</span><span class="s1">&#39;data/moc_transports.nc&#39;</span><span class="p">)</span>
<span class="n">ds</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt output_prompt">Out[2]:</div>




<div class="output_text output_subarea output_execute_result">
<pre>&lt;xarray.Dataset&gt;
Dimensions:       (time: 8419)
Coordinates:
  * time          (time) datetime64[ns] 2004-04-02 2004-04-02T12:00:00 ...
Data variables:
    t_therm10     (time) float64 -17.71 -17.47 -17.23 -17.02 -16.83 -16.68 ...
    t_aiw10       (time) float64 0.8188 0.828 0.8364 0.8424 0.8449 0.843 ...
    t_ud10        (time) float64 -7.654 -8.189 -8.696 -9.154 -9.549 -9.869 ...
    t_ld10        (time) float64 -3.4 -3.388 -3.368 -3.343 -3.316 -3.293 ...
    t_bw10        (time) float64 1.381 1.406 1.43 1.453 1.472 1.486 1.493 ...
    t_gs10        (time) float64 27.56 27.89 28.19 28.44 28.64 28.77 28.84 ...
    t_ek10        (time) float64 -1.006 -1.091 -1.174 -1.243 -1.282 -1.279 ...
    t_umo10       (time) float64 -16.89 -16.64 -16.39 -16.16 -15.96 -15.81 ...
    moc_mar_hc10  (time) float64 9.673 10.18 10.65 11.06 11.42 11.71 11.93 ...
Attributes:
    Title:                         RAPID MOC timeseries
    Institution:                   National Oceanography Centre,UK
    Website:                       http://www.rapid.ac.uk/rapidmoc
    Acknowledgement:               The RAPID-MOC monitoring project is funded...
    Created_by:                    Ben Moat and Gerard McCarthy
    Creation_date:                 27-Jun-2016
    Principle_investigator:        David Smeed
    Principle_investigator_email:  das@noc.ac.uk
    DOI:                           doi:10.5285/35784047-9b82-2160-e053-6c86ab...</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The dataset is a daily time series that comes with the total MOC (mon_mar_hc10) along with all the components that go into calculating the MOC (the variables beginning 't').  The units are in Sverdrups (= $10^{6}$ m$^{3}$ s$^{-1}$).</p>
<p>For clarity, we will extract the time variable and the MOC time series into a Pandas dataframe.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">DataFrame</span><span class="p">(</span><span class="n">data</span> <span class="o">=</span> <span class="n">ds</span><span class="o">.</span><span class="n">moc_mar_hc10</span><span class="o">.</span><span class="n">values</span><span class="p">,</span> <span class="n">index</span> <span class="o">=</span> <span class="n">ds</span><span class="o">.</span><span class="n">time</span><span class="o">.</span><span class="n">values</span><span class="p">,</span> <span class="n">columns</span><span class="o">=</span><span class="p">[</span><span class="s1">&#39;moc&#39;</span><span class="p">])</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Before inspecting the moc data we define the following function for time series plotting.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">time_plot</span><span class="p">(</span><span class="n">time</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">axkwargs</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;Function for time series plotting.</span>
<span class="sd">    </span>
<span class="sd">    t is the 1D time-axis data.</span>
<span class="sd">    y is the 1D y-axis data.</span>
<span class="sd">    axkwargs is a dictionary with keyword arguments for the axes e.g. axkwargs = {&#39;xlabel&#39;: &#39;Time&#39; }.</span>
<span class="sd">    args are optional arguments for the plotting routine e.g. &#39;--b&#39; for a dashed blue line.</span>
<span class="sd">    kwargs are optional keyword arguments for the plotting routine e.g. kwargs = {&#39;ls&#39;:&#39;--&#39;} for a dashed line.</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="n">fig</span><span class="p">,</span> <span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">(</span><span class="n">figsize</span> <span class="o">=</span> <span class="p">(</span><span class="mi">14</span><span class="p">,</span><span class="mi">6</span><span class="p">))</span>
    <span class="n">ax</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span><span class="n">time</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">tight_layout</span><span class="p">()</span>
    <span class="k">if</span> <span class="n">axkwargs</span><span class="p">:</span>
        <span class="n">ax</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="o">**</span><span class="n">axkwargs</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Now we plot the full MOC time series with units in Sverdrups.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">axkwargs</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;xlabel&#39;</span><span class="p">:</span> <span class="s1">&#39;Time (years)&#39;</span><span class="p">,</span> <span class="s1">&#39;ylabel&#39;</span><span class="p">:</span> <span class="s1">&#39;MOC (Sverdrups)&#39;</span><span class="p">,</span> <span class="s1">&#39;title&#39;</span><span class="p">:</span> <span class="s1">&#39;Full MOC time series&#39;</span><span class="p">}</span>
<span class="n">time_plot</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">index</span><span class="p">,</span> <span class="n">df</span><span class="o">.</span><span class="n">moc</span><span class="p">,</span> <span class="n">axkwargs</span> <span class="o">=</span> <span class="n">axkwargs</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Extracting-the-anomalies-from-the-full-time-series">Extracting the anomalies from the full time series<a class="anchor-link" href="#Extracting-the-anomalies-from-the-full-time-series">&#182;</a></h2><p>This plot of the full time series shows that the seasonal cycle accounts for a significant portion of the variability in the time series.  To understand the non-seasonal variability, we remove the seasonal cycle.  We take advantage of time series functionality in xaray to calculate a monthly-mean MOC climatology and then calculate the MOC anomaly with respect to this monthly mean.  We also remove the linear trend.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[6]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">moc_climatology</span> <span class="o">=</span> <span class="n">ds</span><span class="o">.</span><span class="n">moc_mar_hc10</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="s1">&#39;time.month&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">mean</span><span class="p">(</span><span class="s1">&#39;time&#39;</span><span class="p">)</span>
<span class="n">moc_anomalies</span> <span class="o">=</span> <span class="p">(</span><span class="n">ds</span><span class="o">.</span><span class="n">moc_mar_hc10</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="s1">&#39;time.month&#39;</span><span class="p">)</span> <span class="o">-</span> <span class="n">moc_climatology</span><span class="p">)</span><span class="o">.</span><span class="n">values</span>

<span class="n">df</span><span class="p">[</span><span class="s1">&#39;moc_anomalies&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">signal</span><span class="o">.</span><span class="n">detrend</span><span class="p">(</span><span class="n">moc_anomalies</span><span class="p">,</span> <span class="n">axis</span> <span class="o">=</span> <span class="mi">0</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>We plot the new time series for the MOC anomalies.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[7]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">axkwargs</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;xlabel&#39;</span><span class="p">:</span> <span class="s1">&#39;Time (years)&#39;</span><span class="p">,</span> <span class="s1">&#39;ylabel&#39;</span><span class="p">:</span> <span class="s1">&#39;MOC (Sverdrups)&#39;</span><span class="p">,</span> <span class="s1">&#39;title&#39;</span><span class="p">:</span> <span class="s1">&#39;MOC anomalies time series&#39;</span><span class="p">}</span>
<span class="n">time_plot</span><span class="p">(</span><span class="n">df</span><span class="o">.</span><span class="n">index</span> <span class="p">,</span><span class="n">df</span><span class="o">.</span><span class="n">moc_anomalies</span><span class="p">,</span> <span class="n">axkwargs</span><span class="o">=</span> <span class="n">axkwargs</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The data now captures the anomalies in the flow and is centered close to 0. We'd guess that the standard deviation is probably around 5 from the plot.</p>
<h1 id="Bayesian-model">Bayesian model<a class="anchor-link" href="#Bayesian-model">&#182;</a></h1><p>We would like to describe the variability in the dataset using a probability distribution function (PDF).  Our guess is that the variability can be described using a Gaussian distribution with mean $\mu$ and some unknown variance $\sigma^{2}$.  In terms of Bayes theorem as set out above the parameter vector $\theta = (\mu, \sigma)$ and <em>likelihood</em> function of the parameters is:</p>
<p>$$L(\mu,\sigma,y_{1},...y_{n}) = (2\pi\sigma)^{-n/2}\times \exp\Big(\frac{-1}{2\sigma^{2}} \Sigma_{j=1}^{n} (y_{j} - \mu)^{2}\Big)  $$</p>
<p>The next step after defining the model above is to set out prior distributions for $\mu$ and $\sigma^{2}$.</p>
<p>By inspecting the plot above, we can set a prior distribution for the mean $\mu$ as:</p>
<p>$\mu = N(0, 3^{2})$</p>
<p>This prior suggests that we expect the mean to be somewhere in the approximate range of -6 to +6. We use a mean of 0 in this distribution because the averaging we performed to remove the seasonal cycle should also remove the time-mean and leave us with an average close to 0.  In practice, the data will drive our final estimate of the mean $\mu$ rather than the details of this prior distribution.</p>
<p>We set a half-normal prior for the positive-definite variance $\sigma^{2}$ as:</p>
<p>$\sigma^{2} = N^{+}(10^{2})$</p>
<p>By allowing $\sigma^{2}$ to cover a relatively wide range of values we're really just making sure with this prior that any crazy-high values of the variance are ruled out letting the data drive the inference.</p>
<p>In terms of Bayes theorem as set out in the introduction above, the set of hypotheses $H$ combines the assumption that the likelihood is Gaussian, the assumption of a Gaussian distribution for $\mu$ and the assumption that of a half-Gaussian distribution for $\sigma$.</p>
<p>When fitting a statistical model, it's a good idea to split your data into a training set and a test set. This allows you to get an idea whether the model developed on the training set will work for out-of-sample data and so reduce <a href="https://www.coursera.org/learn/machine-learning/lecture/ACpTQ/the-problem-of-overfitting">overfitting</a>.
In this case we'll train the model on the data up to 2012 and test it on the period since then.  We'll take advantage of Pandas time series operations to make this split.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[8]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">moc_anomalies_train</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">df</span><span class="o">.</span><span class="n">index</span> <span class="o">&lt;</span> <span class="n">pd</span><span class="o">.</span><span class="n">datetime</span><span class="p">(</span><span class="mi">2013</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">),</span><span class="s1">&#39;moc_anomalies&#39;</span><span class="p">]</span>
<span class="n">moc_anomalies_test</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">loc</span><span class="p">[</span><span class="n">df</span><span class="o">.</span><span class="n">index</span> <span class="o">&gt;=</span> <span class="n">pd</span><span class="o">.</span><span class="n">datetime</span><span class="p">(</span><span class="mi">2013</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="mi">1</span><span class="p">),</span><span class="s1">&#39;moc_anomalies&#39;</span><span class="p">]</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Days in training set&quot;</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">moc_anomalies_train</span><span class="p">),</span> <span class="s2">&quot;, Days in test set&quot;</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">moc_anomalies_test</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Days in training set 6392 , Days in test set 2027
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Fitting-the-Bayesian-model">Fitting the Bayesian model<a class="anchor-link" href="#Fitting-the-Bayesian-model">&#182;</a></h1><p>We can now fit the Bayesian model to get probability distribution functions for $\mu$ and $\sigma$. To help with this, we define the following function for fitting the data with a Gaussian likelihood using PyMC3.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[9]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">gaussian_fit</span><span class="p">(</span><span class="n">data</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">mu_prior</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">sigma_prior</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;Fit the Gaussian model conditioned on the data</span>
<span class="sd">    </span>
<span class="sd">    data is the 1D training dataset</span>
<span class="sd">    mu_prior is a dictionary with the parameters of a Normal distribution e.g. mu_prior = {&#39;mean&#39;: 0, &#39;sd&#39;: 10}</span>
<span class="sd">    sigma_prior is a dictionary with the parameters of a Half-Normal distribution e.g. sigma_prior = {&#39;sd&#39;: 10}</span>
<span class="sd">    output: &#39;trace&#39; is the trace of the model fit, &#39;map_est&#39; is the estimates of the most likely values </span>
<span class="sd">    &quot;&quot;&quot;</span>

    <span class="k">with</span> <span class="n">pm</span><span class="o">.</span><span class="n">Model</span><span class="p">()</span> <span class="k">as</span> <span class="n">model</span><span class="p">:</span> 
        <span class="c1"># Specify priors</span>
        <span class="n">mu</span> <span class="o">=</span> <span class="n">pm</span><span class="o">.</span><span class="n">Normal</span><span class="p">(</span><span class="s1">&#39;mu&#39;</span><span class="p">,</span> <span class="n">mu</span> <span class="o">=</span> <span class="n">mu_prior</span><span class="p">[</span><span class="s1">&#39;mean&#39;</span><span class="p">],</span> <span class="n">sd</span> <span class="o">=</span> <span class="n">mu_prior</span><span class="p">[</span><span class="s1">&#39;sd&#39;</span><span class="p">])</span> <span class="c1">#Specify the standard deviation rather than the variance</span>
        <span class="n">sigma</span> <span class="o">=</span> <span class="n">pm</span><span class="o">.</span><span class="n">HalfNormal</span><span class="p">(</span><span class="s1">&#39;sigma&#39;</span><span class="p">,</span> <span class="n">sd</span> <span class="o">=</span> <span class="n">sigma_prior</span><span class="p">[</span><span class="s1">&#39;sd&#39;</span><span class="p">])</span>
        <span class="c1"># Specify likelihood and feed in data from </span>
        <span class="n">Y_obs</span> <span class="o">=</span> <span class="n">pm</span><span class="o">.</span><span class="n">Normal</span><span class="p">(</span><span class="s1">&#39;Y_obs&#39;</span><span class="p">,</span> <span class="n">mu</span> <span class="o">=</span> <span class="n">mu</span><span class="p">,</span> <span class="n">sd</span> <span class="o">=</span> <span class="n">sigma</span><span class="p">,</span> <span class="n">observed</span> <span class="o">=</span> <span class="n">data</span><span class="p">)</span>
        <span class="n">trace</span> <span class="o">=</span> <span class="n">pm</span><span class="o">.</span><span class="n">sample</span><span class="p">(</span><span class="n">draws</span> <span class="o">=</span> <span class="mi">500</span><span class="p">)</span>
        <span class="n">train_samples</span> <span class="o">=</span> <span class="n">pm</span><span class="o">.</span><span class="n">sample_ppc</span><span class="p">(</span><span class="n">trace</span><span class="o">=</span><span class="n">trace</span><span class="p">,</span><span class="n">model</span><span class="o">=</span><span class="n">model</span><span class="p">)</span>
        <span class="n">map_est</span> <span class="o">=</span> <span class="n">pm</span><span class="o">.</span><span class="n">find_MAP</span><span class="p">(</span><span class="n">model</span> <span class="o">=</span> <span class="n">model</span><span class="p">)</span>
        <span class="n">waic</span> <span class="o">=</span> <span class="n">pm</span><span class="o">.</span><span class="n">waic</span><span class="p">(</span><span class="n">trace</span><span class="p">,</span> <span class="n">n_eff</span><span class="o">=</span> <span class="kc">True</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">trace</span><span class="p">,</span> <span class="n">train_samples</span><span class="p">,</span> <span class="n">map_est</span><span class="p">,</span> <span class="n">waic</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>We can now infer the parameters $\mu$ and $\sigma$ using this model.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[10]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">mu_prior</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;mean&#39;</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span> <span class="s1">&#39;sd&#39;</span><span class="p">:</span> <span class="mi">3</span><span class="p">}</span>
<span class="n">sigma_prior</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;sd&#39;</span><span class="p">:</span> <span class="mi">10</span><span class="p">}</span>
<span class="n">trace</span><span class="p">,</span><span class="n">train_samples</span><span class="p">,</span> <span class="n">map_est</span><span class="p">,</span> <span class="n">waic</span> <span class="o">=</span> <span class="n">gaussian_fit</span><span class="p">(</span><span class="n">data</span> <span class="o">=</span> <span class="n">moc_anomalies_train</span><span class="p">,</span> <span class="n">mu_prior</span> <span class="o">=</span> <span class="n">mu_prior</span><span class="p">,</span> <span class="n">sigma_prior</span> <span class="o">=</span> <span class="n">sigma_prior</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stderr output_text">
<pre>Auto-assigning NUTS sampler...
Initializing NUTS using advi...
Average ELBO = -18,099: 100%|██████████| 200000/200000 [00:20&lt;00:00, 9890.21it/s] 
Finished [100%]: Average ELBO = -18,099
100%|██████████| 500/500 [00:01&lt;00:00, 428.48it/s]
100%|██████████| 500/500 [00:02&lt;00:00, 221.25it/s]
</pre>
</div>
</div>

<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Optimization terminated successfully.
         Current function value: 18093.341148
         Iterations: 11
         Function evaluations: 16
         Gradient evaluations: 16
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>We can view the output by using PyMC3's built-in traceplot function.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[11]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">pm</span><span class="o">.</span><span class="n">traceplot</span><span class="p">(</span> <span class="n">trace</span> <span class="p">);</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
/wJPZ1ps+LhwswAAAABJRU5ErkJggg==
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>The left-hand panels show the probability distribution functions (PDF) for the parameters $\mu$ and $\sigma$ of the assumed normal distribution for the MOC variability.</p>
<p>The PDF for $\mu$ has low negative values with a low spread.  We expect the mean anomaly to have an average close to 0 Sv over long periods and so this distribution makes sense physically.</p>
<p>Of more interest is the PDF for the standard deviation $\sigma$.  The plot suggests that the variability has a standard deviation has a PDF centered at 4.1 with most of the probability mass in the range from 4.0 to 4.2.</p>
<p>The right hand panels show the 500 individual samples that underlie the PDFs in the left-hand panels.  As all of the samples are in the same range, it does not seem like we have to reject any samples as part of an initial burn-in period.</p>
<p>We can get numeric summaries of this data using PyMC3's summary function on the trace.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[12]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">pm</span><span class="o">.</span><span class="n">summary</span><span class="p">(</span><span class="n">trace</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>
mu:

  Mean             SD               MC Error         95% HPD interval
  -------------------------------------------------------------------
  
  -0.248           0.052            0.003            [-0.350, -0.148]

  Posterior quantiles:
  2.5            25             50             75             97.5
  |--------------|==============|==============|--------------|
  
  -0.349         -0.287         -0.247         -0.213         -0.146


sigma:

  Mean             SD               MC Error         95% HPD interval
  -------------------------------------------------------------------
  
  4.103            0.034            0.002            [4.042, 4.169]

  Posterior quantiles:
  2.5            25             50             75             97.5
  |--------------|==============|==============|--------------|
  
  4.030          4.079          4.102          4.126          4.165

</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Evaluating-the-model">Evaluating the model<a class="anchor-link" href="#Evaluating-the-model">&#182;</a></h2><p>While we can always fit the model, the crucial step is evaluating the fit in order to understand where the model fails and how we might improve it.  We can first compare the statistical distribution of the observations from the training set with the simulated data. To do so we first define the following plotting function.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[13]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">compare_distributions</span><span class="p">(</span><span class="n">train_data</span><span class="p">,</span> <span class="n">simulated_train_data</span><span class="p">,</span> <span class="n">test_data</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">simulated_test_data</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;Compare the distributions of the actual and simulated data</span>
<span class="sd">    </span>
<span class="sd">        All inputs are 1d arrays.</span>
<span class="sd">        train_data is the actual data for the training period.</span>
<span class="sd">        simulated_train_data is the simulated data with the model for the training period.</span>
<span class="sd">        Test data can also be added optionally.</span>
<span class="sd">        test_data is the actual data for the testing period.</span>
<span class="sd">        simulated_test_data is the simulated data with the model for the testing period</span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="n">args</span> <span class="o">=</span> <span class="nb">locals</span><span class="p">()</span>
    <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">args</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">assert</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">ndarray</span><span class="p">,</span><span class="n">pd</span><span class="o">.</span><span class="n">Series</span><span class="p">,)),</span><span class="s1">&#39;</span><span class="si">{}</span><span class="s1"> should be a numpy array or a pandas Series, but is type </span><span class="si">{}</span><span class="s1">&#39;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">key</span><span class="p">,</span><span class="nb">type</span><span class="p">(</span><span class="n">value</span><span class="p">))</span>
        <span class="k">except</span><span class="p">:</span> <span class="c1"># For the NoneType optional arguments </span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">value</span><span class="p">:</span>
                <span class="k">pass</span>
    <span class="c1"># Add two subplots if we have test data as well</span>
    <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">test_data</span><span class="p">,</span> <span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">ndarray</span><span class="p">,</span> <span class="n">pd</span><span class="o">.</span><span class="n">Series</span><span class="p">)):</span>
        <span class="n">ncols</span> <span class="o">=</span> <span class="mi">2</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">ncols</span> <span class="o">=</span> <span class="mi">1</span>
    <span class="n">fig</span><span class="p">,</span> <span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">(</span><span class="n">nrows</span> <span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">ncols</span> <span class="o">=</span> <span class="n">ncols</span><span class="p">,</span> <span class="n">figsize</span> <span class="o">=</span> <span class="p">(</span><span class="mi">14</span><span class="p">,</span><span class="mi">7</span><span class="p">))</span>
    <span class="c1"># Make ax into an np.ndarray when there is only one subplot</span>
    <span class="k">if</span> <span class="n">ncols</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span>
        <span class="n">ax</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">([</span> <span class="n">ax</span> <span class="p">])</span>
    <span class="n">sns</span><span class="o">.</span><span class="n">kdeplot</span><span class="p">(</span><span class="n">train_data</span><span class="p">,</span> <span class="n">color</span> <span class="o">=</span> <span class="s1">&#39;b&#39;</span><span class="p">,</span><span class="n">ax</span> <span class="o">=</span> <span class="n">ax</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">label</span> <span class="o">=</span> <span class="s1">&#39;Actual data&#39;</span><span class="p">)</span>
    <span class="n">sns</span><span class="o">.</span><span class="n">kdeplot</span><span class="p">(</span><span class="n">simulated_train_data</span><span class="p">,</span><span class="n">color</span> <span class="o">=</span> <span class="s1">&#39;red&#39;</span><span class="p">,</span><span class="n">ax</span> <span class="o">=</span> <span class="n">ax</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">label</span> <span class="o">=</span> <span class="s1">&#39;Simulated data&#39;</span><span class="p">)</span>
    <span class="n">ax</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">legend</span><span class="p">()</span>
    <span class="n">ax</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s1">&#39;Histograms of actual and simulated values in the train period&#39;</span><span class="p">)</span>
    <span class="n">ax</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">set_xlabel</span><span class="p">(</span><span class="s1">&#39;MOC anomalies (Sverdrups)&#39;</span><span class="p">)</span>

    <span class="k">if</span> <span class="n">ncols</span> <span class="o">==</span> <span class="mi">2</span><span class="p">:</span>
        <span class="n">sns</span><span class="o">.</span><span class="n">kdeplot</span><span class="p">(</span><span class="n">test_data</span><span class="p">,</span> <span class="n">color</span> <span class="o">=</span> <span class="s1">&#39;b&#39;</span><span class="p">,</span><span class="n">ax</span> <span class="o">=</span> <span class="n">ax</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
        <span class="n">sns</span><span class="o">.</span><span class="n">kdeplot</span><span class="p">(</span><span class="n">simulated_test_data</span><span class="p">,</span><span class="n">color</span> <span class="o">=</span> <span class="s1">&#39;red&#39;</span><span class="p">,</span><span class="n">ax</span> <span class="o">=</span> <span class="n">ax</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
        <span class="n">ax</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s1">&#39;Histograms of actual and simulated values in the test period&#39;</span><span class="p">)</span>
        <span class="n">ax</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">set_xlabel</span><span class="p">(</span><span class="s1">&#39;MOC anomalies (Sverdrups)&#39;</span><span class="p">)</span>

    <span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[14]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">compare_distributions</span><span class="p">(</span><span class="n">moc_anomalies_train</span><span class="p">,</span> <span class="n">train_samples</span><span class="p">[</span><span class="s1">&#39;Y_obs&#39;</span><span class="p">][:,</span><span class="mi">0</span><span class="p">])</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
REREKt7/AzR87qYZb7/EAAAAAElFTkSuQmCC
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>This comparison shows that the model fit in red has a peak at more negative values. The model predicts larger values in the right tail and does not capture the extremes in the left tail.</p>
<p>The next stage in evaluating the model is to test the fit on out-of-sample data. We can compare the performance of the model between the training data (left) and the out-of-sample test data in the plots below.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[15]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">compare_distributions</span><span class="p">(</span><span class="n">moc_anomalies_train</span><span class="p">,</span> <span class="n">train_samples</span><span class="p">[</span><span class="s1">&#39;Y_obs&#39;</span><span class="p">][:,</span><span class="mi">0</span><span class="p">],</span>
                     <span class="n">moc_anomalies_test</span><span class="p">,</span> <span class="n">train_samples</span><span class="p">[</span><span class="s1">&#39;Y_obs&#39;</span><span class="p">][:,</span><span class="mi">0</span><span class="p">])</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Gaussian-model-evaluation">Gaussian model evaluation<a class="anchor-link" href="#Gaussian-model-evaluation">&#182;</a></h3><p>The plots suggest that the model fit does less well in the test period than in the period for which it has been trained - a common phenomenon!  In particular, the tails of the model fit are too large on both sides.  This mismatch tells us that the model may be predicting larger variability than we should expect in practice. We can see that the simulated data is too far to the left in the test period.</p>
<p>The fundamental problem may be that the Gaussian model struggling to fit the large negative values in 2009/2010.  The consequence of this in the test period - when variability was less extreme - is that the simulated data has too much variance on the left-hand side.</p>
<p>The issue here may be that the variability is not Gaussian, and so the Gaussian model is being stretched when we try to fit it to the data.  We investigate whether we can do better than this by fitting the data to a Student-t distribution instead.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[16]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">student_t_fit</span><span class="p">(</span><span class="n">train_data</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">degrees_of_freedom_prior</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
                             <span class="n">mu_prior</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">scale_prior</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;Fit the Student-t model conditioned on the data</span>
<span class="sd">    </span>
<span class="sd">    train_data is the 1D training dataset</span>
<span class="sd">    degrees_of_freedom is a dictionary with the parameters of a Uniform distribution e.g. = {&#39;low&#39;: 0, &#39;high&#39;: 100}</span>
<span class="sd">    scale_prior is a dictionary with the parameters of a Half-Normal distribution e.g. scale_prior = {&#39;sd&#39;: 10}</span>
<span class="sd">    output: &#39;trace&#39; is the trace of the model fit, &#39;map_est&#39; is the estimates of the most likely values </span>
<span class="sd">    &quot;&quot;&quot;</span>
    <span class="c1"># In order to train the model with train_data and test the model with test_data, we need to create a special type of </span>
    <span class="c1"># &#39;shared&#39; theano array</span>
    <span class="n">observed</span> <span class="o">=</span> <span class="n">theano</span><span class="o">.</span><span class="n">shared</span><span class="p">(</span><span class="n">train_data</span><span class="p">)</span>
    <span class="k">with</span> <span class="n">pm</span><span class="o">.</span><span class="n">Model</span><span class="p">()</span> <span class="k">as</span> <span class="n">model</span><span class="p">:</span> <span class="c1">#Specify priors</span>
        <span class="n">mu</span> <span class="o">=</span> <span class="n">pm</span><span class="o">.</span><span class="n">Normal</span><span class="p">(</span><span class="s1">&#39;mu&#39;</span><span class="p">,</span> <span class="n">mu</span> <span class="o">=</span> <span class="n">mu_prior</span><span class="p">[</span><span class="s1">&#39;mean&#39;</span><span class="p">],</span> <span class="n">sd</span> <span class="o">=</span> <span class="n">mu_prior</span><span class="p">[</span><span class="s1">&#39;sd&#39;</span><span class="p">])</span> <span class="c1">#Specify the standard deviation rather than the variance</span>
        <span class="n">lam</span> <span class="o">=</span> <span class="n">pm</span><span class="o">.</span><span class="n">HalfNormal</span><span class="p">(</span><span class="s1">&#39;sigma&#39;</span><span class="p">,</span> <span class="n">sd</span> <span class="o">=</span> <span class="n">scale_prior</span><span class="p">[</span><span class="s1">&#39;sd&#39;</span><span class="p">])</span>
        <span class="n">df</span> <span class="o">=</span> <span class="n">pm</span><span class="o">.</span><span class="n">Uniform</span><span class="p">(</span><span class="s1">&#39;df&#39;</span><span class="p">,</span> <span class="n">degrees_of_freedom_prior</span><span class="p">[</span><span class="s1">&#39;low&#39;</span><span class="p">],</span> <span class="n">degrees_of_freedom_prior</span><span class="p">[</span><span class="s1">&#39;high&#39;</span><span class="p">])</span>
        
        <span class="n">Y_obs</span> <span class="o">=</span> <span class="n">pm</span><span class="o">.</span><span class="n">StudentT</span><span class="p">(</span><span class="s1">&#39;Y_obs&#39;</span><span class="p">,</span> <span class="n">mu</span> <span class="o">=</span> <span class="n">mu</span><span class="p">,</span> <span class="n">lam</span> <span class="o">=</span> <span class="n">lam</span><span class="p">,</span> <span class="n">nu</span> <span class="o">=</span> <span class="n">df</span><span class="p">,</span> <span class="n">observed</span> <span class="o">=</span> <span class="n">observed</span><span class="p">)</span>
        
        <span class="n">trace</span> <span class="o">=</span> <span class="n">pm</span><span class="o">.</span><span class="n">sample</span><span class="p">(</span><span class="n">draws</span> <span class="o">=</span> <span class="mi">1000</span><span class="p">)</span>
        <span class="n">train_samples</span> <span class="o">=</span> <span class="n">pm</span><span class="o">.</span><span class="n">sample_ppc</span><span class="p">(</span><span class="n">trace</span> <span class="o">=</span> <span class="n">trace</span><span class="p">,</span> <span class="n">model</span> <span class="o">=</span> <span class="n">model</span><span class="p">)</span>
        <span class="n">map_est</span> <span class="o">=</span> <span class="n">pm</span><span class="o">.</span><span class="n">find_MAP</span><span class="p">(</span><span class="n">model</span> <span class="o">=</span> <span class="n">model</span><span class="p">)</span>
        <span class="n">waic_train</span> <span class="o">=</span> <span class="n">pm</span><span class="o">.</span><span class="n">waic</span><span class="p">(</span><span class="n">trace</span><span class="p">,</span> <span class="n">n_eff</span><span class="o">=</span> <span class="kc">True</span><span class="p">)</span>

    <span class="k">return</span> <span class="n">trace</span><span class="p">,</span> <span class="n">train_samples</span><span class="p">,</span> <span class="n">map_est</span><span class="p">,</span> <span class="n">waic_train</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>We can now fit the model where the likelihood is based on a Student-t distribution.  We use the same priors for the location $\mu$ and scale $\sigma$ parameters.  The key parameter for a Student-t distribution, however, is the degrees of freedom characterising the distribution.  For this we choose a uniform prior over a large range from 0 to 100.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[17]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">mu_prior</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;mean&#39;</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span> <span class="s1">&#39;sd&#39;</span><span class="p">:</span> <span class="mi">10</span><span class="p">}</span>
<span class="n">scale_prior</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;sd&#39;</span><span class="p">:</span> <span class="mi">10</span><span class="p">}</span>
<span class="n">degrees_of_freedom_prior</span> <span class="o">=</span> <span class="p">{</span><span class="s1">&#39;low&#39;</span><span class="p">:</span><span class="mi">0</span><span class="p">,</span> <span class="s1">&#39;high&#39;</span><span class="p">:</span><span class="mi">100</span><span class="p">}</span>

<span class="n">trace_student</span><span class="p">,</span><span class="n">train_samples_student</span><span class="p">,</span> <span class="n">map_est_student</span><span class="p">,</span> <span class="n">waic_train_student</span> <span class="o">=</span> <span class="n">student_t_fit</span><span class="p">(</span>
    <span class="n">train_data</span> <span class="o">=</span> <span class="n">moc_anomalies_train</span><span class="o">.</span><span class="n">values</span><span class="p">,</span>
    <span class="n">degrees_of_freedom_prior</span> <span class="o">=</span> <span class="n">degrees_of_freedom_prior</span><span class="p">,</span> <span class="n">mu_prior</span> <span class="o">=</span> <span class="n">mu_prior</span><span class="p">,</span> <span class="n">scale_prior</span> <span class="o">=</span> <span class="n">scale_prior</span>
<span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stderr output_text">
<pre>Auto-assigning NUTS sampler...
Initializing NUTS using advi...
Average ELBO = -18,041: 100%|██████████| 200000/200000 [00:42&lt;00:00, 4652.63it/s]
Finished [100%]: Average ELBO = -18,041
100%|██████████| 1000/1000 [00:06&lt;00:00, 151.48it/s]
100%|██████████| 1000/1000 [00:04&lt;00:00, 230.60it/s]
</pre>
</div>
</div>

<div class="output_area">

<div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Optimization terminated successfully.
         Current function value: 18034.629856
         Iterations: 36
         Function evaluations: 62
         Gradient evaluations: 62
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>As for the Gaussian model, we can inspect the model fit using the <em>traceplot</em> function.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[18]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">pm</span><span class="o">.</span><span class="n">traceplot</span><span class="p">(</span> <span class="n">trace_student</span> <span class="p">);</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA1gAAAGoCAYAAABbkkSYAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz
AAALEgAACxIB0t1+/AAAIABJREFUeJzsvXeYY2d5sH8fdWk0mt6293d3ba8rtsEYMMXBGBsHk5gW
aoAESPJ9IfVLJSRX+JHvg4QEQgjNEBKKjQFTbFwAGxvbrO3d9bZ3e5nd2ekzmhmNRu38/lCZo6Mj
6UgjjWZm3/u6Zlc6OuU57zlHep73aZqu6ygUCoVCoVAoFAqFYuE4Gi2AQqFQKBQKhUKhUKwUlIGl
UCgUCoVCoVAoFDVCGVgKhUKhUCgUCoVCUSOUgaVQKBQKhUKhUCgUNUIZWAqFQqFQKBQKhUJRI5SB
pVAoFAqFQqFQKBQ1QhlYCoVCoVAoFAqFQlEjlIGlUCgUCoVCoVAoFDXC1WgBFIqLHSHEBuCXwKeA
9wIa8A7gr4ArgAeBrwJfkFJuyWzzCuN7hUKhUCgWC/W7pVCURnmwFIqlQSdwQUopgH3AN4F3AruA
twKbGyibQqFQKBRm1O+WQlEE5cFSKJYGLuDbmdcvAEgpRwCEEAPAqgbJpVAoFAqFFep3S6EogvJg
KRRLg6SUcjb7Gpg2fgY8vvgiKRQKhUJRFPW7pVAUQRlYCsXy4EbAaXjf1ihBFAqFQqGwgfrdUly0
qBBBhWJ5MAD0CSG6gVHgbQ2WR6FQKBSKUqjfLcVFi/JgKRTLg2PAl4DngV8AjzRWHIVCoVAoSqJ+
txQXLZqu642WQaFQKBQKhUKhUChWBMqDpVAoFAqFQqFQKBQ1QhlYCoVCoVAoFAqFQlEjlIGlUCgU
CoVCoVAoFDVCGVgKhUKhUCgUCoVCUSOWZZn24eEpVZlDoVAoVhBdXc1ao2WoN7X47WprCzA+HqmF
OCsCNR75qPHIR41HPmo88qnFeBT77VIeLIVCoVAolgkul7P8ShcRajzyUeORjxqPfNR45FPP8VAG
lkKhUCgUCoVCoVDUCGVgKRQKhUKhUCgUCkWNqHsOlhDiK8A7TYs3SilPZT43x6TfIqV8oN5yKRQK
SOk6AyMzHO2f5OzwNGOTUcan5piLJ3G7HHS1+ulpC7Chr5lLNrbT5HM3WmSFQqFQLDL7T46STOpc
vqWz0aIoFMuCxShy8QHgw5nXHwJ+G+g3rfM64PHM69lFkEmhuCiJxZOcHAhz7NwkR/snOX5ukplo
Im8dr9uJz+tkciZG//BMbrnToXHlti5ee+06Nq0KLbboCoVCoWgQ07PxRougUCwr6m5gSSnngDkh
RCvwx8AfSCkTptVmpZTT9ZZFobiY0HWd8am5nEF1rH+SUxemSKbmncZdrT52be5k65oWNvaF6Gz1
EfC60DQNXdeZisS5MBZBnhnnmUND7D6c/rtGdPGWV2+jrdnbwDNUKBQKhUKhWHosZpn2DwNTwDcs
PvtHIUQvaS/WB5WxpVDYZy6eZHQyymg4yuhklJHJKP3D05waCBOOzM86OjSN9b1BtqxuZeuaFras
aaE1WNxA0jSNUJOHUJOHbWtbef1LNnD4zAT3PXaC3XKYA6fG+e1bd3Dltq7FOE2FQqFQKBSKZcGi
GFhCCCdpA+tTUsqk6eO7gUeBE8ADgAT+YTHkUiiWA6mUztDELBdGI4yGo4xMzuYMqpHJKFMR69CN
jpCPq0UrG3qb2bSqhU19Ibye6kuSaprGjvVtiLdfxWN7zvONR47yr995gV+/cSOvf8kGNG3FtzFS
XGQIIT4N/BYwBLxbSvmk4bNfAz4LtAGfkVL+VWOkVCgWj5Su41Df9QpFWRbLg3UD0APcb/5ASvmu
7GshxH5gxyLJpFAsSSam5zh8Zpxj/ZMcPxfm/OgM8USqYD2X00FHyMu67iAdLT46Qj46W/x0tPjo
7QgQCnjqIp9D03jFlavZvLqFT9+zj/seP0l4Js5bX7NVGVmKFYMQ4tWkJwavJ51L/FngisxnGvAF
4NvAj4CHhBD3Sin3NEhchWJRSKV0HM7GfM8nkilcTlX8WrE8WEwDa1pKeRBACOEHdGA98DzwHuAA
cAlwzyLJpFAsGaYiMZ4+OMjuw0Mc7Z8kmyXlcjpY3dnE6q4m+joCdLX6M4aUj+YmT0NnEtd2B/mL
d1zNJ7+5l0eeS9etUUaWYgXxCuCslPIZIcRa4D1CiHYp5RiwGVgD3C+l/KkQYhq4CVAGlmJFo+vm
ws+LQySaYN+JEfram1jf29wQGRSVMzwxi9/rIui/+CoQL5aBtQq4YHj/Y2BCSnmHEOJvgX8BPKSN
q88skkwKRcMZGJ3hod39PPnCALFECg3YuraVy7d0sHVNK+t7mnG7lu6MXWvQyx+/5Qr+6X+e55Hn
+mkLeXnd9esbLZZCUQt6gMnM6/HM/73AWOYzTJ/3LZ5oCkVjSKZ0GqEqhyMxAAbGZpSBtUxIplIc
P5/+irx+Z29F28YTSeIJnYCvcjNlejaOz+NsuLdzUQwsKeXvmd6/wvD6E8AnFkMOhWKpMD0b5zs/
P87P95xHBzpbfLzq6jVct7OnZOGJpUhzwMMf3nUFH7t7N/f+7Di97QGuUoUvFIoC2toCuFzV50Fm
6eqqnYIZnUswF0/Sssy+d4zUcjxWAvUYj1BzWlFubw/S1ABvRAyNsZl0vnGl59eo+2P3oUFagh62
rm1ryPGLsVjjkUimCDVPVXXMn2eiYl5+1ZqKtovOJTh4dhKvx8n1l9qb86rXeCxmFUGF4qJH13Ue
23uee352nJlogr6OAHfcuImrtnXidCxdT1U5WoNe/uBNu/jH/3qOz99/gD9/29VqllGx3BkAWjOv
s91Vzxs+A2jN5GN1GD4ryvh4ZMFCdXU1Mzw8teD9ZHnqYDq45KqtXXjcCzf+ShGNJTg1MMXGVSG8
NTpWrcdjOZLSdZLJFG6Xs27jEZ5KtygdGp5qSLjX2FgkJ0Ml59fI+2NgKMzAELTa9MLEEymGJmbp
afPXzfuymOORSKaqumZA1dvNziWKbjsWjuL1OGnyzd+/tRiPYgba8tXoFIplxvRsnH/7zgvc/YAk
mdJ58yu38NH3XMuLtncva+Mqy7qeZt5/207i8RT/9p0XiERVY0rFsuZhYK0Q4nrg9cCvSPd09Ekp
T5CufHs7cAsQAB5qmKQ1IJGsf27NkbMTTMzMcc7QwFyxcE6cD/PskWHm4uYizbUn1aAcrIuBkwNh
zg5NqefDwEJy/hLJ+eJguq5zpH+CF06M1kIsWyx/rU6hWAYc7Z/gb770DM8fHWH7ulb+4X3Xc/O1
6xoeI1xrrtzWxW03bGA0HOWrD8qGJUQrFAtFSvkY8EnSVQKvAj5IOn8428vxfaQNr7uBv5BSHmiE
nLWj/s9qZC4BsKTzSpcjI5PpGfvxqbn6H6xBX+nL7bfEjry6rnP83CThmXR+2Wzm+bBrKA+ORxbF
qF5OGIc9O66NQoUIKhR15qkDF/jSjw6RSsEbX7aJ112/Hodj5Vbau+2GDRw8Pc4zh4a4ZGM7N+5a
1WiRFIqqkFJ+BPiIYdErDJ89CmxZbJnqxWKqr64GlfleLKZn4zg0raoE/YVQSqnXdZ1zIzO0N3sJ
+KoP8Vtuhs5SZnImxvDkLMOTs3lFIOwU4h2fmuPkQBifx8UVWzrLb7BM0YHKvi3m789kSrdYunio
aSSFok7ous79T5zk8/cfxO1y8L/vupzXv2TDijauAJwOB++/bSd+r4uvP3SEC2MLzztRKOwihLhU
CHFH5nVrufUvZhqlLKcW8bCRaBx5ZnxRZ7P3nxxl34mRRTtellItMsIzMfqHp9m3wBCpYpcuGksw
MZ32oI1PzTE9mx8iPhWJcfDUWMO9CouFnVs8ZXoQzNv0D0/z/JFhy7DMaCyR978ijXGkzOO72CgD
S6GoA7qu881Hj3Hf4yfpCPn4P2+/mks2tDdarEWjs8XPO18riMVTfPGHBxv+Rae4OBBC/G/gS8BH
M4v+Sgjxlw0UaUljfCoX09ZaTMPuwtgs49NznBlc+YUwSo1rrXLsih1iz7ERDp8ZJ5FMIc+Os/9k
viE3ND5LOBKryXWYicY5cnYiL8dmJaFlfDb9w9PMJZLMxQrDABcjZ3Kh1OQxr3AfxmOevBCeD6Fs
wHApA0uhqDG6rvM/jxzlJ786S19HgL94x9Ws7go2WqxF59odPbxoezfHz4V5+Nn+RoujuDh4C3A9
6V5VAH9MOk9KYYVB6bBSzuOJZE2MoZSuMxaOGo5VuM7+E6McOTux4GOZySrhSYtJnpSuXzRFG/Qa
aZjl7odiRo8zExaazcNbCIdOjTM2FV3a0RHVDHcF2yRT6XF2LcMCWeNTcxw5O2Hr2VvofTsdSXtS
s97VxWT5XRmFYgmTNa4e3t3P6s4m/uStVy27vla15G03byPod/Odnx9nsAYlqhWKMkxJKXMaXub1
ypzmrgFGBcesxszFkzx7ZBh5ZuFGz4lzYY70z+/HyqM9HY0zNhUtWF6KuXiSfceG2X9ylHMj1pXX
sgaBOTQ7mUrx/JER9h4dWTFGVslAgUU6xWLRClmvTC3GOmssr5DLVoiNLIKsB8u5pFMOrC+QPJs2
kCPRtLHdPzyd82zOxZIcPzdZsM2xc5M8dfBC2WgY8wRA1kAzfv8sFsrAUihqyA9+eTpnXP3xW66k
pcnTaJEaSijg4W2v2UYskeLLPzq8YhQZxZLluBDib4A2IcQbhRDfBA42WqilSt7jaHo0sxXNJmYW
PvM7Gs43nGr1PXB2cJrxcDrf5+yQdehZVh9zmPKTJqZixJNJ5hJJkssg3MoWpYpc1OgQ5a6dlafw
YsTseUkkU4QjpfPPstvYMZmKTRzA8imlnxW9f3ia86PpCZLDZ8YZzlTFhPlbOlspM+u5K0bBmVsM
xWKNjzKwFIoa8fi+89z32Ak6Qj7+8K4rCF3kxlWWa3d0c+XWTo6cneAX+wbKb6BQVM+HgBngHPB2
4OnMMoUlhR6seuRHmZXNWh3CjqKUXcdc/yG5TJTQSih1RjULpyszbIuZb5tK6ew/OcpQDaMj4okk
JwfC9A9PL6gghzlH6uCpMQ6eGivdH7IGQ3fo1BjPHBqsaJvZuQQnB8JljZdKKfeIWX08a1G0o5xh
WmqnOumcPSOLdY8qA0uhqAH7jo9w948lTT4Xf3jX5bQ1X7xhgWY0TePtNwt8HiffevQYkxdJFSlF
Q0iS7l11G/Am4J+Bi7bj9Vg4WvJ5s1KAnj86wvNHh2smg5VCWcowisYSDIzOWBp6JwfC7Dk6X52v
nDGY0nX0jDJl9mCVdN/VgZHJWY6fm6xvYYYSp2FWMqulnPTFPFi1ygEzEonGmZ6Nc2IgXLN9nr4w
zeB4hP7haQ6eHiu/QRH2HsuvIpnNPYtaFKwoYAFRf5MZY6SSiRJ5ZoLB8QgXRusfxm80buyKGDOM
WaVGmw65UEQrGeqJMrAUigVy4nyYz353P06nxh+86XL6OpoaLdKSo63Zy50v30xkLsE3HznaaHEU
K5cEaYMq+xcDamctLCPiiSRH+ic4VEJJzLcxdHRdJ5ZI1rR5qZWBV0rBOXhqnNODU5ZNcwfHI0Tj
iZzyWErZOj8ywzOHBpnJKFcF9pXxdZH9pFI6B0+NcfrCwivfHTs3yfDkLBN1bAa8KGpjnUIEx8LR
isd5shLPhk3iNTKAqwlDq2SLarxDxYgl0s+71bWbiyU5dGqswEgpRSKZYnhiNm8MTl+Y4qmDF/LG
164RaLwiZbfI7NPvceXeWxldi0HFBpYQYiln1CkUi8pYOMqn79lLPJHid95wCVvWtDRapCXLTVeu
ZmNfM08dHCwo4atQ1AIppUNK6ZRSOgE/aU/WPzVYrIZgR9E1F7mopWGVk8Miv6mUYpVV9koputnN
zfuJJ5LsOz7CxPQcZzI5Wbm8FpOFZRZhLBzlyNmJvH3OxhKEIzEGxqwLaJTDajyPnZ/k1IXyHpdq
Ztkr8VpEovGqvGnZQwyORTh4aoyY6RzNcqd0nenZeFmD4Ej/BANjMyu29HolaBW4sIq1PqtVqO/p
wSkmIzGOny8sPFFqm+PnJzk/Mu8Ryz5DRkPNLOGzcqhgX7pOWWtS13XODE4RicZz+8zmplltv5Q9
WKeFEH8vhNhUc2kUimVELJ7kX+99gXAkzltetZUrt3Y1WqQljcOh8c7XbsehaXztQVnww6xQ1BIp
ZUxK+WPgNY2Wpd5MzsSQZ8arCr8xrh9L1Fa5jSeS9I9MFyxfqH4zFo5yZnCqQEEbHJ8lMpfg8Jnx
gvLVBdXFTMblkf4JxqaizM7Nfy8tVBE7fHrccnm5fKiZaJxnDg9ybrhw7GpBLJ5k34lRXjgxyrH+
yVwOUyKZ4vj5yVyBEyuyI3LyQphwJFbQUPikyXg8OzjN/pOjtqvIFrtvl1LKXCQaL/DQVIN58+z7
Ev2iS2L0+tZ6vMrtLxyJ5e6bmcw9YRkeXOI7ynpSRS8bzTs+Ncf50RleODFWMIaNvG1cVWxzLenY
9i8JIeLAl4F7pJQqsUJx0aDrOnc/cJjTg1O8dFcfr7p6TaNFWhas62nmNS9aw4PPnOX+J09x58s3
N1okxQpCCPEe06K1wOpGyLKYZMMAx6aidLb4Cz7Xdb3Ag5NdbnydrPGcx+DYrOXyhc6uH8vMpvs8
LjxOp2HH8y+dDg3b9qJhO+MwLdQQNCbsOzTNtkI+Hk4rymeHp8v2UMzzQhYLdTR7+jKK7Fw8yVx8
lpHwLF2tfsam5hiemGV4Ypbrd/Ya9qtbvobyRuhSyLmdno1zYTTCqs4mAr5q1N58jvRPEo0lmIsl
WdO9dHpcGkMsF9MgjcWTHDw1hobGdTt7csuny+Vf2hQy374q3CaRLduPnrs/s993uq6jF3ivl6gH
S0p5QUr5b1LKVwC/m/kbyHi1fLUWUKFYivzkV2f55YFBNq8K8Vs3C0vlRWHNG166kY6QlweePlO3
GVrFRcuNhr+XAm3AbzZUokVkLDzH6GRhL6li6oR5ebHwrHMjM1VVGCt2XFuGhp1VTMp99p2GhtNp
9mCZZSgvj1ERs2scLZbyNn/A8quYjSCrELRkSsdOS6WCcSy/ScM5MzjFSHi26lBPM9GM4VyrfC1I
V/KL25zhSCRTJMsce3x6LidnvclWTNTR2Xd8lLl4cdmMDX/tPCm6bjbw7cmU9/SXePbrSVWmvBDi
ZcC7SP+I3Qu8H7gV+DbpmHeFYsVy4OQY3/rpMVqCHj7465fhdqlaMZXg87h4282CT9+zj7sflPzZ
264qrPClUFSBlPLdjZZhsTlydr6B5thUlLGpKB0tvYVhNRaPmFlZKWZgnR2aQk/pFc/WF3uqa1UN
2ii+Q9MMs9cQ8LqIzMUt100vmF+Sn3hvlFPPe+1wlv+estLddF2vW+8d44x+sUp95nw8q6/buXjx
fmClIrTMRm7pre1QXoZyzM4lcDkdud/meMaVaavfWYXXKZlKkUqxYD3A3Fy3lKG+Oy9XyfqePJHx
8l67vSeXjzQ0McvpkQhr2n04HbXUW+ZlNT5zVsTi+c+aneeikksyHyKYbWxNwcTBYk2CVGxgCSGO
AaeAzwMfkFJmR/OQEOKOGsqmUCw5hsYjfO57+3E6ND78xstUOfYquWJLJ9eILnbLYR7fe56XX7Hi
o7gUdUQIcZYSOpiUct0iirOojE0VeqzSzA/HaDiK2+WgNeglFk9y6sIUa7uDeR7kcyMzNPncRY9j
Jz9rYHSG04NTXLW1C4/bWdxzViMFx2gApQ2s+c80s/5YkIM1/zqRsK5TZif8zg71bL5rJ+LKTgW4
F07YKzxUECJYY2V1obvTdZ29x9Ml0o1hjlB9blMxRiejudwy87Eqxdg3S9PS+YRZFnbvpXA40mG0
J85PEmr2E55xWuou4ZkYZ4emWdUZqMgAq+T2TublYOllLWedCqsrZtbONWDWdXRKF7ipF9V4sF4L
aFLKowBCiCullM9nPruxZpIpFEuMaCzBv37nBWaiCd79uu1sXqUqBi6Et7x6G/tPjvHtnx7niq1d
tKjGzIrqeWmJz9oWTYolhFGHyFYAu25HD2cGpxmbihJPppgylLmeicZL9kqy8m7NxZNEoomcsnZ6
MJ0DMjE9R3dboKghZVbKy/azSunsMfUVstpPFrOxBdb9cbIUyxMqFUY4kslV2rgqhM9jUKUsRFr0
sEETUwstZ25yYRnHota2Y7W7Ozc8TXPAQzBQOEmQ3aeup+9jVyZ8dHJ6jsmZGGu6gvMKeQUkqnDF
GtMJSvUGG5k05i/azVUqXM/q1it2P05H40xH4wT9btuTx7NzCc4O2i+vb36O7HmwKpjoyHmw5t+W
KnBTT6rxEb4L+HPD+z8XQnwcQErZ2G8RhaJO6LrOF394iHPDM7zq6jXcuGtVo0Va9qjeWIpaIaU8
nf0DmoD1mb9twP80VLgGYa1YzRtK5UK7CsqYT0ULyou/cHwUeXa8sOqcyVWwpjM/tLBSvXQunsyV
b8/bj1lxMiqY5Qwsw7bGCnd5toQpRNDIsfOTTEZihE3GmVnJ1XW9ZiGRVpg9WFaGcC31SR1TJbgl
YmGdzTQGLijcYpBvbCrKbjmUK59/6Mw450dnCNehn1Yx8pR747kaHpmZaKKgOmMxynnlrAyYsj20
yqwwE40jz6Sfe3lmoqJ+ZHlht7puz2CqJEQw879WoozgUs7BuklKeUP2jZTyN4UQT9RQJoViyfGD
J0/xrBxm+7pW7nrllkaLs2K46crVPLn/Ak8dHOQll/Vy6caORoukWMYIIf4FuBnoBY4Bm4H/21Ch
6oRu0UCzHKkqtjFyYSzCht5Q7n12Bt+s1Gd1vmJlpwtmlC2Olad72nQuGI9XoFga3g5NzOZKSRfb
B+TvIxZP4veWV5nMh3360CDtzZXV/ypmDGqaxpnBKTxuJ73tgYK1J6bneGLvedoCrpo1vD91IZxn
RJqNlnIeCDvlvSenDfsvdofaLjIy//r4uTCH+sMFuVdz8SRe93z1yVr0RSpWqbMUxexus8fRKF2l
IZlWxn1Zj3GZz7PhpOPTcxX17ErLk29g2vEm5YfYFpk5ypD11mfzui2/W5awB8sjhMjF8gghgpQw
1IQQ7xJC6Ia/C6bPf00IcVwIMSaE+FgV8igUdWXP0RHue/wkHSEfv3PHpbnwAsXCSffGEqo3lqJW
XCul3AHskVK+iHQPrECZbZYlL5wY4zk5XPRzKyUiEk3kFJyyE8cLUEJyBpY5HyJDKeMny6kLYRLJ
FIlkiqFx63Lv5SUwHiJ9kHgixYmM96kcRr3u0JlxdF1naGI2z2NnZ5iK58mVJqu87js+yrNymLlY
kvOjM3meROPxs16+C6MRBsciPHNokHgimWe0uByOijxaF8YiREznW01VNyPHz0/mwjKPnJngnKFX
Wr5HTmd4YpZ4IsWEzXLvRtlGwun7xlydr6D6ZA307ap2YTiw8Y4tVfTJbAwWFLMxr29xcmUdqpkw
0OGJ2bLfA84KQyuNYZXp8L3CdfweF12t6XYTY1PRstUfrfaRHcJ0EZLCMYsnknkVDetBNR6sz5Eu
aLEbcAIvAv62zDZngEsyr3OjK4TQgC+Qrj74I+AhIcS9Uso9VcilUNScc8PTfP7+A3hcDn7vzssI
BVSeUK1Z19PMzS9aywPPnFG9sRQLJfuL6RVCaFLKZ4UQFXuwMpOIXwVeR9oT9mYp5RHTOpeS/u3a
LqVc9DKY5ap1WXEw0y/LDjVROnMepeqSzKcicQbHIkzM2FOEjB6sAsVQT3sGyoVe5RkPJsXs6UOD
ALQF5/NTLoxF8HtdhOqYQ5rtp2XXe6FpWq7h71h4Lr+gRyrF9Kwd41K3VPQHxmbobpvvtTYVieWq
9Nkl22tr25rWknlMZwanGRibobc9YDuPzI4zKpnS869zDdrR6rpecRUNu0c1Xr/hCfNkQ+XeqHg8
yd5jIwQDbjb1hQq3AfqHpjk/Wr6svcOhVV2rv1h1TeMwnjbld1mdrdU+sveuVVNvHZ39J8aYSyTp
661fLn01fbC+CNwEfAv4b+ClUsovl9lMl1JOZ/6MZ7sZWAPcL6V8GJjO7FuhaDhTkRifvncf0ViS
99y6g3U9zY0WacVi7I3Vr3pjKapHCiE+CDxGesLuM0BrFft5B3ALcC0wDHzC+KEQIgT8DBgq2HIJ
YCcUcCF5GOeGpzljVnzyFNZ8CkIEyVesikk7E43bzkUx7ieWSDJump2ejsY5cGqsQGEr3Mc8xQya
qci8TLOxRJ7hWs/oI8u8OqsVtXnv15xFVMBYuLzBWipszhiyNR2Ns9eiAElJ+TIc6Z8oWGY8x+w1
jJXoq1S4ffkLcKR/goOnx/OOOTQeIRKNF8ibSun0D09bjqOV3HGLXEHzejmD1HCwcrbZ5PQcIxOz
BfdvOYPSKkduJppgNpZgeGKWg6fHLTzKuq3Kk1C5ByvvMEU/0YqGHlpdXqsxKDWeKR3mMtcpXseo
mYoNrEwz4SuBEOkfrtcIId5TZrM2IcTTQohDQoj3GpZnWz5nGwCMA32VyqRQ1JpEMsVn79vP8ESU
22/YwLU7espvpKgar8fJ224WJFM6X31A1q1njGJlI6X8APAN4P8AXybtfaqmN+MrSIcZHgZ+QuHE
XxJ4JXBf1cLWkwoSw4uFIxV7Bk9fmOLscP7stg48f3Reyc5uW8yDBfml0Ys97mPhykLravK1kdnH
yORs0eIHHneh6jRfgbG4ED1t6WhVq3L4JwfCDI5HSOl6XsicEStvj5VBEY0l8kIiC/Xn8gOl63rR
9cwNbKupplfiyLlX2bumXCGRvM9se0fn9zkXS3JiIMw+i1L1g+MR+oenef7ocMlx03WdkclZnj0y
bOk1yTITjfPskSFODoRNZ2GoLmhxvQ6dGefY+fxeWekP4fzIDAdOjVk2Ps4aH8aJS6OBbOUZ1AGn
Rc+3SDTBgMmrtRADCx3LtIBSxpGu64xPzeU1Pre6LiV7axrWr6Z6pF2qCRF8kPSPy2nDMh34UpH1
j5H2dn0OeCPwH0KIh6SUZ6o4tkJRd3Rd579+cgR5doJrRBe3v3Rjo0W6KDD2xnpsz3lecaXqjaWo
DCHEU6R2nVdvAAAgAElEQVRD+74hpfz6AnbVQ/7EX0gIEchGYEgpZ4B9QohXVrLTtrYALpez/Ipl
6OwMEmr2F/28ozOIJxIjNFY8d6nJ78Y168LldFhWnmtrayI0Xeg9momnCo7d3t6Eb3QWn2Hbrq4g
Y5E40aROZ0eQkal8RS7Q7KMtU/whkUwROl/oWfK4HfhSxRsgZwk1+3E5HbSGfMQWqOt3dARxOTWG
zk7icLkINReqSc0BDy6TYnp6OMLLr1rDXDxJaMDaQOrqDBLXNXxeJ11dzQyMzNDkdxNq8nDw7CSz
03FW97XkxtehaXR1NRNqTt+KLS0BQs3pa6q7nHS3BZidSxAazFd6jdenLWPURQ2FHlqCXnRn6fuw
vT2I2+Ug1Bwu+Mzj85S8/3Ln29VMy/AMHpveEABvwMv4TIyAz0VrawB3BR5MSF+/0FDx8bAi1OIn
NJdW9FuDXjCMTUtLgFAkLb/b76Gt2Ze7HnnH7WxmfHaCULOfsZl43jGN13A6ln5+ZhM6q3oDjM2k
zy/7PBY9p1HrZ9nncTIxm0BzOgkGC69pW1sTXW1+Dp6dzMkUbPahl+hz1Rzy4/F5iOvzxkeT382p
4fS4Gs+tJejBMV1dFcbWtgDRWLLg+mTL7UctGkMnNAcDEzMkNA2Py4nTqdHaGiAczTfU2juaCM9Z
e6dmk/PnoGWesXpQjYHlllK+3O7KUspfAL8AEELMkJ5Z3EY6L2sgs1prJh+rAzhfhUwKRc14+Nl+
Htt7nnU9Qd57687SMyGKmvKWV2/jwKkxvvnTY+zc0EZ324qsT6CoHx8B7gKeF0LsAb4GfF9KWVQD
EEJ8BXinxUf311q48fHiM9t26ewM8tSec4SnihtPQ0NTRKLxkuskYnEicwncTmdBEQCA0TF3ye2N
DA5O5a07MuLCg874eITw1CzjYzMF+zo3MEki4/VJJFOWx3JllMBSHpJQs5/w1CwuhwMtlSRcZUGJ
nOyj06DrJc89lbAuoz08PEUsniy67bjXSTg8S9TtpP/8BM8fTRcpuXZHT26b4eHp3GuHpjE8PD+2
g0Ph3Oun953j+p29zM4l8o6XHY8sXiegk7dMTyZznguPy2lZAn9oeAqX02F5Lgdt3hfDw1NMTs4W
eLxK8av98/t2aFrF0QwDFyZLjocVY25tfp1kMs9zedIwVuNjMySKPFfDQ1NEI3PWnw1PWS4/cjKR
83yWknFkdLro54Xmr2nbkSn0+LzMoWY/Y2Mzubw+K/bJ9PNkfO4SsYR13qdpvCphbMxFLF747OuJ
JImY9TjriSRTszGmp6O5e6Ovvalg3YlxV9Exy+4jy/Cw/T5eVhQz0Koph3ZACGG7lrIQ4qNCiGNC
iPWkPVhx0kUyfFLKE8AJ4HbS8e4B4KEqZFIoasL+k6N845GjtDR5+P07d+H1LHy2WWGftmYvb3+N
YC6W5D/vP1h25lqhMCKlfEJK+fvABuBTwGuBc2U2+wPSoenGv3uYz93qBCZM+cMN43j/ZK46Whbz
JJCd52Zeb7VWYM09r0px9Fx+Lk0uRDDz3mqOyk5hhFSRJPhi605HKi/8UYCpDLnlsYp8nkimSkZm
amTHQs/L6TH3bsodR9c5PzLvjSknl/UxtUKZjEUvitwrul5ZSXCfu8h8/QLCNqsJ+RybqrwyXKmQ
PmMIna5TtBl3StdxVlhhuFRj71qRLuiRvyxh4RkyY57UqKaoTjl0vfICI1nDKGV6Tgr3XTqc0856
C6UaD9Ya4JgQ4hCQM4GllC8rsv6nSVcaPAgMAu8Gvg5MAHcA7wM+D7wN+Asp5YEqZFIoFsy5kRn+
/bsHcDocfPjOy2gPVda7RFEbXnxpLy+cGOWpg4Pc/8Qpfv1lmxotkmIZIYRoJf3b8hvAJuA/Sq0v
pZxkPhwwu4/7gc8IIbaTNtIeyiwPkP7dS5E24jozy7cAY1JK+2X6qsTKG2Ce6d97fITVpua+Bdtk
cg/M+kVaIV+Y0pHbp55/LCPxRIpYPEn/8AytQesKfJUo+CldzyWuLwTdxnGLOdR2yyH8nhJqlZb+
R9chHrfOQTMbb2eG5mfXzf2crPKrrCjoO2Z439seKFItrrIGyVZG9Fg4WpVRuBAWerxS3pgzg1NM
FzGK5uJJIvUymBZwSolkquB+Ttaz83UF6LrOXMzimdUqK8hofgbagl7aQz7OFimYZVy9nune1RhY
H69kZSnlKOlSt0a+bvj8UUB1blU0lLFwlE99aw+zcwned9tONq+qX+lORXnefrPgaP8kP/jlKXZu
aEOsa2u0SIplgBDiQdItQe4D/kFK+WSVu/pv0g2LnwYOA9niTAeB7wL/DBw1rH8U+CjlW5YsGOue
L4XaSLFCCVmyirxZ+UqXOK9ePkgn3Tsc84aaUb5sSOLgeISh8Vl0dIYmloRzEMh4bsoo6aWU+FKh
V1kPlq6TF5b33JH5fmalVF/zcZ89MsSuTaUDiqzGNruXVR1NtAa9lgZWSgfHAg1tqyqBlVDNvViL
psHFKGZcARw+M170s4XKtJCtE8lCD9ZSKSI1PRsvqPYJVl3sSmOeQFjf21yy6XNer7UalOgvRsUG
lpTy50KIW4GNUsp/E0JsJh3mp1AsSyLROJ/69l7GwnO86RWbefElvY0W6aIn4HPx/tt38on/fp5/
/+5+/vpdL1IeRYUd/gV4UEq5IFeGlDIBvN1i+QbD24YkZ1opa06HRqXVhnMNh+ugX+jonB2aoj1T
xMKo67hdGpqWzvupp3KzEMp5Qaxy1myhpYtP6+h5pceNCu+pgeKhmVa5aNXo7tnQNE3TLCsiQto7
VknuVCnDcjFZbI+ZHXbLhXVzOHK2ckPV73ExG0uQTNkPszVjJwduIaMdLhLSq0HRMu1WFE4Sld56
oY2y7VJNmfb/j/Rs3rszi95KOgxQoVh2xBNJPn3vC5wbnuHVV6/hluvWNVokRYata1q565VbCEfi
fOa+/WX7iygUUsofLdS4WupYNtWsIps6u5/uNn9eDlepmd9KySoyxv1H5hJs6F26PQV1Xa+bF8Sh
ZcZXt2oYm6aUQmsOEQTrMtt20UgXubBCnh0v6Lm0HAo+LZXwNyNW17SnggJO1ZyTy5X+UhiaiFiH
4dnAzvW26rNlJhQoEgJcbNtKGzYXhDmX3oVxMqCeOVjVFLl4uZTyjWSKl0gpPwZcVVOpFIpFIJXS
+c/7D3Lk7ATXbO/mza/eWlPlQrFwXnX1Gl5yaS8nB8J87SdH6vplqFAsBywNrCq+t7Iz/T6Ps+59
/sziedxLo3iQq4hlWlcniJZuclpN7ygr70y5xsnlqKQP0HIwsOoZIlhL3BUWxKgU4ySGsRF2JdjR
h+x4DIN+Nxt7QwXLi3mwo3OVeUPN11zT7E8ULSkPFpCddtEBhBBOqsvlUigaRkrX+fKPD7FbDiPW
tvK+1+9YFj8eFxuapvGOXxOs723mF/sG+N4vTjZaJIWioVjmYFXRLDNrqLlMil4tvwVzjYZNe/W4
6qtcAnhdTrxleo4VMy7qpaRrmmZrxr8YNffOZE5/TZmCKLnVF/k3sprQNisv31KkFg1ui1ZuJN3M
uqXJu6D92xHRdmhoBadbabEa88Srpmm29bmlZmA9KYT4MrBKCPGHwM+Bn9VUKoWijqR0na8+cJgn
XrjAxr5mfu/OXbhr0PxTUR88bie/f+cuulp9fP+JUzz0q7ONFkmxRBFCXC6E2C2EOJx5/1dCiOsa
LVctsczBWoDi66xS0Wv2e9i1qYMmn7voOsXKtLsXwcBKpnQCvtJzv1ZKmK7XL49HA2I2ytMXo9aG
X/bs13QHKwpZW2wqmfxcijlYVtTCVi1npFk925UYdrWoypml0tOtZHysnii72y+pEEEp5V8APwQe
IV2y/ZNSyj+ttWAKRT1I6Tr/9aDksb0DrO9p5iN3XVH2R1jReNqavXzkzVfSEvTwP48c5fG9qh+5
wpJ/A97DfBP7bwKfbJw4tcc6B6t6bS3rwcp6mZxOe/vye10EfG4u29RBX3uT5Tq5HCyTfJXMMFeL
nRC8tubCGX6d+uVgZfdfLZESoVNdrX4C3uLGbjmWcgBHJQWOFtvAaq3SS1SL+7/cLqyMh1p4zqrC
IGytn31zHqJD0+yHCNZUknyqKXKxCXgO+H+kf8z2ZJYpFEuaRDLFF39wkJ/tOc/a7iAfefMVBErM
viqWFt2tfj5y1xU0+Vx8+ceH+YnyZCkKiUsp92XfSCmPYOjXuBIoVkUwy/qeygpIuDIG1WWb2ulr
b8pV/iuHMVyt2CRVyqLIRZZGh2Sv72m29qRV2GAX0t68RuNxOdm5ocJ2FoZrYO+UG+Mdqqgn0iLL
2N3mt7We+blajNs/6C/Ubxrx1JWr6lf7A9pfdUl5sEh7rh7O/D0OSODeWgqlUNSaeCLJZ+/bzy8P
DLJ5VYg/eeuVll8+iqXNmq4gf/rWq2gJevjGI0f5zmPHVeELhZGEEGIj8znCt9Cgcur1wup2N85K
e91OvBUUkXBmPFgBnzvTP8bedglDrktni8/Se5JKpT1jbpejwMtVTT6P0XjctamTyzd3VrwP4/GL
iVCpF8Rl0+tXz2+qVEqvu9Lu9zYm2mOR1XMCXlfJ0FcjmqaVzIXKsqqzid52QxjmIlhYqzoLPcu1
yKOzm7OXd1zT+3Le1oXIaWdLX6Yh+JLKwZJSbpRSbsr8rQauAH5ae9EUitowO5fgn7+9jz3HRtix
vo2PvPkK21+eiqXHmu4g/+ftV9Pd5ucHT57mP75/oKJ+LYoVzR8B3wNuEEJMAh8Hfr+xItUWKw+W
sVCFVkF4DBRWM7M78WTsn6RpGh0thZ6vlD6v9IeaPAWfVYrRU1dJafqgz013a36OUbERmpiO5bWE
CNr4rbBfsUyvm7Ggo1eslFYqid/ryt0fG3pDZYuI1IrF8PZ0twZyRSF03X4onabZyyl0aFp+SXyL
+78tuLCiFGY0TaPFVCK90gjBVR0W4b8V7kMzbaNpGu0W4bm1ws5z4MoMxFLzYOUhpTwAXF0DWRSK
mhOeifF/v7GHQ6fHuWpbF//rNy7PzVwoli9drX7+/O1Xs2V1C88cGuJjd+9mYHSm0WIpGoyUcp+U
chfp/OC1UsrLpZR7Gi1XrUjp1k1Dzcqgt4IiEuZtS+W7bOgNcY3oZm1XkHXd5UMRjRXzzIpduYp4
lv2ZTHkclSje5nWLbTsSns3lOm1f18b29RWG3ZVh65qWkp9XG26o6wsrJGBXz9y5vp2dG9rT3pga
GT7lPK52rvP2ddbXqac9wM717WW3dzm1nCcyldJtn5qGPaPFTjGZ1V2VeYbsNOQ1P9+VmhPrepoL
SqxXc9mNcpbrU2V1DLeztsZ89nrU06tcsaYphPg706K1QGttxFEoasfA6Az//O29DE9EueGyXt51
y3ac1XTkVCxJWpo8/Mlbr+RbPz3Gw7v7+buv7OZNr9jMTVetbnh+h2JxEUJ8DYvfSiEEAFLKdyy2
TPUgPGPdVNYYoubQoLXZy+QCGtAWo7PFh8vpsK0Ipj1YGdlq/Ew6HBqphZTktmGgtdrwKDgdjtx+
XA5HyeIaup42YH0eV1Gve8DnYmq28muXN9Z1IpFM4XBoucaxtfLGbeoLcejMeNHP7RzH63bi0LSC
CYj1fSGmw9ZNnbPbtTf7WNXZxNmhaaCyEFHNodnydplVj/aQjxMD4aLrX7W1i+eODtuWo/hxTQZW
BY/Mpr60YdXTHsDrcXK4xDUqiWY1wWH/3gl43TQH3AyOR4qus2V1C8fOTdreZzY0OpXSa+Bqsqaa
qXxj3UYd2Av8ZW3EUShqw5GzE/zrvfuYiSa4/YYNvOGlG1UT4RWIy+ngra/expbVLXztQcnXHzrC
rw4N8s5bttNnFdqgWKk83GgBFoNiJb7zyrQXCRHsa29iYCzfy9scsPaW+D0uy/42lX6FpgxeFTub
tgW9jE/PAdaKoDE8UtNKK96bV7UwFo7mrW/EgXV550q4fHMnbpeDUxfsNfu1o9tW+zNlHi8rY6+v
vYm5eJKxqShm7BSHmJ0zle0uIauVsVOMWvw2OzKVKc3HzHoqVncGOTeSNqA29oY4eSFt3HjcTtZn
mvJmQ20TqVTBqW3qCzE+NZe7P7O4HA5b8jscWt4Im/vPQf61r5W60t3qZzRsvN6F12RTX4jR8ByT
M/nn1tk6X8CjnAeuLejF4dDobgswO5cg4HNx8NR8g2Nz/l6x83NoGpdsbGd8as56hSJUOnm+GNUU
qzGwPma1UAjhAJBS1rgTnkJRGc8cGuQLPziEruu8+3XbuXHXqkaLpKgz1+7oQaxt5b9+coRnjwzz
1198hpddvorbX7qRlqbGV/hS1Bcp5d3Z10KIS4GdpDWJfVJK2TDBakyx8uFGZaFY+M3aniAz0Tjh
SIzmgIe1XUH8Xuuwm50b2hiZjNLbHmB6Ns6BjKJUqSKcTKXmc7xsbOrJCxUrPNdkSmd9TzPhmRhO
h4OEVrxPT1uzN9/AMgmQrmxmzwC4dGMH+0+OFizPKo2rO5uIROOs62kuPcufUf7rodplc0myZfYv
29zB8yYPSNaQeOrghbQcNq+n1+1kLp6sKNd154Z2yzGzolyREDtiOhwW/dacztw9ZfzI2JjbWOI7
z4gw7Ky3PUBXq5/OVj/PHBrMP4ar0INl5U1J52Cln4VsmsLlmzsZmYzmDL98bJy0nVVseLC62wJ4
Pa48A2tjbygvEqTcvSIMIZotTZ48Q1cj/az0tAUYHI+gacWriK7ubKLJ584zsOxc/0r7+WXXT8tZ
H2OrGsdYFIhb/CUy/ysUDSGV0rn358f53PcO4HJq/K/fuFwZVxcRLUEvH3rjZXz4jZfR2ernp8+f
488+90u++/gJZkv0j1GsHIQQ/wTcB9wB3An8SAhhOSm4HCkWupSn/GjWypBGvhoRavIUbbDudjnp
62gqKJhRnRqi2d5W09LGzGWbOop6sPo6mvKUuWI4NI1EyroPl9Wyrtbi5baDfndBMRAjfq+LXZs7
c6FzxShmzm1Z1ZKbga827C47Xi/a2Zv2rJWQN0vekUrYmtkCJc2mAiilJK3EFne7HNbFFHL7Kr8z
q3V62/2Gz+eXFxuZUJMHt9PB2u7m3Lm5nU429IaKlhp3OR0FxoJVaKmmaXS2+FjX3cyOTF6f3+ui
ydDiIM8IrJHObzY8vB57uUyV9B6zwkr8VZ1NBP1utq1tLXp+uebkpn2Vc4ZW6pFq8rlo9ntshQFX
SzUerI8CB4GfkB6L24CtUsq/r6VgCkUlRKIJPn//AfYdH6W71c+H77yMNRUmjCpWBldt62LX5g4e
33ue7z1xiu8/cYpHnzvHa69bxyuvWq2KnKxsXgnslFLGAYQQXuBJ4K8aKlWNsOvBslIg8xTQKlOX
Sim6xbwQWdHsekuyVeqsRDSfv3mPaZ+UnvswkQmpdDkdBfI5nRq6YUo4UIsS5DZ1vAJPi9uJQ5vP
v/C4nMQSxb1zVmQ9WF63E7/XVXGVxlJrtwW9dIR8BRUmmwMey1BSqNQY11jX04zDoTEViReEqhn3
FfC6LBsup5+B/KO6jMVeTJMQVgT9bq4W3QAczuQ75oftWUxcaFpBfpWm5Ye7Gte1Kp1eT4zGX197
E5ds7OD8YPHcrywFIbUVGnxWY+V1O7l0YwcA0VgF93cdHEwet5NLNrbTEvQyXEXOox2q8WC9Ukp5
n5RyRkoZkVJ+E7ip1oIpFHYZGJ3hY1/dzb7jo1yysZ2/etc1yri6yHE5Hdx01Ro+/oHrueOlG0mm
dO752XH+5N9/yY+eOq3Kuq9cLpDfWDgGnGqMKLWnmIFl1GWcjnyv04beEJdtSis1WeWuHkpeV6uf
vvYmdqxro7PF4A0qohxdsaXQy2L0ERjLJ2ebtPqLNDTObW/SoeMZA8vtctDd5sdl0IRdDi1vPIuN
bZZi+Wr58pchcwhz1TxNg7XdQbwuJ+0hL5duLF/1zoxZfFs6qcVKxTxorUFvQd7Q+t4g29a0lvQ+
2RIjc8g1XUHarMp3G0TaVaT3Wblm1p0Zj8ymvpAtL2G5+QC308GW1S2Wx64klDZ/XWNIno1tbZxH
XhPy3mZ8XleV5eAXYOVYGqb2t8mbOCmCVbn1UuNT/wys6jxYHUKI1wGPZd7fCHTVTiSFwj57jo7w
+fsPEI0lueW6ddz58s2LkryoWB74PC5uf+lGXn3NGh7e3c+DvzrLPT87zgNPn+GW69Zxk/JorTRG
gF8JIR4lPYH4MuBEtvqtlPKvGyncQila3UxPl8+ejSUI+Nx5s8NetzPX968l6OW6HT0VKoD21nNo
Wi7HZyoy7xrKNiQ278fncdEa9DI8WbzCG6T78KzpDjIdCdAcMIWolZBN0zRCTR7GpqI0+924XU6u
2d6dyz9yOPILIpRz+GxaFaJzxseR/omSxyxFU8YDtGlViAtjs7ncG410Hkx3W6DE1qUxK5i2wury
dpD+z+mYD60sh9PhoD3kKzJ2CwkoNS0rcy5ZA6fQ6zK/wOtxcv3OXoC83Lxq5IF0pc7sRILxOE6H
oybKe60qNFrpQ1vXtjI5HUOeHS9qHBcajTURp+j+S6JR1uveHPCwvqc5L+Sv1L28GEXPqtEs3g/8
P+Abmff7gQ/WTCKFwgYpXecHT57iu4+fxONy8IHbL+G6nT2NFkuxRAn43AWG1rd/dpwfK0NrpXEi
85flh40SpB6MT0XxBwpnn3VdpyXozeXKGJWHahTvvPWrkNOYWJ/td2W5nxI7z4qtZarDmRsV2yFr
FFnlkzgdjpzXyk7FO5fTUXVeiljbhtvlyIXYuV1O1nbPV7Wzc02cDkfJ3mGWfcOqwOHQCsorljM+
rcSvukeZxXbZ8M1sI2AzGzLlxM3GxEImW8tdk7y+TobjXLm1s2rlvdw4VINl/qGm0dbs5drtPcXH
qMTx7Xhzy+2q/Pjmv7Zj8psrB7ucJdomLMI8fMUahZTyGeBGIYQmpaxnjy6FwpLZuQRf+uEhnj0y
TEfIy4ffuCs3c6pQlKKYofXgr87y6zdu5MZdq5QHdBkjpfxoo2WoJ8mUbnl/micHjLpLNYbJQrF+
hCoLy8qGBNlXwwopZRQ5DR4sh6bhNjVnXmjYmxGHQyvIX6qUUmfa195UXdin0RBnfizMlK/yZ/35
+p5mTg9al7BvafLmcq3MTWjNtDV72bGuLecBLDh+5n+z7EVth0q9J5b7sD6OVfn1arA6bCWl743b
gHWjXnPuZqnjm79TLt/cyekLU0zMzJVNyajIALc4vXJXK+C1vi9WdQaK9hrzVNCMvVqqaTR8OfBF
IAhsF0L8JfCQlPLpWgunUJgZGJ3hM/ft5/zIDNvXtfI7d1xatnKTQmHGaGj95FdneeCZM9z9gOTh
Z/u566YtXJrJWVEsL4QQfw78CRDKLNIAXUpZ0fS+EMIDfBV4HXAMeLOU8ohpnQ8DfwF4gC9IKf90
geKX5fItnXR2BHls9xnmEkl2berA5XSYypvnK5ALV/gqn3CwMgKrjsipyBOilXW3bFnVwnQ0ng4R
zExuOxwaPe2BnDEQ9LtZ17N4k3YLndNZ1xOsymti7VnIf7++p5mWMjk7xQ7d19FkaWAFvC52rG/L
hWvaKZ9XSoacgWUuNlGDybK5ePliDNb3uyH3qcS9VGzsNE3D53YRjc+nlGbzCEcmo+nlWnr7cjbX
1du6Ky5jbr6fzCGLfq+LbWtbicwlqpo8qPh+LXKOPW2BohPs3W0BOlp8/OrwUG6Z2+lg06qWRYlY
qeab99+A9wADmfffAj5ZM4kUiiI8K4f52N27OT8yw6uvXsMf3nWFMq4UCyLgc3PHjZv4x/e/mJfu
6uP88Ayf/NZe/vnbexmZKJ0boliSvAO4grTR4wHcmf+r2c8twLXAMPAJ44dCiE3AvwB/CLwT+BMh
xPXVi20Pr9uJz+ti58Z2dqxrI+BzFxhXUNt8iWr2ZaU8lfOCmMkWgihVbtx8GDtH6Gz1s6E3bX8b
QwQdmpbLVbNT4rwY2Spplcm1sAtWdUia4fV8SCZ5v6t2GrZbV9dL/2/9G21W3i0EqQLzsYoZFXaG
KxuWaC5IYr2/0jus1ntZkHOIxpruIF53Zfen2+WoKDJjY1+oYJnVKS7EM1vRLVti5dagt2Q+l7kB
scfttC6kUgeqMeHiUsp9QggApJRHhBBFS3IJIZzAf5LuSTIB/LGU8luGz81P0y1SygeqkEuxQkmm
UnznsRP8+KkzeNwO3n/7zlyyqkJRC9qavbzndTt49dVr+Oajx9h3fJS/PP00b7hxI6+5Zm3Nwj4U
decA0C+lrKzGdSGvAPZIKQ8LIX4CmItjDAGXA4eArZllfQs8pm28bmdJxa/RQa5WT4vb5WTH+nZ8
JfrwGBXV7evaGJ6YpauteH+qheLJKKqBTHVCY95XMYo1Hc5iqXCWuSCLkG9fERv7Quw9PmJ7fcsQ
sMxJ71jfxtOm5ryF28/vIJbIz5mxCv+6dnsP0ViCfSdGswcD0pUYAz4XU5E4g+ORoveaneFe0x3E
73XZ6htVznaxawCbVytmatYjNyf7DKzqaKLHothKPYtcNPnczETz2+gaz7Gt2ZvXEHq5UI2BlRBC
bCRz/kKIWyh9v/4WcBdwNfAu4EtCiO9IKY1G2euAxzOv1bSxIkd4Jsbnvrefw2cm6Gnz86E3qv5W
ivqxrqeZP3rzFTx1cJBvPHKUb//0OL/cP8i7btnOplWFs3qKJcfdwD4hxLMYyrVLKd9T4X56gMnM
63EgJIQISCkjmf1NA/uFEA7g40AU+GW5nba1BXDVoBhBV1fp8DXP9Byh0Vlb65YjEo0TGpqpaF8p
p5PQ1LxClN2uy1RveCwSZ85gCre1BfKOsW5N6YbCiWSKI+enCDWnjTCXy5HrfWVH1rb2JrqGp+nr
bMLtctIyEsE166K11V90+6ZonDMjkZLHCDVP5r3v7Ahahrhl1+vsDBLw5RsS2zbESaVgNDzLxlUt
DF163x4AACAASURBVI5G8pRMj9tJLBO+ZpYj+94sh3l5R0eQrva0Mj0dT5EgHSrZ3dVc0TU33m+5
c+4K4vO40HWdUH9+Hkww4Karqzknh/EY47MJQtEkbpeD6y/tQ9OKGyinhtPXoaN9/jy6uwu/p83n
4PK5CY1Hi35eavma3lnCMzE0l3P+c5eLoXAsb5uhqRiJjGq8fk1bUQ9SMOTn/HiUYMBNZ2czocH5
cR+ZjhMz2JutmeejdTwKTietQS+relwMjMzk7TPU5Cl53Yp9dltvS9Ft4okkoYHpktubyV7f9vam
gm38kRihzHO0fUM7h0+NAZlnsquZ2aTO5Gz6K/wy0cNUJMZzhlC/LB0dTXS0lJ6EMT4Hu7Z20tac
n5e50O/IYlRjYH0E+B4ghBCTpHuMvKPE+j8GLpdSHhNCnAKagGbSP1pZZjM/WApFjuPnJvnsd/cz
PjXHlVs7ee+tO3OzLApFvdA0jRdf0stlmzq452fHeGzvAP/wtd3c+uIN3H7DBuXNWtp8Cvga0G93
AyHEV0iH+Zm538bmnwXeAPyulPJCuZXHxyN2xSpKV1czw8PWhQOyTM7ECE+lFd5y65YjGktUvK+x
idncNqW2Gx+P5K034XUyXEH4UyKZ1j6z+3A7HcQzy+zK6ndqTGSuy/hEhGgsgVvTGR62jixNJFOE
p2ZpCXiKHsN4TgDj4zPELJqZZtcbHZ1mxpQT0p4JD+sMugEdj0PP229b0EskEqer1Z8nh/H+MMth
Xj42NoOWTBtpAadGZ9BNi8/J6Oh0Rdd8JhovONbI8HTO+2P+TE8mGR6eYnW7n7l4Mu8YbtLnuXV1
K6OjpdVCq/MwY/W8hA3PB1T2jHQG3YyMztAT8ua2GwtHC8ZrYiJCeCpKwOsuex4bugJ4PU5GR/LH
PRbNl7PJ7WDY62RiMkI4EoNkkr7WNmJBNyczxRyu3taNy6kVPSc73x9WZO974zmWI7v++Lgbr8m+
jEQThus3f95jXidNLo0xw3dD9ng717bM5+1lGB2dIVWmr+XG7iZm5xK0h3wkonGGDd6yasfDSDED
rRptdURKuUsI0QXMSSlLtoSWUg4Cg0KIDuBPSYddjJtW+0chRC9pL9YHlbF1caPrOo882883Hz1G
Ste58+WbuOX69ZX1TVAoFkjQ7+Zdt+zg+p29fPGHh/jBk6fYd3yE971+J6uVF3WpcqyKSoJ/APyZ
adm/kvZiAXQCE1nvVRYhxB8BHwA+JKX8XDXCKhZG4U/Cwn4jWpo8RDO9xIrhcjq4RlRWNKBcTyM7
IWQF+UVOB9ds77YtQzkcDi3XhyuuFy8Hb4WV9EV7tgHBbF82iwqXQb+74hSAGtVLsIXP4+KKrfnN
jhdaeTZ7vyXINxJ7OwL4PE6O9k8WbbSraRp+g3Furoa5VMlvCm4xfgvIxTPj97rwexd/cr6aI34d
eKWUctjuBkKIZuAB0g2Jf8P08d3Ao6R7lzwASOAfqpBLsQKYno3z5R8d4vmjIwT9bj7whku4ZEPl
Xe0VilqxfX0bf/fea/nGI0d5fN8AH/3Kbt74sk3c/KK1qqT70uNpIcRHgSfIDxF8tNgGUspJ5sMB
ARBC3A98RgixHXgt8FBmeSCz3y7g70kXffqqECIIxKSUSyJRIBRw09nip6ulur5NRmqo5xTQ1ebP
bzRc4eNUq2asWdb3NNPZ4iubuF+pF7ucAWDnLMwKYluZyn4Aa7ubmZieK5q/UryCnQ2B8taf32Dz
qhZGJqP4vdahsB0hH6u7alcCvypqfFPXrGmtaTcOTaM95MPpCOc1zG1Ef6SFnKJlyXnTb2e2bL8/
4/XMVvkzTyys72lmcGw2V13R3OdvKVGNgXVECPFV4Ekg99RKKb9ktbIQQiNtlG0FXi2l3G38XEr5
LsO6+4EdVcikWAEc65/kP76/n9HwHNvXtfK+2y5ZtGovCkUp/F4X737dDq7c2sVXfnyIb/30GHuO
jfDbt+6gs7V+SfiKinmZ6X9I6yNFDawi/DdwM/A0cBh4b2b5QeC7wPOAF/hw5g/go8DfVixxHdA0
jS2ri+dTVEI1+ovHRmEASCtPm1a1cOL8ZPmVbaFzjajeq+NwaBU3UbW731LYVV6zzYbbgl46bBjP
qzub8LodFRcIWIgy3dXqp8v0naihoaPjdjrZuqa1+p3XCOMt7a1BTmS9g2vMva+6Wv1MR+KL+ttT
68kM4yOhabB1TQuT0zHaQ2mdr6PFh05LrrJnlr6OJvo6mpBnxhmfnmuIZ8outiUTQuySUu4j/aOS
BG4FsmVmdMDSwALeCNxGutDF/sxMn57Zx3rSP1TvIV396RLgnspPQ7GcSek6P37qNPc9dhIdnTte
upHXv2SD8g4olhxXbO3k71Zfx9cekDx7ZJi//tIzvO0123jJpb21m8VUVI2U8ibzMiHEnVXsJwG8
3WL5BsPbuyvd7/KkcgsrFPDQEfIxGo6WXXdBX/Pmqmt67Rq91pJa/ZRld1NRD58qDORKv8uW21ef
0V65dNPCI2RKn/7CPSxZA6spk4Pe3eqns8W3qGkTCzqUZaPh/IUup6Ng0qCzRPGKrWtbicdTtqo8
NopKTL9/Jh0a+G4AIcSjUsrbbGz3+sz/3zQs+znpmPY7hBB/S7qfiIe0cfWZCmRSLHMmZ2J84f4D
HDg1TmvQwwduvwSxrnTlKIWikYQCHj7465fy5P4LfP2hI3zxh4fYe2yEd7x2e9U9QRS1QQixjrRH
KZsk4QVeCdzbMKGWOX6vi9YmL50VhhvaN7DmFa2QRU5ORcesQUhkLXA5HCRS83lM5Q0We9qr06mR
SFWm7JbKpipmjFaquJc7v2wz3FrbA6s6mjLhiNV7Mdw18GDVzKgvYovtWN/OWDhKu+H+Xuyc9AVN
IFqc10LFd2jakjauoDIDq6rhyBhk7y7x+ScwNXFUXBzsPTbCl398mPBMjF2bO3jvrTvqEp6hUNQa
TdO44bI+tq1t5Qs/OMhuOczRc5O899Ydlo1GFYvG10hXrr2NdH7UG0i3ClFUiaZpbF9f+aRXVums
JLTITlNXI8Y979zQvmQmOC7d1M6eY/N9pGqlDIu1bZwfmWFVZwU5TCViPGtVEKFRDqx1Pc2s66m8
xHat83b8XhcbekMFjYFrRUuTx7IgyHLBarSNBttKjf6o5Okyj9HKHBFF3ZmdS/CVHx/mX+7ZRyQa
565XbuEP3rRLGVeKZUdXq58/fetV3PnyTUxH4nzym3v5+kNHcv1pFItOQkr5cWBQSvkZ4HbgQw2W
6aIk1ORhfU8zuzaXnnDIU7QWcryAZ8lUmvV5XLgNXo1iYmUT+J1Oe3IHfC62rGmpyGNSypTwVFAS
vxR2h31pXJ36KPS97YG8fKHVXU24HA7W99rvn1isUmD57ZY2yWShH3Wp3Av1ZCHZYUv9miqWIEfO
TvCFHxxkZDLKmq4g77ttJ2u7VclrxfLF4dC49cUbuHRjB5+//wCPPNvPwVNjvP+2S1jfW58Ghoqi
+IUQa4CUEGITcBrY0FiRLl76Osp7WvKT3WsbmtZY0rI5NK2onDvWt6Hr9Q33yir9HaH58LLWJi+T
MzGcjtoYWFmDz3iMpUxr0ENPW6DisNdKaPK5a1pGvxRu5/y9tpTIFmVJJAvNhXwP1mJKtXhUYmC9
RAhxxvC+O/NeA3Qp5braiqZYSUSiCe597Dg/e+4caHDri9dz+w0bl03PBoWiHOt7m/mbd72Ie352
nIef7efvv7qbO27cyC3XrVcFWxaPTwCvAv4J2EO6mNJ/N1QiRWlWuKJVygjUNK3u5xz0u7liS2de
+KWdkM9NfSHbnjJN07huR0/Rc9UySVhL5XtQ0zQ29tn3LC0W1UYuBnxutqxuqXuI7JrOoO0KoQAu
p0YyRa7598VGJQaWqJsUihWLruvslsP890NHmJyJ0dcR4N237GDLmtqUEFYolhIet5O3vmYbu7Z0
8MUfHuLen59g7/FRfvv1O+lW5dzrjpTyu9nXQoh2oNmisb1iCbE0VO7ak7U1loJNUVHVwQzZpsN2
KWlIZv6vpDnzxYjX48TncVXlWStVca9WrKkw2sjjcjIXT5Iq0XQaVu53gO2nTkp5up6CKFYeF8Yi
/M/DR3nhxCgup4Nff9kmbrlu3ZIso6tQ1JJLN3bwsfdex1cflOw+PMRff+FpXv+SDfzateuU17YO
CCFCwHullJ/KvP8A8LvAMSHEh6SUgw0VUFEUo15eTYjTut5mos1LL383ey5LO4xxcVkqHqylikPT
uGJLZ/kVlwmbVoU4NRAunwayQp+RpduhS7FsmZ6N8/0nTvLT586RTOns3NDGb/2aoKfCGTGFYjkT
9Lv53TdcwtPbOvnGI8f4zmMneHL/BX7r5m3s2LDw3iuKPP4DOAUghNgG/CPwm8Bm0m1A3twwyRQl
yTNAqtCzNq5qYXh4qnYC1Qi3y0E0ng6TutjJ9nFSHqyLC7/XZeu3bqXeFcrAUtSMeCLFz54/x/ef
OMlMNEFXq4/fvGkLV23rUrN4iosSTdO4fmcvuzZ1cN9jJ3n0uX7+6Rt7uH5nD3e9cgstQW+jRVwp
bJJSviXz+k3At6WUDwMPCyHeUmI7RYNZoH21ZMmeV60KSSxnsgaW8mApLiaUgaVYMIlkiif3X+D+
J04yGp7D73Xymzdt4VVXr1HhUAoF6STkt928jRt29fLVByRPHRxkz7ERbrluHTe/aN2Sb5i4DJg2
vH4F8EXD+4szw3qZYOyTtZIm4nweF+FIbEFNcFcaysBSWLJCbwv15CuqJpXSefrgIN/7xUmGJmZx
OR3c/KK1vO7F63P9PRQKxTwbekP85Tuu4ed7z3PfYye47/GTPPLcOd5wwwZuvHyVyk+sHpcQohto
Bl4M3AX/P3vnGebIVSXsV2p1DtNxch7bd/KM7bEZ5zHYYIMxDrCw7GLWLKxZ8BrY/AHehV1gzZKN
SbuADV7AgA3YBowD4IDTOE2euZNneqZzVreyVN+PkrpL6pJU6la3Opz3efRIqnDr1K2S6px7zj0H
lFJVQA5VWYXJZgbZVEksmVtJRZmHhhrxUieQEEHBlhla9EkMLCFnItEYL+3v4NfPH6e120eR28Xl
5yzimguWU1ctDxNByITb7eLysxexde08Ht1+kke3N3PvYwd5dHszb7lgGResny+GVu7cAewDKoBP
aa17lVLlwJ+A/y2oZMKspNhTxPx6mXdsxSPhkoINsbHmp5/iiIElOMYfjPDUjhYef7mZXm8Qt8vF
JRsX8NaLlk9KilBBmEmUl3q47pKVXH72Ih567jhP72jh7kcO8NCzx7h66zIu2biAYo+EDjpBa/2I
UmoBUK61Hogv8yul/llr/ViBxRMyMNWKowoTR5mEQgs2ZEvjPl0RA0vISs9AgCdePsVTO0/jD0Yp
LS7iii2LuXLLEpqkto8gjIs5VaW8542Kt2xdxu+2n+TpHS3832MHeejZ42zbvJDLz14kyTAcoLUO
A+GUZWJcTXHEvpo9lMl8NMEGMbCEWYVhGBxtHeAPr5xi+/4OojGDOZUlvHnrMi7bvGjCK4YLwmyj
vqaMd19xFtdcsJxHXzrJk6+18NCzx/nN8yc4b81crjh3CSsX1hRaTEHIK2JgzXwWN1YRjRmiNwhJ
NNWW09nnp6JsZt4XYmAJSQTDUV7c184fXz3NiXaztsiChgquOn8pW9fNl6yAgjDB1FSW8I5tZ/DW
C5fz/N52nni5mRf2tvPC3nZWLqxh2+ZFnLd6rmQeFGYEMylzoGDP4myFZoVZycoFNSydWzVjQ+HF
wBIAONU5yNM7W3h2dxv+YASXC84+s5HXn7OYNcvrJE5eECaZshIPl5+9iG2bF7LvRC+/f/kUOw93
cbRlgB8/cZCta+dx6eaFLJtXLUqqIAiCMK1wuVwz1rgCMbBmNV5fiBf3tfPsnjZOtJneqjmVJVxx
7nIu27yQ+pqyAksoCILL5WLd8nrWLa+nq8/Pn3a38syuVp7c0cKTO1pYOreKSzYtZOu6eVTO0FAL
YeYig3eCIMxExMCaZQTDUfYc7eGFvW3sONxFNGbgdrnYtKqBizYsYPOZjZIiWhCmKI215Vx3yUqu
vWgFe4718MzOFnYc7uJHjx/kZ388zBbVxKWbFnLWklrxao0DpVQJ8EPgzcBh4F1a64Mp23wa+HD8
671a649NrpQzBLlNBUGYgYiBNQvwBcLsPNzNKwc72XO0m1AkBsCipkou3rCArWvnSZYyQZhGuN0u
Nq5qYOOqBvqHQjy3p5Wnd7by/N52nt/bzry6ci7euIDXrZ0nJRTGxk3A1cD5wNeA/wauS6xUSl0G
fBx4I7AMuFsp9XOt9XMFkHVaI/aVIAgzETGwZiCxmMHJDi/7j/ey93gP+mQf0XgazPn1FZyrmtii
5rJ0XpWMcgvCNGdOZQlXv24ZV52/lIPNfTy9s5WXdQcPPHWUB546yqpFNbxuzTzOWz1XBlKcsw3Y
obU+oJR6DPg360qt9VNAMYBS6hrAAHonW8iZgDyDBEGYibiMaVhBubPTO/2EnkD8wQjH27wcax3g
aMsA+mQvQ4HI8Ppl86s596wmzjmriYWNlQWUVBCEycAXCPOy7uTFfe0cONmLYZjpsFcvreOcs5rY
dEbDlPNsNTVVTxlNWyn1OODXWl+rlHof8D2gUmvtS9nuIeAq4O+11ndlazcSiRqeGType6w89eop
AC47Z3GBJREEQcgZ22eXeLCmCYZhMBSI0Nbjo63bR2vPkPne7aO9x4fV4myoKeXsM5tYu7yONcvq
ZNRaEGYZFWXFXLppIZduWkj/YJCXDnTw4v529p/oZf+JXn70uBkivGlVI6uX1rJy4Rwqymbn40Ap
dQ/wXptVDzvY/f3Au4EvKqV+r7Xen2nj3l5fptWOaGqqprPTO+52phIDXj/AmM5rJvbHeJD+SEb6
Ixnpj2Ty0R9NTdW2y2fnE3UKETMMhvxhBnxhBn0hBnxhvL4QfYMher0Ber1Ber1BerxBgqHoqP0r
Sj2opbWsWFDDigU1LF9QTUNNmYRdCIIAwJyqUq7YsoQrtiyhZyDAziPd7Dzcxf4Tvfz2hRP89oUT
uDANrjMWzWHJ3CoWNlaysLGS6oqSQos/GXwE+NeUZV8H5sU/NwJ9Vu+VUmo9cInW+ltKqe8AXwEu
BjIaWII9a5fX43FLciVBEGYOk2JgKaXuBN4DdAA3WycCK6XeBHwTqAO+obW+fTJkmggMw8AfjOIL
hBkKRIbfvf4w3qEQXl+YAV8Ir8/87PWF8PrDZIvSrCovZm5tOfXVpcxvqGB+fQULGiqZX19BdUWx
GFOCIDiivqaMy89exOVnLyIYiqKb+zh0qo/Dp/o51jrAqc6hpO2rK4qprymjrqqUuupS5lSVUF7q
oaykiLISD6XFRRR73KxcWENp8fQMfdNa9wP91mVKqYeBbyilVmOGAD4eX14BRDATW3xTKXUQSFRR
TcoyKDinZnYY8oIgzCIm3MBSSl0B3ApsBW7BNKY2x9e5gO8CPwd+CzyulHpAa71jImXq6PWhT/Zh
YHqQjJhBzDANpJF3A8MwE0ZEojFCkRihcJRQJEY48TkcjRtSEYYCYXzBSFZjKUFlmYeqihLm1VdQ
XVFCTUUxVfH36ooSaipLqK8ppa6qlJJpqrgIgjB1KS0pGs5ECBCJxjjVOcjpziFausxXa4+Plq6h
4Tp56di2eSE3XbV6MsSeLH6MmSHwReAA8Nfx5fuAX2mtP6qU+iJwX3z5f8UTXwiCIAjCpHiwtgHN
WuvtSqklwPuUUvVa6x5gFbAYeFhr/Uel1CBwOTChBtaPHj/E7qPdeWmr2OOmoszDnKpSFjRWUlVW
TEWZh4oyD5Xxz9UJo6mihOqKYqrKi6XWlCAIUwpPkZvl82tYPr8maXli/mefN0jfUJBAMEogFCUQ
ihAMR4nGDM5Vcwsk9cSgtY4Af2mzfLnl8z8B/zSJYgmCIAjThMkwsOYxEn6RSGM7H+hhJMbdun5B
tgbHm23qcx++eDy7C4IgCELO5CtTYrpJ1bMV6Y9kpD+Skf5IRvojmYnqD3GjCIIgCIIgCIIg5InJ
MLBagdr458b4e4tlHUBtfD5Wg2WdIAiCIAiCIAjCtGIyDKwngCVKqa3ANcBLQFApVaa1PgocBa4F
rgYqiGdrEgRBEARBEARBmG5MuIGltX4a+DJmlsBzgA8BjzCSfekDmIbXD4BPaK33TrRMgiAIgiAI
giAIE4HLcJpXXBAEQRAEQRAEQciIJLkQBEEQBEEQBEHIE2JgCYIgCIIgCIIg5InJqIM15VBKlQA/
BN4MHAbepbU+mLLNp4EPx7/eq7X+mJP9JhuH53Ir8AmgBPiu1vpflFKfAv7dstmLWuutkyO1PeM4
lyl3XcDx+awHfg6s1lq74ss+xfS8NnbnMp2vzU3A54Bi4FNa629NtWujlLoTeA/QAdystX7Osu5N
wDeBOuAbWuvbs+0jTF1m63VTShUB/wvcCPRhFnd+EfgpsA74A+bv12/3my2M1BOPUur1wO+BTwN3
M4v7Qyn1Ecz/5TDwUeA5Zml/xJ9t38dMHjcEfBZ4mFnWH0qpGzD7YYfWeptSahkO+yBfests9WDd
hJm18HygE/hv60ql1GXAx4F3AP8IfFQpdWG2/QpEtnNZCXwN+HvgvcA/xzM6AvwJqI6/Lp8sgTMw
1nOZitcFsp9PDfAkpsKUynS7NunOZTpfm28DXwT+H/BVpdTc+OopcW2UUlcAtwJvisv0Tcs6F/Bd
4EHgz4BPKqU2Z9pHmLrM8uv2HuCdwOuAn2AqTZ8FosBmYCtwS5bf7IwibnR+DeiJL5q1/REf2PsK
8BfA/wB/h6kwz8r+AN4OXIeZVO5u4KvAl5hF/RH/v/wqyWWfcvmN5EVvma0G1jZMq/YA8BgpSpLW
+imtdbHW+o9AF2AAvdn2KxDbyCxTB7AJ+BmmJQ6wIP4e1VoPxl/+yRA2C9sY27lk269QbCOzXFHg
9cAvbfadbtcm3blk269QbCOzXOcD5ZgGyoOYHtOL4uumyrXZBjRrrbdjZmndpJSqj69bBSwGHtZa
PwEMYp5jpn2Eqcs2Zu91ewTYFP+tHgcqgeuBJ7TWR4DtmPd2pt/sTOODwElgd/z7NmZvf1wDHNNa
P6K1vl1rfSFwGbO3P/yYz+N2TJ0pgHn+s6k/TgJnA1av0zac98E28qC3zFYDax7QH//cC9QopSpS
N1JKPQT8ArhNa73f6X6TTEaZ4krgHkwj8Q7MH9vz8dVnKqV2KaV2KqWumUyh0zDWc5mK1wWyn8+Q
1npXmn2n27VJdy7T8trE1xPfpjf+OTEwMVWuTeo5AMy3rCNl/YIs+whTl1l73bTW7Vrrw0qpBuBf
gB2YipDdvQ32v9kZQ9ywvh0zkiNB6v0xa/oDWI5ZW/XXSqnDSqm/ZXb3x68wo0m6MD1XHwVqmEX9
obU+qLXuTlmcyz2RF71lxs/BUkrdgxlOlsrDDnZ/P/Bu4ItKqd/nU66xMM5z+SbwNuBvtdZtSqkd
wAOYse1/D/xIKTV/skbk83wu+RRtTIzzfFKZztdmyjGTro0gzEaUUtXA74AmzND95zPvMaP5D+DH
Wms9FZ59UwADWAq8D7gBuJNZoNtm4Ebgkvjresw6tLO5PwrGbPBgfQTTIrW+7gdq4+sbgT6ttS+x
g1JqvVLqb7XWHcB3gFLgYqA1036TQM7nAqCU+kfgFuDDWutvA2itf6W1vk1rvRtz4l8NsGhSzsIk
b+dC4a8LjPF87Jiu1yYN0/XatMbfa+PrAVqmwLWxktq3MBJzPix/fD5WQ3xdpn2EqcusvW7x+/dH
wJnAFVrrlxndH4l7G1J+s5Mo6mTxFuBWpVQAuBT4JFDE7O2PVswQwRcwB788mGFys7U/3gDsjocT
/wxzrvBs/r0kyKUP8qK3zHirVmvdz4irDwCl1MPAN5RSq4GrgMfjyyuACLAM+KZS6iBQFd/tIBC0
22+yGOO5NAGfAe4CfqiUqgJCmIajwpwQ+TbMybInJ+dM8n4uT9jtN5mM8XximOENjfHlZ2Behy8x
/a5NunOZrtfmRcCLOQI4iBmO+oxS6m4KeG1SeAK4PZ7o5RrgJcxQmTKt9VGl1FHMTFJlQAXmOTak
7qO17iuM+EIOjLrWs+i63QC8FTPRxZ74//7vgTcqpe7FTH5xO2l+swWReGK5AjPjGZiZzrZj/r5n
a388jJnE53WYiQkCwH3M3v44DNwYTwp2JaaH7wCzqD/iHu95mPM1y+P6SC7/GTXkQW+ZDR4sO36M
OaHtRcwL8C/x5fuA/9Za/wYzq8h9mJm4/ktr/VSG/QpJxnPB/DMuxcxA5Y2/Pg78J+ZEyMOYo2B/
rrUOTarkoxnruUzF6wLZz2cxcAgz7Tzxz7cxPa9NunOZltdGaz2E6Sn9GPBvwIfiMd1T5tporZ/G
DP/4LWbGqA9hJgS4L77JBzCV8R8An9Ba702zjzDFmeXXLTHP8aeM/O8/gTmo80r88/cy/GZnFFrr
I1rrA/EJ+D7MuTa3M3v74zVMPeBBzGkdtzCL+wP4FqYx8Rpm9MbHMDNxzqb+uBFTB7kCM5HFIXL7
z8iL3uIyDGN8pyEIgiAIgiAIgiAAs9eDJQiCIAiCIAiCkHfEwBIEQRAEQRAEQcgTYmAJgiAIgiAI
giDkCTGwBEEQBEEQBEEQ8oQYWIIgCIIgCIIgCHlCDCxBEARBEARBEIQ8IQaWIAiCIAiCIAhCnhAD
SxAEQRAEQRAEIU+IgSUIgiAIgiAIgpAnxMASBEEQBEEQBEHIE2JgCYIgCIIgCIIg5AkxsARBEARB
EARBEPKEGFiCMMkopc5XSj1aaDkEQRAEwSny7BIE57gMwyi0DIIgCIIgCIIgCDMCT6EFEISZjFLK
A3wbuAQoAnYB9wBf1lqfoZSqB+4HzgBeBPqBU1rrTymljgNfAm4GFgF/C7wBuAroBK7WWvcqqWQb
vQAAIABJREFUpS4A7gIqgRhwm9b6ick6R0EQBGFmIc8uQRgfEiIoCBPLm4AVwGrgTGAvELSs/zjQ
qbVeCtwB/HnK/uu11ucA/wncC/wc84HmBm6Ib/M/wBe01qvjbXx7Yk5FEARBmCXIs0sQxoEYWIIw
sXQCa4HrgQqt9e0kP6QuAX4CoLV+BXMk0Mqv4u+7Ab/W+kmttYH5sFsYX7cZ+Fn88zPAynyfhCAI
gjCrkGeXIIwDMbAEYQLRWm8H/i7+alNK/RiotWxSB/RYvp9OacIbf48Cg5blUcywDYC/ALYrpTTw
OODKj/SCIAjCbESeXYIwPsTAEoQJRmt9v9b6cmAZUAH8k2X1AFBl+b4gl7aVUouA/wXer7VWwNXj
FFcQBEEQ5NklCONADCxBmECUUjcrpW4H0Fr3AAcAa+rO7cA74ttuBs7P8RBNwBBwID4p+W/ibVVl
3EsQBEEQ0iDPLkEYH2JgCcLE8iBwrlLqkFJqP2ZM+5ct6z8LKKXUYeAf4tvnUjthJ/Bb4CDwPPAw
8ALwVB5kFwRBEGYn8uwShHEgdbAEocAopVzxyb8opX4O/Elr/bUCiyUIgiAIaZFnlyCkRzxYglBA
lFK3Ag8ppdxKqbnANszRPEEQBEGYksizSxAyIwaWIBSWezBT3x4CngW+FM/eJAiCIAhTlXuQZ5cg
pEVCBAVBEARBEARBEPKEeLAEQRAEQRAEQRDyhKfQAoyFzk6vuN0EQRBmEE1N1TO+yGg+nl11dRX0
9vryIc6MQPojGemPZKQ/kpH+SCYf/ZHu2SUeLEEQBEGYJng8RYUWYUoh/ZGM9Ecy0h/JSH8kM5H9
IQaWIAiCIAiCIAhCnpiWIYKCMNXwByO0dvvo9Qbo8QYJR2K4XS6K3C6qKoqprSyhfk4ZTbXluF0z
PhJKEARBEARhXIQjMVq7h1jQUEmxZ3r5hMTAEoQxMOgPs+dYN3uO9nCsdYC2bp+jEvalJUUsnVvF
GYvmsHFVA6sWzcFTNL3+NARBEITZSzAUpa3Hx+K5lRS55fklTBwn2r109fsJhWOcsXhOocXJCTGw
BMEhvkCEV3QHz+9t42BzP7F4iYPy0iLU0loWz62isaaM2upSykqKiMUgGovh9YXpGwzS2efnZPsg
h0/3c+hUP4+8eJLyUg/nntXEBevno5bWindLEARBmNIcPNXHUCBMkdvF4rlVhRZHmMGEwlHzPRIt
sCS5IwaWIGShuWOQx146yfb9HYQjMQBWLaxh0xmNbFzVwOK5VTkZRsFQFN3cy64j3ew43MWfdrfy
p92tNNSUse3shVy6aSHVFSUTdTqCIAiCMGYSSm84GiuwJIIwdREDSxBsiBkGu49089hLzew/0QvA
vLpyLtywgAvWzqOxtnzMbZeWFLFxVSMbVzXy7ivP4lBzH8/uaeOl/R088NRRHvzTcS5cP5+3XLCM
pnEcRxAEQRAEQZh8JtTAUkrdAHwf2KG13qaUehK4zLLJ57XW/6qUugn4HFAMfEpr/a2JlEsQ0hEM
R3luTxuPv9RMW49ZG2HNsjreeN4SNqxqyHsIn9vlQi2tQy2t412vP5M/7W7lD6+c4umdLTy7u5WL
NsznLRcsF0NLEARBmCJIKLsgZGPCDCyl1BXAV4GWlFX/hWlMAYSUUjXAt4GPAwPAt5RSD2itOyZK
NkFIpdcb5A+vnuLJ104zFIjgKXJx0Yb5XLllCUvnVU+KDBVlHt543hKuOHcx2/e389Czx3l6ZyvP
7m7jog0LuO6SFdRWlU6KLIIgCIIgCMLYmEgP1kngbOB7QK1leUhrPZj4opS6FCgHHsQ0sL4HXAT8
cgJlEwQATrR5eeylZrbvbycaM6gqL+atFy7n9ecsYk6BjBm328XWdfM5f808i6HVwgv72rjq/KW8
6fyllJdKdK8gCIIgCMJUZMK0NK31QQClVOqqG5VS7wGOAx8C5sWX9wN98c8LJkouQYjGYrx2sIsn
Xm7m4Kl+ABY0VPDG85Zwwbr5lBRPjUrnCUPrvDVzeWZXKw8+c4yHnj3OkztaeNvFK7hk4wJJ8S4I
QkHxBSL0DwVZ0FBZaFEEQXCIPxghGI5KVMwEMtnD4L8D3MBDwP8BdwH3TLIMwiylfyjEs7tb+cOr
p+gZCAKwfkU9V563hPUr6nFN0RTpRW432zYvYuvaeTy2vZlHXjzJvY9qnni5mb+88izWLK8vtIiC
IMxSdh3tAqCmsoTKsuICSyNMJoaT4o/ClGT30W5ihsGmVY0SETNBTGqvaq3vSHxWSv0O+EugNb6o
1iJP6rwtQRgT0ViM3Ud6eGZXC7uOdBONGZQWF3H5OYu44tzF02rUtazEw7UXr+CyzQt58E/HeGpn
C1+4bwcXrJvHn73+TOZUSmp3QRAKw9QcnhKcEAhFKCtxrg5O0bFIIQcSdTwjkmp/wpjIJBfVmOF/
lUC5UupMTA/Wb4DPA28AdgAvAl7gemAQCADPTJRcwuygrcfHM7taeG53G/1DIQCWzq3i4o0LuHD9
fCqm8UjrnKpSbrpqNZdsWsgPH9U8v7ednYe7uXHbKi7bvFCKFQuCMOlM1QgAITOt3UOcaPeyYkEN
8+oqCi2OMMmIE3LimEgP1o3A3ZbvB4GrgK8Df41pWN2mtR5SSt0CfAFzEOxDWuvuCZRLmKEEQ1Fe
1h08vbOFQ/G5VRWlHl5/ziIu2biQZfMnJxvgZLFiQQ2337SFP752ml88fYR7H9U8u7uVv7pqNYvn
VhVaPEEQZjiJwuvC9KW7PwBAnzcoBtYsIWaN7RQLa8KYyCQX92A/v+osm21/AvxkomQRZi6GYXCs
1cszu1p4cV87gZBZYX7Nsjou2bSAc89qotgzNZJWTARut4s3nLuYc1UT9/3+ENv3d/Dpe17irRcu
580XLJMkGIIgTBiD/vDwZ5mPMz2JxswLJx7I2UMsNvJjNab4Dzch3YAvRMwwplWEjsxsE6YlXl+I
5/e288yuFk53DgFQV13KlVuWcPHGBbOuMG9tVSkffNt6LlzfxQ9+p/nVn47xysFO3vfmNTPOcycI
CZRS64EztNa/UkrVaq37su4k5I18KWdd/X5OdQyxcmENNTKXdFJJKNtF7twVV0PcH9OSJAOrgHLk
SjgSo3SKZHl2ghhYwrTiZLuX3714kpd1B5GoQZHbxbmqiUs3LWTd8nrcY3hIzCQ2rmrkP/96Dj/9
w2Ge2dXKZ374MtdetJy3XLB81veNMLNQSn0M+HOgFPgVcLtSqldr/ZnCSjZ7SLavxq6qneocIhCO
0NnvnzIGVixmMBgIU1MxNeSZKBLhYrk8H+RJMr2JJnmwCiiIA1xpPk8HxMASpjyGYXDgRC+/ffEk
e4/1AGbdqks3LeSC9fNn/AMwVyrKirn5zWs4b81c7v7tAX75zDH2He/lA29dS31NWaHFE4R88efA
VuD38e//BDwHiIE1SeTLg5VoZ6ooe5FojJd1BwAbVzZSUTYzVaWYYRCOZ5HLFnrlD0YoLSlK2q6z
z8/ipqpp5VUQkudgTZcQwenIzPzXEGYM+mQvP3/yCEdbBgBYvbSWq7cum9J1q6YK61c08On3nc89
jxzg1YOd/Pv3t3Pzm9dwzllNhRZNEPKBV2sdSxSzj3/OmnVBKXUn8B6gA7hZa/2cZd2bgG8CdcA3
tNa3K6VKgO8D1wJDwGe11ncppZYBPwXWAX8A3qW19uf1DKc41s4ejyLkGuPY9MBQiMFwP1XF+Z1r
6g9Ghj8Hw9EZa2BFLElKMoUIDvrD7DnWTX11GWctqU1aN+QPi4GVI139fob8EZbMq8LtcnGy3UtX
f4C1y+tySpc/VqwhgtOJKW4LjmJm/msI055TnYPc/+QRdh0xE0qee1YTV29dxsqFNQWWbHpRVV7M
h69fz1M7WvjJ7w9x1y92c/nZi3jn68+gRB6KwvTmiFLq34E6pdQNwDuBfZl2UEpdAdyK6fm6BdOY
2hxf5wK+C/wc+C3wuFLqAWAtcF18u/cBX1VK3QN8FojGlz8Xb++r+T3FycUfjFDscTtPjpODxjPg
C1FeUmSfdCih2+eoQO070UNNdTkr5lbmtViqVYzoDK4TZPVkuDIYWEMBM5lJjzcw4TLNBg6fNrMc
N8wpo6q8mJZucx65PxidFAPLen/HDAPDMKbFgHVsmllYkmJMmFIM+sPc88gB/v3729l1pJvVS2u5
/b1b+PANG8S4GiMul4ttZy/i3967hcVNlfzxtdN85ocv097rK7RogjAePozpUTqNWbT+xfiyTGwD
mrXW2zGNqE1Kqfr4ulXAYuBhrfUTmHUZLwf8mIZUO6bXKxD/vg14Qmt9BNge33baEghF2Hmkiz3x
MGwnJGV7zqD7hCMx9h3v4dWDXZnbmyoBQRYxwjPYwPIHo8Ofx5LkAqafV2EqkRqeN2nhepbDHD7d
z45Do3+XnX1+jrT0T448MxTxYAlTAsMweOlABz9+/CADvjCLGit5x+Wr2LCyYVqMrEwHFjVV8cmb
tvDTPxzmj6+d5j/ueZkPXLOWzWc2Flo0QRgLUeDL8ZdT5gEJraE3/j4f6ImvI2X9Akyv1JNAF+Yz
8xattV8pldrW6mwHr6urwJOHshFNTSOZQZvbvRxr6eeCDQvGVZKifzBITXX5qPYzEcJF95Dp3Whs
rKI6zXzYYDhKTas3bdu1nUP4AhFqa8uzHjsajdHaPcSCxqpheRsbq/JaPN5TFqCmx4z2rK7JLtNU
YM+RLiLRGI2NVY7kDUei7GvuH+7D+vpKmprs6yeGXS66B83r3NRUzZz2weGSKPX1lTTVT+36WYW8
fgmjyarH1FTHPVgNVcypKh3+Xl9fRVPdxGdArm+oHL6/E6T20b5mU6a6+sqClnup7fXjKjL/1+ob
qqgqT/879wXCnOoYZNXi2pwGDCbq/nBkYCmlXFprGacQJoTu/gD3PqbZdaSbYo+bt29bxRvPWyI1
nCaAkuIi3vMmxcqFNfzwUc2dD+zimguXc93FKyTLoDDdiJAc7WJgGjwNeT7OjcAl8df1wJeVUg+O
paHePHiNm5qq6ez0Dn/fcaANgCPHe2iYM/YkNgNDIQa8ptJlbT8T3d1Dw/t0dQ0SSKP8BMPR4e06
OgZGDZoNDPjxBSN4MOisypy06HjbAG09Pk7VljPg9VNTXU5X12BeQwT7B4Mj51Xsyvscr3xjGAbH
TpnjBWtXNNDfl/0+GwqEh88RoLvbQ0kaD2JPry/p3ugf8BMMmwZWd88grmjUdr+pQOrvZbLZc7Sb
UCTG5jMah5+x1r7s7h4c/t7dPQiRSNq28kFTUzXdXYNJ1z4hixWrjE50MX8wgqfIlbe6o75AmGOt
XoLhKKGIeX91dXnxZxhI2Xm4C38ognfAz9J5zoymfNwf6Qw0p/9IJ5RSPwS+r7U+Oi5JBMHCC/va
uPdRjT8YZc2yOm66Skk1+Ungog0LWDK3irt+sZtfP3ec460D/M216zKODgnCVEJrPfzUjyeieAOw
KcturUBiln7CddtiWQdQG5+P1RBf9wZgt9Z6u1IqDPwrcLZNW4l2CsJ4Hf1jGUG1RjQdPtXPWUvm
2HqSrKFPBnbplp0LH4mYbXmHRoocOzn3011DBIIRVi2ak3XbJKt9Ggwtp44yOCEcyVPo4zTon0LQ
6w1SWuxmMD5/LRQZPb/q8OkBwhbjdLJCZPN9lHAkys4jXXjcbrasnpuXNg+d6scfSjY2s/0WE6tb
uodoqi3P66DLWHA6LHM+0AZ8Xyn1uFLq3fEHmiCMCX8wwvd+vY//eWgfsRj81dWr+cd3bRbjahJZ
Oq+af7/5PDauamDPsR7+456XONFWuJE+QRgrWuuQ1voR4Mosmz4BLFFKbQWuAV4Cgkqpsvjg4VHM
bIFXAxXA48BhYI1SamW8fSO+7AngjUqpM4HXAY/l/8ymNlbDKRCOsO94b5rt7PdJpccbyDqRvdhj
qi2JUW2nNHd46ex3luTRKsJ0yLg2lrk7pzoHczjAmFbNWmKGgW7uZdfR7pFlNvZsuECeP7vbZTzz
v8LxQY9ILJbH0g2jlzn9bwDoGwzmRY7x4Mi801q3AXcBdymlzgDuBr6ulPoW8BmttaSWERxzrHWA
7zy0l45eP8vnV3PLteuYN8VjuGcqlWXF3Pb2jTz87HEe+tMxPnvvK9x89WouWD+/0KIJQkaUUu9L
WbQEWJRpH63100qpL2MmuGgB/gp4BOjDzBT4AeB/gL8APqG13quUOgZsAV7DTHzxMa31UaXU7ZgZ
B1+Jt/G9PJ1aYRiDYtTRm2ywRB0YI3aHsXqg+gdD1FWXpt3fE1eikmv5ZD3smJkOmcucGrDJO431
WCmJGcbWzIzG7ho4uo+ybHK6c5DmzkHOPWtukjGRK3byGcb4veBg1pDLR5igbX9l6Z+y4iISQ8RF
bhet3UPMq6so2PQHx/4zpdSlmA+jS4AHgL8B3oL5gHnrRAgnzDye3d3KD353gEjU4OrXLeX6S1fK
XKsC43a5eNvFK1ixoJrvPLSP//31Plq6h7j+0pVZi08KQgG5xPLZAAaAP8u2k9b6H4B/sCzaZln3
B+CMlO19mEWNU9s5DVyYk8RTmLEoykGHXqRs2QZz+ZfJ9R8pEo3lbIBZFdDp4MFKIkdx59VV0N7r
y9hHVmW31xtMrls2DQzQyWYs3hfIfuma417HQX844yDEWIgZBu4x1qOzSh6O5MnAsvndZRs8sBqd
R1vN2qlFRW7m1k584hA7nCa5OAwcxxzZu0VrnQh+3q+Uum6CZBNmENFYjJ/94QiPv9xMRamH225c
x/qV+Z6LLoyHjasa+eRN5/K1+3fxm+dP0Nrt4/3XrJmUuhyCkCta65sLLcNMYmL1ZKu3KflAMcMY
nqcCYxtFzyT7y7oj9wYtTAf7KsmAdbhPzACP201tValpYGXZNkFq2vpp0D2Tjq3zxYl312H7E+GR
SWe8ZDO8A8FoktzhaH7uCDuDNF+/Ra8vhKfIPeFztJy2fhXg0lofAlBKna21fi2+7pL0uwmCOdry
rV/tYf+JXhY0VHDb2zfKXKspyoKGSj550xa++cvdvHqwkzv+z89tb99Ifc3Ys5MJQj5RSjWTQRfR
Wi+dRHGmDAmFJBiO0t0fYH5DRVoPtD9ozpdqqi2zzbYVM4ys3utc5lpkShrR3pOc8S6bxyiNGuhY
FickzcGaBh6apCQiDuU1i8s6M2itxoHHnRJxMobuGQqEOdHmZWFjJbVVI54YfbKXOVWl1FWVMhQI
T+PnzhiNA4fXbrz2lb2HLXFPOG/8yOl+ugcCrJg/UqPU6wsxp3L8KRrG8rOz3cdm4d7jZq2/rWsn
diqE09isvwL+n+X7/1NK3QEg6duFTHT1+fnsD19m/4leNp/RyCdv2iLG1RSnqryYv3/nZi7bvJCT
HYP8xw9e5shpKTgoTBkuZiRteurr2gLKVVD6h0JEYzH0yT5Odnjp7Euf0KG910c4GqWle2h4WTol
PRCKcLRlgEiq5yKHJ38mg8UXTM4UNtEheakGiC8QHmXkWbO5ZfI8BEKRKTGZfqwZIF0uS7Bfhgtq
vWZFRZkV8P7BIMfbBjJu09HrZ8AX4mT7SFKlSDRGb3zf1w53cvBUH4GQfcrymGFw6FTfpPT9WO5H
u12ctOP0SOOtDWqXrTAcifHi/naOtaZeu/RSdQ+Y6RcG/SMe6JySp8Q50eYddVw7GceSQGNgKMwr
upMhi5d8snBqYF2utR6eUKy1/jPEcyVk4XTnIJ/7v1do7/Vz9dal3HrjhoKnzRSc4Slyc9ObFH9+
xZl4fSE+/+PXeGFvW6HFEgS01icSL6ASWBZ/nQX8pKDCFZDOPj+Hmvvxxw2WUNg+DXdHn582i0GR
bsJ7gsOn+uno83G6cyhpm3x5dowUMaNjaHc8kuw62s2xtoFkZT7JIEy/747DXRw42TvK+Jx0xjTa
bzgOx7QmLwlFYgTCI32Veuj9J3tp6/Hhy6DQJi5xxBJOZnfZI1EDXyCcdK/tP9HL9v3tdA8EOHDS
PmtlOk51DnLgRC9Ru5R+Nhw+3c/2A+05X990SS56vUH2n8ggswE9AwEONvcRClvStxsGrWkGQ8aE
ze5DcSOpPaVWX7pDWftkvP8ErT1Do45rR7b/HDujrGvATzga5VRH7obfeHFqYJVY07IrparIIUGG
MPs4crqfO370Kn2DId75+jN4x7YzJGHCNMPlcnHlliV89B2bKPa4+J+H9/GLp49Mi5AZYeajlPoa
ZsKlB4EvAT8F7i2oUAWmbyg4rDSnU8KOtiR7o0PxekjpElEk1jvJEJiOWBrvWOo6GJvHICdvmoM2
rNs4+b8bT9/kgySPm0NRDOKekPgNk3EOluX8Uu+fdPdZrl1i18+93iC7jnZzvHXE09U/NHav1anO
QfqGgvgCzor5dsXT+gdC6ZO5xGIGPQOBZIMjTZIL3dybVf6Dp/ro8QboHwoNL2vr8XHC4u0b7yPY
zlzM9bnenCeDJSdjcRznXVSAZGpOj/htzIQWP1VK3Q/sjS8ThFHsOdbNF+57DX8wyl+/ZQ1vOn9W
TomYMWxY2cAn3rOFptoyfv3cCb794N6k0TVBKBDna63XADu01udh1qia9fHHifAhe4/AaNUqEo3R
6w2m9WolPqaOj41VMUrdK7WdaJ4myTuRxckmjgy+Ao85jSXJhWEYjnPGjcWAzFVht+tnr880MhKh
aPkiVwMl09hwa/cQB0/1cbwtswHUPxgavTBVLutnSyOp3uhx3242AlrD/JwcK2AJ7fUOZT+3dIQc
FLxOBLJm2zLTdS0qQKp2RwaW1vp7wOXAz4AfAxdrre+eSMGE6cnuo93cef8uYjH48A3ruWjDgkKL
JOSBhY2V3P7e8zhr8RxePtDBF+57jQHf2P9UBSEPJIaCS5VSLq31K8BFhRRoKpBJjQjbKDORSAzd
3IvXP/J7TtZT0qSVGOPAc+p+qXr1qa7BJDl9gQiHT/ePGIe2IY15tnAs7YUj2Yun7jnWndYr0tHn
TzsgFYnGON05OO4QQyNTB1tIrR2WPAcrfftjMbByT42ffl2+VeN8RmEkDJPkkMjR7fc7MEKs95k/
GB0O97XZ0HZxOBKjtXtoTF7gIb8zr14Cq0cotVxDLr/H1PmPdiSyJo4nzC9RDsgqm9NQ0bHiyMBS
SpUBZwM1QC1wpU2RR2GWs/dYD19/YDcul4uPvmMjZ5/ZVGiRhDxSVV7MP7zrbLaum8eR0wN89ocv
J8WFC8Iko5VSHwKeBh5XSn0D8/k0q0mMttspkbYGlo3HyM6DlRrinZOOaq0rlbqjTUOvHBxJra6b
e+nq99PSlf6/JidRHBiMSfYKRlYDKByN0esd7WXpGwxytKWfvcd6bPc70e6luXOQExbvx9jI3gOh
cJTt+9uHj2VminTWeiaFPd2qXI1eu4QWE+UYzNUAyWRgJjwwxRaDw27zXJX51p4hdh7pIhYbPVcu
nTTHWgc40e7ldIbfSqb9c9k405SPMf41pKW2qgS3y0UoEs34W8zUVsJIs24yMDSxiS+chgg+CnwE
uJSRbE0XZ9tJKXWDUqpPKfVk/PsypdQLSimvUupBpVR5fPlNSqlTSql2pdTfjulMhIKy/0Qvdz6w
C4C/u3EDa5fXF1giYSIo9rj5wDVrufai5XT2Bfjcva+gc5xoLAj5QGt9C3Af8HHgbuAws6zovb0S
O6L4+ALhJMXVTjlJrWtktmv5nObYTrwApzsHOdY6kNGDZdUeF9RXjmojYQAm9rM9qmVhOGKGPKaT
0bqowzKx3rCJYyyJF0wNpkkYko1IXPlOV5A5GJ/bExxnyLX1LEdngTNJeFpae0zlO+HBStwug/4w
B5vtM/dNhgfr4Kk+m0ZyPqwj8uldS6yzdtFYPap2u0VjsVGDIOmaT3hRs95PNvunrYOVtjBCpk7J
fPhc8RS5h1P2R6MGMcPI2Ui2G0xIzWCab5wmqijWWl+WS8NKqSuArwItlsWfBaLAZuA54Bal1Pcx
53N9HBgAvqWUekDrcVYHFCaN5o5B7vrFLmIxg9vevpH1K6SA8EzG5XJx3SUraaot555HDvDF+3Zw
85tXc+F6CQcVJg+l1AvAD4H7tNY/KrQ8hcBOJ0rYK6FwlF1Huylyuzlv9VwAIhalxO1yETOMYSMg
uV1j1OfUAesjLdlLNzTHUzZbax2lCm1VfOwGxUcpfln0qv0nevEFw6xZWkdFWXHa7Q6f6qdrYCSV
fXd/gOb2Qc5aWjt8CE+Ri1Bk7Knjx5tO2ynWLurpD1BT4h517qO7Mdkz0hdPvhCOxFi3whwgPdY6
QHGRO/P5p1PM8xCGl1Di03WjCxctXUPUVJZQVZ7+WqeSj/lhI5jrrB6qsZ65nYc5GhsxJhY2VNLS
PZTVGMp219ntnd4TyXB9LK8vRK83yJK5VRn7xMAgFjNlL/a4iRkGHb1+GueU0dI1xPz6CkqKi5Jk
zoTLNeIxi8YM9h/pJhKJsfnMxuHQP6dtZR7tyS9OPVh7lVK5as0nMcMKD1qWbQOe0FofAbZjzus6
HyjHzAT1IFCCxNFPG7r7A3zlZzvwB6O8/5q1bFgpxtVs4aINC/j7d26mtLiI7/56P7965mj+50II
Qnr+AVgNvBaPiHi7NdvtbMBOUUwoo/64dyRJ8YsrRWcuqkUtrQMgYhO6FIkZ7DzcxcFmG68CpsKZ
blK8Hdb/hUy6aiaDJJOtYm3SFzTl2n+yNynU0EowHE0yrgBauofoGwoy6AsPy+seThiS/X/N7rxS
ZQ5HopzuGhq+boldQuHYuGo6jUoUksUgTBzfxWhl3DpfrL3Xx6muwYweEeuRrKm2nRoxvkA4fdhX
liYMDE52eNlzrNvRsXKRzRqSmun6J1ZZ+3ysj8GEd9FKLGYMy+vOFtOZOG62zXKYx3i0ZYAX97cT
ixnsPd5j/k4GQ8PnWGFTescwzBIGrxzsMFPMdw1xvG2Al3UHLd1DHLbU1UzOXmovgwsWVYgpAAAg
AElEQVQXifrWXn+IQChCJBbjyOn+5Hlqjuwry3XKvvm4cGpgLQYOK6WeU0o9nXhl2kFrfVBrnXrX
zwMSPdsLLIgvI748EWskQ+HTgKFAmK/8fCd9gyH+7PIzeN3aedl3EmYUa5bV8fH3nEvjnDIeevY4
P/jdgQmfOCoIAFrrZ7XWtwHLga8AVwGnCyrUJGM3ipxIWxC0pJZOKGhWRS2hq9nNwQoEI/hDEXq8
gZF9LNZCrkkZYknKZ3q1JpNe2NbjIxZLM0adg0ZrGFk8ElaPWryTHCUStDV2k89o15Fumju89HmT
jalAOMKBk71jzs7q5OztQiDtDFrbsEqMpDlGdgePxmJJ4YmHHRSnD0di7Draze4j9gbSiCT59QRm
u10MwzTcEmT21thsk8eBxpgxcm8lMuGla34iDIZE8hurkR0IRUYNQljZf6KXUDws1jBG/8dE46nt
9xzrTsoamnEOlWv0/1rvYBB9cmQQKKOf0Uh+z7pDHnAaInjHhEohTDvCkShfv38XLV1DXLFlMW86
f0mhRRIKxMLGSj5x0xa++rOdPL2zFa8vzC3XrhsOARCEiUIpVQtcB7wDWAl8p7ASTQ6JkB3bkfhE
Hayk2kgGuFzDSqDbNTIaHrUxlmw9IBY9yqowuS1ypAvRyTS6n/heVuJJ8viYSRhcScZhuvCo3PQk
w3beWQKXRabcPFijt0l1OCSOaxhmem9vSibWSNSgxHmk2wi5RVGOeLBco42sdN6vYo/bfr5e/N0u
vC0difsk8Z5ujlq6EgHjJVvI5+hMl5k8WIkQQWde2lyxhgg6vR9dGQzSgaGQ7TW282SnUuR2E43F
CIVjxOLHcdl41YYsGRVjhoHHk2ycFxe5h+fcWT3h5v0w+n/NZf2/SpHdWvTaeuNXlHqS5lgVIrbG
aZr2p4AqYEP88ynMzE250spIlqdGzPlZrfHvtfFlkDxvS5hiGIbB3Y8c4OCpfrasnsu73nDmpMWa
C1OTOZUl/PO7z2bNsjpeO9TFl3+2MyVtrSDkF6XUo8Ae4Fzgs1rrNVrrTxZYrAnnZNsALx3ooG8w
SM/A6LAyuyii1In4Znpuc8OIjbJlV4vK2qzVS506gp1IR21VYq3HSDXCEt82rmxI0qRjMWNUaFq6
ULVcHAa9g6GMhWYNi0yJvnTSvn2+Ecv5WDYIRaJJhWPHy6hD28li42DJ5MFKVeIzZY0DZ/WMMso3
vg2zt5Qpk2UKo4pfZ3SNjOyTru/GQ2eff5Qxk651q0Ha6w1yMuUe6xkI8Jru4FTn2NKdJ+6BmGFg
xLMbZp3vZZjGuZVUgytBot5XqgHscrlGjp1l7hfAuuX1rFmWnGitucPLwea+MdWMGytO07R/Hvhr
4Ob4oncDd2bZp1opdQZQCZTHP/8eeKNS6kzgdcBjwIuAF7g+/goAz+R+KsJk8bsXT/LC3nZWLazh
A9esyfrHK8wOyks9fPQdm9iyei4Hm/u440evjWtegSBk4WvAMq3132mtnyu0MJNFe4+PmGHQ1RdI
CmMawUZpjislwyPh7pE5DXYeLNvR7KQQQcNuMWBGN0CyEea3GDSD/nBS9j6s3hSSFw85nOfV1uPj
1YOdjsKTj7b0092fvnCtYcZkAZbUzk48WPG+7e4PsONQl2loWo0qi3HYl6borFWx7/UG2Xm4y1kK
9xwV+nSJSxKEI9FRTaab/5Noyy5ZStrjO9xueEDAccvQPxjkhX1tSYWzU4+ZPUTQfHei1FtXjTUZ
Sia6+v3DxkxCYTcs6461DliOO3J83dxLS/dQUjiv1ze+Qc/ELWDOCzP7J9vgul1B63Q6Y6KcwSgD
i/QeLDvKSoooKhp9jB5vIKk/JnrOuNM5WJdprW/AzPKH1vo/gXOy7HMjcAi4AjORxSHgCcxizK/E
P39Paz0E3AJ8DPg34EM2c7eEKcKuI13c/+QR6qpLufWGDRR7JAxMGKHY4+aD167j9ecs4lTnIJ+7
95Wkic+CkC+01r/VWo8vv/U0pLTE/M9NTdKQwE53iRkGhmWE3W3JymU3B8tuWaLZQCiCbh4pzZBO
wQpHRtqwytrW4+No68CwNyqxlcvlSpI9GI7a1MyyV477h4KEIlH60xguqVgVq/rqsqR1McPiwXKP
jNhnb9N8P901RCAcobPXn6TUW22//iH7gSfrcXRzL/5QxDbxwahjj5IleYk/GEkKl0ooqUVut/39
Eht9ztkGUlMLz5cVZ5iB4lSvHb45HG6PmdwE4HhbSrp6yzFPdw0OG7yRaMxm7luif5xc/5F1iX7N
ZyHjRHtuywhE4voePt1Pe6/PUcKZcCTm6F5Kh2GMzEm0ZhZ04sFy2huJgZ3U/jMYMe4yGVgju6WX
azITcTmdg5X4dzQAlFJF2fbVWt8D3GOzalQ6Xa31T4CfOJRFKBAtXUN856G9eDxubr1hA3OsqXcF
IY7b7eIvrjyLmsoSfvXMMe740av847vOZlHj6Bo3giDkRjZF1271jsNdlJd4qKoojm8zMvIcspn/
YufVSrTrtChutoGVQChKaXGRqbjZqEMHm/tYMrfK0bGG97GrpWSDdS6RJyV5g2HRCEfmvGRvc0Qp
HFGyrft19tkbxEltpFEeW7qGiMaMtP0xes5Q8vedR7qSvo8YWPb3UswwcBvJ69J7sMx3a/KBRBup
9A8G4wasMyV32NOWg4VV6ikiGIlSXJQ8+Jt6zF1Hutmyei6v6E4MDLaunW+R3XwvcpvzzjJdf+u6
4euXZx0+Zpj97xqZYJlE4nrazVlLLNtzdHx+C4ORwtSJcEi3K/v8uJgxelQk0z5DgTADQ8nGupEw
MHHmJbSbWzjcVlK7WZsaF049WM8ppe4GFiql/h54CnhywqQSphxDgTBff2AX/mCUm69ezYoFNYUW
SZjCuFwurr1oBe++4kz6B0N8/kevjooHFwQhd7IpBekUC38oMjzHwRoiaIfdKLErjbGRTp7+ocze
pERB29R6TAlCkdEerHzpQ1YPXaqREbFkKrTOOcnGyMi4ff878R6kUx5Pdng53TWYvv5Raj9ZvtuF
TQ4bWEX2posR93hayZYiPFV0O1n3n+xFN/c6VmxT2+xwYKQmQsNKS1IN5+TtEt4SO2NvOEOe27lS
DxYPlqOts1NW4qG4yD0y38nevhoOy7UjMRc6XSIRO+yuXSxmWP4DzMEDl6MQwdx+t7uPdo+an2gY
1hDB9L2bKrfd3T0RYZzpcJrk4hPAbzDnUC0Gvqy1/peJFEyYOhiGwfd+vZ/2Xj9Xv24pW9fNz76T
IABXbFnCX129miF/mP/+8WuOipMKghOUUpuUUi8rpQ7Ev9+ulHpdoeWaaDKN/nvc7owP9URYntsy
adwOuxDBdJSX2oeJG4ZBaYYQ8sScnYSilvicYE5lqa0i7tT7ATCnooSzFteOWm5V0lLnahxt6R+l
YNvJkcial6gDlFDchpVgGyMlG9kMuXSZ+npT0r5blchUzxKM9H16D9boc0637XBGwFFGXvp0/k77
JRyNy+4yEzQcdfD8SCRoydU7kVxc23xP3BvRWPprGUsyZhMerPEr8QvqK/G4XWYWQYsHJyGrdcDy
aGtyOKTVsNh/sjfnsgp20huGdcAhESKY3YOVy+81EyNZT515sKzvSfJYds+XbOlwmuRiJfAq8CXg
LmBHfJkwC3h0ezM7DnexZlkdN162qtDiCNOMSzct5P1vXUsgFOWL9+1An+zNvpMgZOcu4H2MZKL9
KfDlwokzOdjpbkvnVuN2uSgpLso4opyYa5IIoUkXemUXIminYC6bV03jnOQ5TEdODzDoDxOLYZvC
OYE1ZbndVmUlRaOPaaP4Z8LlcjGnKnPt6XSGA1izCI4+aELZ9wUjuF0uosPhbIl9nMuZINvoemoW
Ra8vREevj87+ZM9OLGmf0dfy0GkzlNJUWu0zCeY6BytV8kgsxsu6Y9i7Mt55SZmKHVtJDZcD0zDt
6B3t/bIzqiLRGMfjYbCe+A3Q0edjZ5paXVZiNsceC/PqKlg2v5oit5myPBr3HlkHIlq6R3tE0x02
lxT66RoyGDFY+oeCIx6sLOGbMeukxjFiNTCdzMHKJJPdNZ8onIYI/h4zKcUTmBn+NPDARAklTB0O
n+rn/iePMKeyhL+5dl32SuKCYMMF6+bzwbetIxKJ8ZWf7RzOFiQI4yCstd6V+KK1Pgikz789U7BR
Clwu01AwDCPjf3Rq0eB02zrJ1AVx702K4m1gsOdY9/C8iTMWzrHddyTLm32IIOQnnCebYVBkU0B3
OItcBg+WNQTSU+QmEkl4sJyFFVaUji54lThdO6+TdX2Cvcd7RnkvTHlHNswUPhaL2fe9YeOxSXev
tPX4OHCiN62Hxx8/F6vR3ptjdlknWsfpLjNj3nDon0Wek+1e24ybybWrzM/H27zDSUiKLHG0iZDW
VGJJCnvcwErZpqqsmKryYhrnlDs4kxGsSVbc7vQhgoljp7sGuYbn23l2otFY0nWIxGKmPJaFdr+1
Y61eugbSZ+10JI+RPeFMrzdIX0ryGLvBpskLEHSY5EJrvcL6XSm1DjNtuzCD8fpCfOvBPRgY3HLt
OuZUZh4JFIRMbFk9l2KPm2/8cg9fu38Xt924gfUrGwotljB9iSilVjCSfOlqcsvoPC1JF9bicrnw
hyKUOijwndA7zBCk0eudFB1NHDMdkViMMlcRJSXp5Rn0h+PGi40iZOOtShQizYV0MtZUlLB0XrVN
BrmR0LZMWeTKSjz4gmHKSjy4Xa7hdhJKbixmZBwhn1NZgi+YnP3N6wuNzn5nxeGQu9UwzVSfam5d
+fC8vKT9jdFhhx6btNcJ+oaCw6GSqSSU7tT2csHlyn7qzR3epGtp3TyQzmC1MeD9lmyL2QaU7cIi
7ZYXFblZs6yOjl4fXf3Z55HZHb/ImrHPpjM6LaUHUu/XdAZtajHeDM3bJpBxkT1EMPUeT9d+JlIT
bNhhzWya6Cg70U51jK0G2Fhw6sFKQmu9F7O4ozBDiRkG3/31fnq9Qa67eAWrl9UVWiRhBrDpjEZu
e/sGXC6484Hd7HIQdiEIafhH4EHgIqVUP3AHcFthRZp47PQLl8s1rNT5bRQmu+1hxHtTVpJ9rNX+
uJnNHZc781yvoUA4Hmpkc7w0hmS+wnpKPEVUlRcnGWAetxuP282AL0RxkZuKMtPLZFfPL+HcWL+i
Hk+Ri0gslpQKPxoz0p5DWbHH9py7s4z0Oz11ax+lm7OyoL4yyUOTvL9Bc0ox2opSDysX1KCW2OsC
6byeCcXYHxxfRQVr63VVpTTZeIMClns/Eolx6FQfvkA4rREQsBpkFsM4Qabw0VSZzO/xNlJWDBsF
DmuGjmw+sr3bnRwimIp1fprTcMwNKxs4+8ymtMfPRmqIoNOaqLnOfbLO03QkV4Z1g4ERg2+iQwQd
ebCUUv+RsmgJMHrmqDBj+N2LJ9l9tJt1K+p5y4XLCy2OMINYv6KB296+kTvv38Vdv9jFh6/fwKYz
GgstljDNiIcHblRKNQFBrXWGof8RlFJ3Au8BOoCbrUWKlVJvAr4J1AHf0FrfrpS6B3hvSjMrMMuQ
XGZZ9nmt9b+O8XQcY2AqMlvUXLYfaAdMhWJeXQWnugazKldWhSihs5QWF6UNgbIeNxUzdXR63GRR
Uo14FkG7VTZTN/KpECXO3SpeWWkRvkAEolBS7KbEYxogdl4ewzBDyDxF7uFU773e4LBHIByJ2Xba
4sYq5jdU0Nade31A59n3sm9Y7Ek/vm63v8vlYm5dRdq204VzJpaObw5WsgvLlcayt16lSCxG90CA
l/a1j6rRlWDf8ZFQ9YT4qWn7M5LqYTVSP8TbHmOoq9WmcLtHzjlda4nDOjnenMpSXC6Xrcfbqbyp
SS4c20C5erAyhD7bGXUJY2yyEnCkw2kdLOvQgwHsBD6Zf3GEqcDB5j5+8dRRaqtK+MBb1zoelRAE
p6xbXs9Hho2s3Xz4+g1sPlOMLCE7Sql7sXlEK6UA0FrflGHfK4Bbga2YBe6/CWyOr3MB3wV+DvwW
eFwp9UB8u1vjTXwYeD9wKv79v4DPxT87q3I7XlLmBwFgUXSsnoTS4qJRyQGsSkVi20zhXyM72ijd
2Sa4p8qZ2iTJ2clSV9rNKclFKcr46HKN3sjtciXNUyspLqK4yCbZBvEsaon94udoDaOKxGLDiS+s
VJYX4ymyL/CbC3ahjSOyjXxOZ9gkjEc7OY6cHqC4qGgki59lu3Rip9PJR8Lm0oo7cgxcttfX5YK+
lCLSdvdewIH3Nh121zhb9r10ZQRSm0oYLE5Nt0QfuFM9WBlkte7nxECy/iw9bndSWPDpLmcFiVND
BJ16mbJJl6jZl6gdl/Y/wpGE6Uk31zFfOL3e/2l5fQa4E2hVSrmVUmMKMxSmJgO+EN9+cA8AH3zb
emoqZN6VMDGsXV7PR96xiaIiF9/45W5eO9RZaJGE6cETmImX0r0ysQ1o1lpvxzSiNiml6uPrVmGW
IXlYa/0EMAhcrrUOaq0HMQck/wn4lNY6ocmFtNaD8dekGFhm3ahkxcGF/STwsizzsSrLzDHW8hIP
VWWjky5kw+3GVodJhBwaMYPS4iIWN1ZRX102artEPZ3hOROWttIaUjkMOtfXjD5mArfNKLc1QUUi
A2JJsdv2kDEj+0h52MbzVVKcMGxyVxgTinXPQIBXM/xfOkmD7sngwTIwkowrGPFEppM7XX2ik+1e
AqGIIw9WJm+n1z/y80qXHjycYzpyKwnxrAMUqQZWVsMlTZKLxtp4OOM4jOqiLCGCVhwZWJa+Pkcl
hwl29Dn0rqaECObLg1VdUcLChsqRzQ0jY1Hs9Pd75gMN+EKOQqrHilPjKACEbV6R+LswA4gZBt99
eB99gyGuv3QFZy2RKFBhYlmzrI6PxY2sb/5yD68eFCNLyIzW+geJF/AK4Ad8wAvxZZmYByQmKyRm
Rc+3rCNl/QLLvrcCXuA+y7IblVJHlFK/VwkX2gRjm9Y8TV2riixG0/L51ZyxcA4LGitYvayONcvq
bbPbJY6752h3UqaudMq2J8XYWzy3inn1FcPrk+f+GJZ06MnHs9ObnNpXakkdTbXZs7YleQmsIVnx
dzPBgr0HK7F9utF1O4W/Mn5NxuPByqYURmPG8DbpdM9hA9OB1u/CRXmaJBbZGPCFOHCiz5HSny48
L7V/ncicK6c7Ta+N1RBMrQfXnJIgYVQSFpskF2uX1bOo0TQWHMud8FKneFft7pnq8tGD4Onmw1WU
emwziI41Ssk9KkQwP3OwUpsp9hRl/L04zXpqhy8wcSaM01/Mp4F9wGOYl/6twJla689MlGDC5POb
546z51gPG1Y2cPXWZYUWR5glqKWmkfXVn+/iW7/awwffto5z1dxCiyVMcZRSXwCuA17C1IfvUEr9
WGt9+wQcqwjTwPqK1joxtP+7+HEfAv4Psy7XlZnaqaurwJOh+K4TjncOMWdOOU1N1dRUm7ZgY0MV
sZhB99CIsrDpzCYi0RhDNl6Upqbq4c8LU9b1ByJ4fKNVg+qacgaCUWqKR9bNbaqmZDBIx0Cy865h
Thnu/gDFHvfwsYrLgtT0mCE/JcVuQuEYtbUVeEMxSouLaGqqJhCDPr9pGNTWllNaUpQkf21tOUVu
F6GUU6qpHm1InbWy0bJ+dIHa+vpKmpqqKfeFqOkyR+zr68qJukwlv66mjKamamp7/BQVh5L6DKC6
bZAit4umpmr6A1H8kdFKXlV12ajliXbCuOj15TZ6XldfSVNdBYPhGP2BZA+TNbzRHzE41jHEeWvn
UVsbJmCT6KKpqZqayhICoQg17Zkzq61cNIe5c0fO364/U1k6v5qTbSPpwWvmlBFJY2A01ZVTXVFC
OBKj2SaleF1NKa6Bkd+N+Tty2/a5HXb3Ryohw+yT6vZBSuKhYxvPbGTXoa7hbYbCsaT7IBSOUtPq
Hc5yWFdfSVNTFf3BKIPxm3TB/JrhgQ7DU0TNQPZsirW1FTQ1VeMNjfx+GxuqaKgtp6bTR21txfDy
2upSKqpK8QdG7qXyMg/u4tG/4aqKYgKhKDXV5dTXVSadi5NrmkpdbTkVZZ7hc60sL2bIn2ywFBW5
RiVamTOnnLCR3mKqr6+ksbGSmg7T6D1n3QKKPW5qT3ttPaF1dZVJ1zhxXjWt3qw1wFz/n73zDpPk
qg79rzpMT84zu7Mzm8PdHBRWAgVWASFARGEBFsHY2NhYgG2Mn7Gt92ye7WdjsonGQoBNECIIkCWB
IkIIaZVWq013tTlNzjM9odP7o7p6qnOY7umemfP7vvmmu6vq1rm3blXdc0+4hhF3b+eLTBWsa7XW
/2T7fpdS6mFMd0FhAXD41AD3PHGShhoP779pk8RdCXOKWtHAn9+yg8/e/SJfuecgf/wmM627IKTg
WmCz1toHoJTyAE8CqRSsTmYSNFkj8Au2bQD14XisJtu2KzAtXD+3CtJa/4v1WSn1APCudAIPDmaf
2MDO8Pg03kk/I6MT9PaOMjJqKiwDA2MQIvIdYMo7xfD4dNRvFr29ydfFGRmeiMq0ZeFxRpffWl/J
8JCXwZHJuHM0VrkZGZ2gvMwVOdeId0aWcreLSZ+f/n4nA4PjeFxOentHGRuZiOzjDAXxlDmjynaG
gjgdjshvBgY1NeVR363ZcXsdVzRXcuLCcFRK6iq3g16PE++kL3K8xzFTRxchs41HJhjxTse12fCw
F5fTQW/vKEND3oTtbAQCcQkWrHIGBxMfk4r+/jF6ekY5mSCVu1X32pqKSLnnLgwnvD4AgwNjTHnd
TPkCM3WOicWJ7DvootxmXMpE7qHy6GuXqC0s6sqdlFeX0T+cuE1chBgZncmw6HGY1q5M5LC3RzpO
nx1kaMi8rjvWNeO39Q0Lez+w2s7pcBAIBunvd1FGiMHB8chxfX1jEetfsmsRS5kDenvdUf1quNIF
fvN85U5jps8HAnin/FHW0pFkt3cgQFl5GSOjE3ic0Fvhsh2TXK6airIoF00LFyF85a7IsUG/n7EY
BStRn3KGgoykWAutusyBxwhFyh0aNBWtsbHJSFlbVzdxoW+cgdFJuntGouS3rtHw8ETaJScMUj8P
MyGZgpapi2CTUup1Sqnq8N9rgfjcjsK8ZHB0iq/97CAOw+CDb95KjcRdCUVgw/J6/uKWHZS5HXz1
pwd55khPsUUSSpsuohcWngZOpTnmIWC5Uupy4CZM69eUUqpca30COAG8EXgtUAk8GD7uCmBMa30I
zIQYSqljSqkvKKXageuAffmpVnK6BxIraAZGvHuOEePyluGkWTI3H7uLl8vhYM2y2qRltNZXsHJJ
DcrmZm4v1XJPstKST4UXw22qK6ejpTqyX2IXweRptC/dlHhSprrCTX21J+q3SNKGKB8nm4wRFzpL
lpiEBhnEYPlTuC65c7FkhuwLNMduSp3FLxYjpn6mTPkLqY9tktGJFK5YkXbMcGI3SQxWIlYszdw6
sf9EH/5A8ox1bqcj2oISceWL3i+XhIntzTP93irXXsfGmvLI91grzlKb+20sbqcDT7ivuZwOKjzm
52zcLJO1tcMwotw6E6XOz2Wu3hET2xX5PcqtcabsZPdZRq6DBbQlZHo3/RHwcczZvAuYM4QfLJRQ
wtwRCAb52s8OMuL1ccs161jbXldskYRFzPqOev7i7Tspczv42k8Psvdwd7FFEkqXPuAZpdQnlVKf
Ap4GfEqpTyRYWgQArfXjwGcwE1xchPkeu5+ZuKo/xFS8vgX8bXjNRzA96bps5YQwMwreCBzFjM0q
2hpchpE4W59h+y3dmj4zByX+2b5GU3tLVeKdwjgcBm1NVVFxO/bBs9MZrZi4nTOJH6zg9oyyzsWM
3rLxvEiU5MI+UI1VwOIyw9lisJIpBv4U7kked/bKTIjUySmSHpSARP3BmSSbZE4eLTHHpEpyYe2Z
7DSxym02ykFjbTkdduUlDanig3yBIHsPd+PzB/H5g3SHLdJW+1jjebu4dgUkVRtYCWfs2PuV2z2T
eTK2PVJl6vS4nZEGdjgM1rTX01RbnlIpA6KS0tj3dcRMSNj7jMvpoL4qeiIj0QMl2cLHkSOMhIfF
9MOZSaVka70VOg17OjJyEQxnXLpKKWWEXyzCAuHHj5/g6NkhLlYtXH9JR7HFEQTWtdfx0bfv5DM/
2MfXfnYQnz/IFdva0h8oLDYsi5PF/2RykNb6o8BHbT/tsW17BFiX4JgPJfjtF8CGDGXNC4ZB0gFz
AgNW1IDE6XBklGUt3fC9rrKMtqbUClbac8QMSO1Wq0zX+oFoJWH7mqaU50xk4Yv93WVLvuGIZM2z
5LGlO6SwFiwrRXpjTTnTvkDEZTPETAIR+36pSDbIjK0fmIrLitYazvTEuEzlol9ls28aRTVWLzGz
CGZ2BqfTQUdrNZ0DXgLBIJUeN9UV7pSZ8tKl7+4a8DLmnWY47PLocjlMK6yVRTD8f117XZRVMJl+
1VxXQW1VGRVlLiam/bY07TP72K06dmtyiPQKsHVep8OgtqqM9R3pE5jZi6ytKqOmsoxR7zROh0Ew
rNAYRrQCGTvRU1NZFtWWy5qquNCfPgV8smtrz41jzyQ5m+yRhUiYYpHpQsM7gDuAamCjUurvgAe1
1k8XTDKh4Ow71sf9T52htaGC9712U05pYwWhEKxtr+Ojb9/FZ3+wjzv+5zAj3mlee5kkXhFm0Fr/
Q7FlmGtSDQbiMq0ZRtQAzek0Msv5m+Y9UFURnWUw0/eGfTdLMYrMxCfy0rNSuNswlZqZ7/YBV7qM
ibFSJnKRs8/GJ7JgDY1NRdawMtPlR+8TS6p06W6XgzVttZzojI6nunRjK4dPDeILBAjEDhxjFlxV
K+o5cLI/6TksuRORbFBeXRHfjrmMDPJg9IqQqB0zLd9qLiuNfGOth0qPK6WClS775Pm+saj2syyw
setgxYZbJKpHQ7WHdRl6Ds24CMZuSH3csuYqzvWM0VgTa11KTpRLsNNhs/ja7rrOgY8AACAASURB
VBGMOEuo1T9dDgebVzawz5YkpL7ak1DB2tBRH7WGXCqXRPs+1veR8dxXyCjksDfTJBdfBH4f+Hz4
+w+AOzH90oV5SN/QBHfcewi3y8EH37yVygTmaUEoJmuW1fLXt17EZ37wInc/epzhsWluuXadJGAR
AFBKfRz4K8AKBjKAkNZ6dmn6SpkkFiwjSQrnKLe8DF0E0+2W6/0XpchYadzD+kPUoM2ybpHexWc2
z4IZt7TEbRRbdv/IJCdjlKHIsUm0mFiXsPXt0ZaDxtryOAXL6XBQW1U2k2jEJkYo+akoL3MxOR2f
lTCZkjdTvZkTdLRWJx6s59DO6RRve/KDRMqunViFwjCi97WsK4mwp6MPEaLM7Uwr28oM4rbs19ay
UkVS4yewQEHmsVnWfvGTJtb2WJfJ1CxtrEzrEpiMSFr3BF3dMIhL329PA28+l+InLWJJ6OqbqK2i
JmlmXCb7hrNLFmMnl3i5TMnUmdentd5vfdFaHyU6uFiYR0xNB/jij19ifNLPra/ewIolhUlRKQiz
pb2lmr9998W0NVXyy2fO8p/3Hopb/FFYtLwH2AmUhf/c4f8LllQDKbtlw7J0JbIaZcPKJTVsXNEQ
LUPOOo1NeYmxYMVZlwgPsGItWEQPLhPFnly8oYWLN6TPQDpjfbL/Fi+j9ZN3Mn7Ik2jQmYqmuuiF
j5O1ZUdLNe3N1ayOTSQScx579Ztqy9m0spFMSaRk1FWVJexjuaS+iC2nrspDc+2MZSi6vyaXCeIV
CpfTEdV4tTZLUXNMooWy8GLbW1Y3sqShkua68rSTCFkTLq9/ZHJm8Wzi65NQZ0ig4CeKD7SfyK7c
OYwECW4SyJYrlixT4bTwdpfUeBdBI2JVjljAktxfqTAcRsLJFSvWyuN24nY58uLeV8g4rUzvG79S
ajXh/hHOIijTyPOQUCjEHfcd5kzPGK/auYyrtktsi1DaNNaW8/F3XczaZbU8dbCbT31/36xcAoQF
w0HgnNY6YP8rtlAFJeU4Kn5jVAxWkkVc48qJOSY2s1yqgPrU5c58tsq0hjbx7nvmwCfd0CeRBcvt
cibMhhfnVWVED2YjxzvNAXlNhTtqv0SB9NaCyamSF6TCOnddTGIAh8NgeWs15WWuqOuawFGOJQ2m
ZaLM5aCuqoxVNqUslMDNEqCizJ58JKbEhKbQtFUx5Y5JgBC9Lfq3qH5kRP2LI9aC1VgTrSTFxipZ
cly0viVynuoKN6vbatMrJDFYbVWWJGauqtwdlRBifNKfdFHldK6Oa9vrqK/ysHxJdXhbYguWPfN4
bRKleLbEKoneqXj/4thnTigUmokTSzJ5kojYy+FIUDbMLPxs3S+JJo0SJTTZtKIhTvGeEToDAXMk
U7+wjwI/BZRSahgzFe57CiWUUDju/e1pnj3Sw4aOOm599QaJuxLmBdUVbv7ynbu4495DPKt7+cS3
nuFDb92ekSuHsGD5FrBfKfUcNo8KrfXvF0+kwmIk8xEkPgAcomeXM7VgxY6RY4+KVUim/TM6rcfl
ZMOK9AH0VeF4qUDERzDBTgksWIRChGIsYbnasyPViDn3ltUNDI9PUxeT1j1R5rOIopjjIM0wDHZv
WoLDMBjxTkdieaJ3mvloKkwh2/GwamkNDTUeaqtMK449fmjU6yOQQLgNy9NfIzu1GS7d4nQ4CIYt
HLGX1OlwRP3mcTsjLo3pLFixCqzDEePOabeGGbBzXTMT04GI9SqWbIY9W1Y3MjHl52zPWFRft9i2
polx27pxVkycQXQKc5jp9x6XM7I0gV2RqPC42LhyxmKczFvD3gfamiqjMnzGkquVxzqD1bRNteWR
81jrfsUSDIZs1unw+TM4ffwEi4GnzEl7c3WkXwNUV7gYHAvgKTOva+xkz9bVTVExhMtbqhken6a2
qoyeocRuhIXM2pepgtWntd6ulGoBprTW8avcZYBS6vcwY7csuoHLgLuALcAjwDu01rk7VApJ2Xu4
m3seP0FTrYcPvmVb3M0vCKWMx+3kT968lXt/e5p7Hj/BP//3c7zvdRu5fPPSYosmFIfPAv8FnCu2
IHNFqsFKImuOfQCSsYJlG+4kOiL2NE215QyOTNHRWp0wQUKi42JTlMcOAg3DCOtXaWKwHAaZalix
1gPLyhDbbuVlLsptFh5LCUg0oLQULLsCYGDQ0VLF2d6xjOSyzp+pEhMbA2MYRtQaX/b6dA6kz9gW
i705GmvKWd9Rl/FErNtl4LN0kNi4mhi3r6pyF8PjU1H7xp57zbJantU9cdfO6TBi1kSKVrDK3M6k
ypW5T+ZKh8vpSLs2aKLSXAlS3tdWlbFjbTPT/iCHTw8kPziM1Q/bGs2snVY9J8J9cklDZTiZzewn
yu2LdAORjmYt9bC8tTqiYDkMgwDELeJrX7oglMA+bU4I1NI14I2OF0xiqVveGm2NWt1WS8P4NE21
Zn+PVbBin3HtLdW0t0RVJ45UiWhmS6YK1neAa7XWvXk45xlMZQrMR+N/AAFMX/ongQ8An8vDeQQb
R04P8p/3HsJT5uRDN2+PmhUQhPmCYRi84ZWrWN5azdd/fpD/+Nkhjp4d5pZr1kYNioRFwbHFmEkw
GekGjblYsMyxUfxA2Y7L6YiadU9abtRAK/GAyn7aUCh+UBQIhQjY1pZyOowEKdUyY8oXbY2oSPL8
SKBXRShzR1uwylxOLtrQwuS0P2MFKx32pjHbJFqZi9s/g+tsb++4FOgx+2WjjNRUljHtC9LaUBEX
f+JwQDA445YZpRRFzmd3TzUtQAZG3DVwOIyIeyYQNZ7JxGKTq0tncuLPmcwlt8LjwheYcXFP1bwN
NR62rWmKWL5yMUZlOtYzjOi+EGvBsk/ItzZUcL5vjLqYsoOh+HXaYi3iSxsrCYVCnO4ejfrdTjI3
5DK3k9b6xHF8pozJGyhX1+bZkOmI5KhS6tuYClCkZ2itv5HDOUNa68iTRym1B7hDa31cKbUXuAZR
sPLKuZ4x/v3HLxEKwW1v3SZJLYR5z851zfzdey7hy/cc4LEXznPo5ADvv2kz6zpkoexFxNNKqX8A
fkO0i+AjxROpsKSMZbcPZNJYs1Kfwz7wjc5O2NFcTUMWqZ6jC87snOZ3SOS8MzUdiFrzxhyk5zZY
tsfU7N64JGnbphqMW7E3ZeFBpZVRLWH75yH7YigUiqy9ZJ4nfv9MLnOixAoza4BFX/9EbOiox+cP
crIr2pmpsbac1W1mDFhsZjeHYRAyZqyGdkVwRsGa2d+Syxz4x7gIGtEWLPvgP5N+XltZxvKWaroG
vBmvoZSql0XFFzrN9eZcOViME1FlW34g2Z7JlOBNKxupqUy9fEE6rH5rn6Bpb66iqbY8Lvt0MBii
vCzacphItLh4Nts+tZVlKS3hdpwxhduV7lhWtFYTCoWY9gejMk4WMotgSgVLKbU9nD3Qg2llej1g
JbUPAbkoWA1KqacxU+t+ClgCDIe3DQIbcyhTSELXgJdP/2AfE1N+/ugNm9m8KvMsQ4JQyrQ1VfG/
33sp9/z6BA88fYb/953neO1lK3nTlasTBrkLC46rY/6D+V5auApWyhisxK59q5fW4p3y57ReVSwd
rfEB5JkSaxlJt3eigU/sYDhXz6h1y+qiMvqlGpSHUljIrOPamisxDHNmH5K5jM3+mTQZswBuYgUr
AwuWfX+HwY61zZFnZrwFM57GWrPtLAWro6WaJQ2VUc/dWMWhsbacnsGJyDmjntFG/Onsg+VYJTd2
jbdE8YfpaG+ppsLjilp/KRWZKkxWH03Vp7K7F+z7Ru9sxWglKyPWwpS2bFs7Rxz8IoqumVClvMyJ
w2FEKVfWgtexWQUhth+ElflYK5ft88YVDRlPBsXul+q4MreT9R31dA14S0PBwrQkXau1fh+AUuoR
rfUbZnG+Y5hraH0VeCvwNWDhrllSZLoHvHzyu88zPDbNO69fz+VbJFZFWFi4XQ5+55p17FjXzH/e
e4j7njKTuLzz+vXsWNdcbPGEAqK1vib2N6XUzcWQpRSwD6ztsRFLwuvfjHincRhGVuvhFCoHUnzM
Vfx5Y1OyJyzHMNixvoWR4eSLxlrYY3Ka0ywka8c+uK+r8szEDdlwOhy0t8won4mU2ZwVLFtZgQxW
mM1EkY7dJ3Yto+SlJyFE3KSW/RSbVzZSXeGma8C8Tg7DoKWunBMXzLl1Kzuc/SD7YDlRN7D/ZFfG
Zpu4q9KT2HpiuqBHX/vW+uT3UqZ9LJflEyyshCb5uE1jy2is8TDqnY5anNiyTsayeVUDXQNeM6Ol
ATUVZbTUl8cVbF2a2Cr7bRk6s7l8ubj9LWmowON2os8OAuEFw7MuJTPSKVh5Pa/W+gngCQCl1Djw
N0AnYKW0aQYu5POci5XuQS+f/N4LDI1N845r1/HqS5YXWyRBKBgbltfziT/YzU8eP8nDz53j8z/c
z/a1TbzlqjWSaXCBopRaAdyG+d4A09PiWuBHRROqwMxm7FhbWcYlG1vTWjiSLW46W1JZRuJcBDGT
S1SUpZ5/NYD6Gg++yfTLNrTWVzA8NhW3FlU6LJ2mrbGKlUtreOZIT8KEF1FyxdTPYRhxAfuZ4rEp
hgOj0dniElqwsozBSrktTVFWYoR0MU0z6cXDLoIOywplEAyFmApb5hK7CBoEQ/Htbbk0xvbXbMbc
iZSx9UnczNtbqvBO+nC7nPSNmJa41W3muyXRREAq65H9vJ40fTwVkeQmtvLqKssY9k6zrKkq53LB
9BCpr/YkVb7tVHhcUcrXltUznlJ+f/y1i0tOYYudykZBLi9zRvpgpvU1DCPazbmIFqz00yVZEPaX
vxW4DtOC5QMeAG5QSv0XZkbB22dzDgFOdo7wubtfZNTr45Zr1nHD7hXFFkkQCk55mYt3Xr+eq3e0
8Z0Hj7L/eD/7j/ezc10zb7xyFauWJp59E+Yt/wXcD7wB+CLwJuDdRZWowFjjOLU8fVKJRGQbB2QY
iV31csHtcrK6rZaqcnd8Wua4E5v/Ei3um/rA5DgcBmpF9u1mDZ6tQeG2NY3sO9aX6pA4dq5rTpnV
LhUdLVX4/IGEaeILZWGMlJ+mgS2vskR9xJ5i3Bo0x2ZuXN5azenuUerDA1772ay4NvtvNRVlLGs2
B9KV5S42dNRTFROvMxsLVn1VcoXC5XSwaVUjPYPeiIJlncu6tjWVZSxtqGR0YjpKMU5FrsmZNnQk
TrW/cWVDTm2wtLGSc31megRLWclEuUrHxHT8PWzvV2p5Q8YZNGPxuJ1csrEl67XNwEzhfrZ3jBB5
tiTZyLb1Zvuo/QJwKXAIM0X7+4DHgLuB5zBflnfM8hyLmheP9fGVnx7A5w/yntco9uxqL7ZIgjCn
tLdU87F37uLQ6UF++sRJ9h3rY9+xPrataeL6SzrYsroxL2lthaLj11r/i1LqRq31l5RSdwDfAx4q
tmCFpsxduBjDQt4a1qK4vtj1hGLOWVNZxtTwRGStoGTMxV28cWUD53rGIq6V5WWuuPV5YomzqszC
DazM7WRZc1USBSvzcj1uZyRzYqrnX1SSkzTFWxaoRCQKXZsOWzMsd8K2pipa6isi7pP2cydSSJc0
VERZH6xYsGj5U8ucioyuUxL3z4s3tOJymgP9bKyklZ7cFO9EdTfFy60BOlqrIwpWpouSZ0vERdBW
fM5Jc8KkSmyRCne4fxUzTfsrlVJnbN9bw98NzGyAWZlGtNb9wOsSnSebcoR4QqEQv9h7lh8+dhyX
0+C2t25j1/qWYoslCEXBMAy2rGpk88oGDp8e5GdPnOSlE/28dKKf1voK9uxq58rtbRlnKxJKkgql
VAcQVEqtAU4Dq4orUmGx1paxhlCWe0xseuLZPPtjY2kKM/6Idwm001xXHpeFLnExhVexaivL4pJD
pXX3ixFrNnE2kHzQnKzUleFMwf3Dk4yFF8Hdtb6Fpw51pT4w9aakJFKyWhsqOBVOgmFtnw4reHbl
KSoDoO3k1lpp9rqXZ2BRmU1Lz2biIpvEStaC0i6HA3dsRr0SYLb9NRmW5Wq2cXL5wJKgmEkuVOFO
LeQL76Sfb9x3mOeP9lJXXcZtb9nG2nZJVy0IhmGweVUjm1c1crJzhEdfOM/Th7r5waPH+PHjx7lo
QwtXbmtj86rGoqyTIcyKT2K6m/8bsA8z0+13iypRgZkZDJh9dfvaJkbGpyMLoa5aWksoFMrYPSkR
SxsrI2vUJEuXPlvik1pE/xCXxjlMQ7UHfyDE6IQZc1Wqt6xdrFzclzI+T5Jy28IuXk6ng7ELw3Hb
U0kTne4/t/NDtJXMcg1c2lTJud4xmpNaeOKTXCxtquRsj9kfq8qTD1nrqzwMjU9lpbDYxV/WVBVx
Pyw0njIn29c0FcxSNFvyeV8ta6riQn94wetIkov4E1yiWgtqTYolomAVMAgrpYKltT5dsDMLeeHw
6UHuvO8wfcOTbFxRzwfetDWr1JyCsFhY3VbL6rZabrlmHb95qZPHX7zA3sM97D3cQ0ONhyu2LeWK
bW0RNyahtNFa32N9Vko1AjVa68EiijRnWOOTCo8rKk4imwyBycvOn3tb5ueM/p7M62f98nochjFj
iSlR7G1YTHfkZKnFM07Zn0EMFiRfK2xDRz3dgxORGJv25iqWNlYmzahoF8tqt8pw/26o9qSUe11H
HZPTgZy9EuZ6fdDK8tzkvES15lmSePJ5z7fUV8woWGESXcZ8LGOQFTMaVsGYfQSbUBQmpvz88FfH
efT58xgGvP4VK3nzVatz9kcVhMVCdYWb1+xewQ2XLudE5whP7O9k7+Fu7n3yNPc+eZoNHXVcsb2N
Sze25hyALBQOpVQt8Ada68+Gv38A+BPgmFLqT7XW3UUVsIDM4QQvYMbM1Fd7WNNWS3VF/ibu4ixY
MduTuSiVqMEqIVZ8Uj7crfwx63+tb6/PKHYlNwtJ5vJa1zFZv2ysLY+KFTIMI86dNVF51r5gxuhs
XNGQdsFcl9NBdUV29Z1P/cmikIqIy+HAHwzmdRxp7//Wp1LwFrEmDwr5SJXRwzwjGArx2wNd/PCx
4wyPT9PWVMkfvH4za5ZJhjRByAbDMFi7rI61y+p4x3Xref5oL0/s7+Tw6UGOnhvmuw++zKUbW7ly
exvrO+pKwm9cAMz1E08BKKU2AP8PuAVYC3weeEfRJCswkRisAnfF6go3YxO+iAWkNc9W3XjLSExM
VrKYo7gU8qV/TzpTKBSZUltZRnW5OxJP5XAYGQ1Sq8pd1FV50iondnJyEczTKDXZ9YykI88386D/
zCVqRT0j49N59YKKWgA9hYvgXDMzORAqmKYtCtY8IRgK8eKxPu598hQnO0cpczl44xWreP0rVpZk
kKQgzCc8biev2LKUV2xZSt/QBL850MVvXurkifBfa0MFV25r45VblybN3iTMGWu01u8Mf34bcLfW
+iHgIaXUO1McN++xLAWFViw2rmhgaGyqcH09LgYr+nuhguznEiOcwzwf1gCHw2DrmqaIa2QqK5Ad
l9PBppW5pfSH9P2sutzN5LR/Vms5RZ0vL6UUmLk2I2eAlTRjtopLTWVZJJ4zX5T6vRwqYJ52UbBK
HJ8/yG8PdvGLvWfo7DdXQd+9qZXf2bMu6wUTBUFIT3N9BW+6cjVvuGIV+vQgT7zUyXO6lx8/foKf
/PoEW1Y1cuX2Nnatb5bJjeIwZvu8h+ilPVKvADvfsRSsAp/G5XTQXFdRsPIdhkFdlYfh8fjU4xC9
CG0qSnnoZgXsF2KAmU3GumyJsmCl2XdVWw01VW5a8tRX5toiWcr9Jxsqy12sb68vyay4pWplngu5
RMEqUbyTPh7bd4EHnz3L8Ng0TofBFduWcuPuFbS35LYivCAImeMwDDatamTTqkZufbWfvUe6+c3+
Tg6cHODAyQGqyl1ctnkJe3a10yH35FziUkq1AjXAK4C3AyilqoG5SQNWJELhZTFLdMySFZtWNkQs
Monqk4mCNeeB8VlgyZ4PF8FYclWwtq1pIpBogSobdvfNTNo/n0mB5rpfW+3oWQATZaU84b6ho54R
73TUhKSBEVlMuhhEuQgWSNUWBavEGByd4sFnzvLYvvNMTgcoL3Ny4+4VXH9Jh7gmCUKRqCx3sWdn
O3t2tnOhb5wnXurktwe6eOT58zzy/Hk2rqjn2os62LWhWRLNFJ5/wVysvhL4e631oFKqAngC+HpR
JSswAyNT1NSUs3Dm3k0SjeOdDgN/GntkIRdczheFUAJzfcZUZZK5zta1+kcm5zS73lwrWBUeF5tX
NVIhyYwKSmyyE4BLN7UW9Sk2B0kERcEqFc73jvHA3jM8dbCbQDBEXVUZN71yFXt2Lss5nacgCPln
WXMVt1yzjptftYYXj/Xz8HPnOHx6kCNnhmio8XDNrnau3rkskppYyC9a6/uVUm1AhdZ6JPzbhFLq
r7TWvyyyeAXF6TBwOR0FsYoUk0QJG1wuB1P+QML9PS4nU/5AVIr6UqOq3M34pC8SH5MPLlrfktaq
NFvsVyIfaf+zO/fc92t5TheHYie6qKpwU1/lobG2nMkkrsqzpXSfTouAUCjEy+eGuf+p07x4vB+A
tqZKXrN7Ba/YsrSgftaCIMwOp8PBRRtauGhDCxf6xnn4+XM8+VIXP378BD/7zUl2b1rCdRd3sLpN
MnzmG621D/DF/LaglSuAneubaW6uZmjQW2xR8sKudS2MT/oSLoxcX+1hPJw1b3lLddT7cOuaJvyB
YEm7CG5a2cDw2DR11fkbwJfNYgHpTLHHpsy5grWw5g2EEsbldLBxZQM1lWWiYC0kgsEQL7zcywNP
n+H4hRHAXCTvtZetYMe65qJr9oIgZMey5irefYPi5qvX8uSBTh5+/jxPHujiyQNdrFlWy3UXd3CJ
apVJkxJAKfUF4N1AD/A+rfWTtm2vAb4MNABf0lrfrpT6JvDemGJWY3qX3AVsAR4B3qG1niik7C6n
Y0ElVvGUOZNmoLMnh4iNO3a7HCV/L7mcjpKOi8mEOU86YRhsXNGQUOEWhPmGKFhziM8f4DcHuvjF
02foHjTfw7vWN3PjZStY31FfZOkEQZgtleUurr9kOdde3MGhUwM8/Ow59h/v5+sXDnHXwy9z9c52
rtnVntEioUL+UUpdD9wGXA58AFOZ2hneZgD/CdwN3Ac8qJT6UXi/28JF/CnwfuAc8E0gED7+yfB+
n5ujqix4Sj29s1AYCrbmVZ5oqPHg6DJYuXTuYtOE+YkoWHPA+KSPR58/z0PPnWNkfBqX0+Cq7W3c
eNkK2poWdNIrQViUOAyDraub2Lq6iZ6hCR57/jy/3n+Be588xX2/Pc1FqoXrL+6QBYznnj3AWa31
XqXUcuD3lVKNWusBzIWKO4Cfa60fVUqNAddorfcBU0qpeuBjwEe01n6l1B7gDq31caXUXuAaRMHK
G4YoWEIJ4nY52b1pSbHFEOYBomAVkO4BLw8+e5YnXupk2hekwuPidZev5PpLOkp+lkYQhPzQWl/B
Ldeu401XrebpQ9089Ow5nj3Sw7NHeljeWs11F3dw2aYleVusU0jJEmA4/Hkw/H8pMBDeRsz2Ntux
twGjwPeTlLUx3ckbGipx5cHFr6Vl4c+eh5xO+kangfT1XQztkQ2zbY+1K6ap8LgWTLsulHrkC2mP
aArVHqJg5ZlQKMTRs0P8Yu9ZXjzWRwhorPVw/ZXLedXOZSWd9UgQhMLhcTu5escyrtrexsvnhnn4
uXM8p3v55v1H+N5DL7NzfTOXbVrC1jWNJR28vxhRSjkxFazPaq0Tp7bLgME8JKdoaamht3d01uWU
Ov3DE4yMmq70qeq7WNojU/LRHi3hxBwLoV2lf0Qj7RFNXu6XJAqajPbzhHfSz9OHu/nVvvOc6R4D
YHVbLa/ZvZyLVYusjSMIAmAGcm9YXs+G5fUMjk7xq33neepgN08fMv+qyl3sWNfMjnXNbFnVSGW5
PKbzSCdgBbw2h/9fsG0DqA/HYzXZtl2BabH6eYqyLiDkjWKk7BYEQcgX8uaeBcGgaa369f5OntM9
TPuDOAyDi1ULr7l0BWvbayW+QhCEpDTUeHjzVWt405WrOdU1ytOHutl7uDuSgdDpMFjfUceW1Y1s
WF7P6rZasW7NjoeA25VSlwM3Ac9gxleVa61PKKVOAG8EyjEXMn4wfNwVwJjW+lBMWTcopf4LuAy4
fa4qIQiCIJQ2omBliT8Q5MiZQZ7TvbxwtJcRr7lOR2tDBVdtb+OVW9skQ5ggCFlhGAar22pZ3VbL
Ldeu43TXKPuP97P/eB9Hzgxx5MwQYKanXruslrXtdSxvrWblkhpaGipkaYcM0Vo/rpT6DGaWwAvA
7wH3A0PAm4E/BP4DuBX4W631wfChy4CumOJux8w4+Fy4jDsKLf9iQrq0IAjzGSNU4FXBC0Fv7+ic
CR0IBjndNYY+M4g+O8TL54aYmDJd8Gsr3eza0MLlm5ewYXm9WKsEQcg7I+PTHD07hD4zhD47xLne
sajtnjIny1ur6WipZklDBa0NFbTWV9BcXzGv1pNpaalZ8A/QfLy7FksMheUhsqSxMuWk5WJpj0yR
9ohG2iMaaY9o8hSDlfDdVTIWrFSLPxaCUCiEPxBk2h9k2hdkfMLH4NgUg6NTDIxM0js0wYU+L539
40z7g5HjljRUcMW2Ji7e0ML6jnockkpWEIQCUltVxiUbW7lkYytgLvtwpmuU091jnO0Z5UzPGCfO
j3Ds3HDcsVXlLuqrPdTXeKitLKOy3EWlxxX5X+Fx4XI6cDoNXA4Dp9Nhrj9kACEIhSBEyPwfnowL
hoBQiPA/MGBNW60k8BHyisNhsHFlQ7HFEARByImSeCOmWvyxEHznwaM88tw50k0lul0O2horWbOs
FrWigQ3L68X9TxCEolJV7mbTqkY2rWqM/DbtC9A14KV3aIKewQm6ByfoG55gaGyawdEpzveNF1Sm
PTuX8Z4b02YpFwRBEIRFQUkoWKRe/DHvLGuqZH1HHW63kzKXA7fLQWW5y/9R6gAAIABJREFUm4Ya
D401HhpqPDTXldNcVyEWKkEQSp4yt5MVS2pYsSRxutip6QAj3mkmpvx4J/3m//BfIGBa8wPBEIFg
kEDAtE4ZhpnJzTCseBgD63FoGOHfMS0NF6vWOaqpIAiCIJQ+JRGDpZT6OnCZ1nq7Uupa4GFgS0zG
JkEQBEEQBEEQhJJG8v0KgiAIgiAIgiDkiVJRsFIt/igIgiAIgiAIgjAvKBUF6yFguX3xR631UJFl
EgRBEARBEARByIqSULC01o8D1uKPFwEfLK5EgiAIgiAIgiAI2VMSSS4EQRAEQRAEQRAWAiVhwRIE
QRAEQRAEQVgIiIIlCIIgCIIgCIKQJ0ploeGSQin1BeDdQA/wPq31k7ZtrwG+DDQAX9Ja366U+ibw
3phiVgMh4C5gC/AI8A6t9UThaxCRNV/1qAK+BWwCngHerbU+W/gaRGTNSz201qfCx3w7XF7kt7kg
j9ejH/gecD2wH3iL1vp84WsQkTVf9WgE7gAUcAh4r9b6YOFrkFMdyoBvAG8ExoF/0lp/USm1kvl1
jyerxxaKeI8L6Ul1rRcySikn8HXgZmAI+BjwNAnuO6XUe4B/BtzA32utv1IcqQuPbc3QfwDuZBG3
h1LqI8D/AXzAnwFPskjbI9EzHvg5i6w9lFJvxWyHfVrrPcne1YnaINyG3wZeBxwL73s0WxnEghWD
Uup64DbgNcATmAMUa5sB/CfwU+AW4O+UUjuBDwA14b+/xrwg5zA7dgDYCVwe3m8+1uNLwHlgPdAG
/O08rQfhTJWvmyv5bbLmsx7/G1gFbMNU4m+Zp/X4F+A4sA6oxqxXqdbhbcCbMZPw3Al8TilVzfy7
x5PVo2j3uJCeVNd6EfBu4O3AZZgTS98gwX2nlKoFvgp8Cvg4Zt9uLYrEBSasdH4eGAj/tGjbQym1
FfgscCvwH8CHMAfMi7I9SPCMBz7NImqP8PPyc0Qv95TNPfIe4LXAbqAX+GQucoiCFc8e4KzWei9m
VsMdSqnG8La1QAfwc631Q8AYcI3WekprPYZpEfwYphbsD5f1kNb6OLAXuGae1uOPgT/QWl8ABjEH
YPOuHuFB5+eBf51D+S32kL/r8QbgLq31y1rry7TWn52n9ZgARoEuwBvevyTrEJY1AHRjWhAmw9/3
MI/ucZLXo5j3uJCePSS/1gud+4EdWusjwClMj4q3EH/f7QYqMCcVfgqUAVcUQ+A54I+BM8BL4e97
WLztcRNwUmt9v9b6dq31K4FXsXjbI9Ez/hoWV3ucAXYBdqvTHjJvgz2Ylq8jwC/J8b0uLoLxLAGG
w58Hw/+XYs4ULQl/t2+3D0Ruwxwwfj9JWRsLIG8y8laPcCdDKXUz5izinxVM6njyeT3ei/mwuZsc
ZyRmQT7rsQpzgHUAGMEcGB8ujNhx5LMef4U5G+/FdHv8+4JIHE8udfgc8BjQh/nc/EDYvWC+3eMJ
6wEU8x4X0pPqWi9otNbdQLdSqgn4X8A+YCvx9529z1vraC64iYKwYn07phLxtfDPiZ5Di6I9MN+H
U0qpezHr/WkWd3vcQ8wzHvgKi6g9LHc+pZT952z6ROy+tUqpSq21Nxs5xIKVJ8Im+9uAr2qtA8WW
J1eS1UMptQf4b+BxzJu1pImtR9gN6h+BjxRXsuxIcj1CQCWm20w9c68sZk2Senwasz9diqlg/VuR
xMuEm4Grwn+fBD6jlGoprkg5kbQe8+0eFxYPSqka4AGgBfjDIotTbD4BfFdrrYstSIkQAlZgvt9/
DHyBxW08iHvGs7jbo2iIghVPJ+agFaA5/P+CbRtAfdjdrMm27QpMrffnKcqy+4MWmrzVQym1FnNW
5Eng9Vrr6QLKHUu+6nEx0A48BVgvJh0OfJwL8t2vHg4nhPgVpjvYXJHPelwH3Ku1fgl4FLi6UELH
kEsdrgNeCrto/QAznmxXgrJK/R5PWI8i3+NCelJd6wVNuP9+BzM+8Hqt9bMkvu8ifZ6F3UavB25T
Sk1iPjP/DnCyeNujE9NF8CngR5jKxASLtz0SPeMX8/1ikU0bxO47lK31CkTBSsRDwPJwMoSbMDNq
TSmlyrXWJ4ATmNlZXotpRXgwfNwVwJjW+lBMWTcopdZjut38co7qYJ07X/X4HKYr2q0ASqnKuakC
kL96PIOZIW0nM0kuXsfcPVDyeT1+DrxJKbUivP0l5o581uMY8Cql1FLgFUT7S5daHY4Bm5RSa4BX
Y86aHmP+3ePJ6lHMe1xIT9y11loPpTlmofBWzLjTPwIOhL0RHib+vnsa0wX5LeG/SeDXRZG4sFwP
bMd8lz2LGaT/TRZve/wcUEqpyzCfdZOYbuiLtT0SPeOPsIjaQylVo5RahxmvWRH+nM0z4yHMiceN
wI3MjGOyQhSsGLTWj2OaVO/DzMLyQcwgWytu5A8xX3DfAv7WllZ6GWawvp3bgSDwHOYFu6OgwtvI
cz1uApZjavWjmCm154R81UNr7dVaHwnHkx0P/3xca+0rfC3yfj3+HtM/+CDm9fh4IWW3k+d6vB9z
kHACMIAPF1T4MDnW4SuYD+gXMN1M/zysxMy3ezxZPYp2jwvpSXKtFws3hf/fhdk3RzHvtaj7Tms9
jhlv8ueYGUk/qLXun3txC4vW+rjtXebFjLWJew4tovZ4AfgbzCQF78es86JtDxI84zEzcS6m9rgZ
eBlzMmJ3+HM2z4zvYvanpzGVtP+VixBGKBSaXTUEQRAEQRAEQRAEQCxYgiAIgiAIgiAIeUMULEEQ
BEEQBEEQhDwhCpYgCIIgCIIgCEKeEAVLEARBEARBEAQhT4iCJQiCIAiCIAiCkCdEwRIEQRAEQRAE
QcgTomAJgiAIgiAIgiDkCVGwBEEQBEEQBEEQ8oQoWIIgCIIgCIIgCHlCFCxBEARBEARBEIQ8IQqW
IAiCIAiCIAhCnhAFSxAEQRAEQRAEIU+4ii2AIAiJUUpdCfw3cC3wS2BMa72zuFIJgiAIQnLk3SUI
YsEShPnAFUCnvKAEQRCEeYS8u4RFixEKhYotgyAIYZRSfwd8AOgDfgb8NTAA1ALHtNY7iiieIAiC
IMQh7y5BiEYsWIJQIiilNgN/AVwS/tsOdAIfB34rLyhBEASh1JB3lyDEIwqWIJQOVwO/0lp3a60D
mD7sgiAIglDKyLtLEGIQBUsQSodGYNj2fbBYggiCIAhChsi7SxBiEAVLEEqHQaDO9r2lWIIIgiAI
QobIu0sQYpA07YJQOvwW+IRSqgUzOPhdRZZHEARBENIh7y5BiEEsWIJQImit9wFfBZ4HngOeKK5E
giAIgpAaeXcJQjySpl0QBEEQBEEQBCFPiAVLEARBEARBEAQhT4iCJQiCIAiCIAiCkCdEwRIEQRAE
QRAEQcgTomAJgiAIQhqUUm9VSg0ppR6L+f3bSqmQUmpVcSQTBEEQSo15maa9t3dUMnMIgiAsIFpa
aoxiy5AMpdT1wOeACzG/Xw68LtNy8vHuamioZHDQO9tiFgzSHtFIe0Qj7RGNtEc0+WiPZO8usWAJ
giAIQmrOALuAo9YPSikD+Dzwr3MpiMvlnMvTlTzSHtFIe0Qj7RGNtEc0hWyPeWnBEgRBEIS5Qmt9
FEApZf/5vcAkcDfwyUzKaWiozMsLvaWlZtZlLCSkPaKR9ohG2iMaaY9oCtUeomAJJY/PHyQYCuF2
OXAYJetFJAjCIkEpVQ38I3BTNsflwzWnpaWG3t7RWZezUJD2iEbaIxppj2jStceUL7Coxlr56B/J
FDRRsISSYGLKz4nOEU5eGKGz30v3oJf+4Um8U358/mBkP7fLQZnLQVWFm8YaD0215bQ0VLCkoZK2
pkqWNVfhcornqyAIBeVioB14CrBGIloptUFrfbp4YgmCIOSGzx/ghZd7qS53s3VNU7HFmfeIgiUU
hWAwxPELw7x0op+Xjg9wpnsUe/S302HQWOuhsbaKSo8Lw2Hg8wWZ9geZ9gcY9fo4cmYorlyX06Cj
pZpVS2tY1VbLyiU1dLRW4XSI0iUIQm4opWqAJUAVUAEMApuBEKai9RBmsosLycoQBEEoZaZ85mT2
2KSvyJIsDETBEuaMUCjE2Z4xfnuwi6cPdTM0Ng2YStH65fWsba9l7bI6OlqqaKorT6sU+fxBBkYn
6RmcoGvAy4W+cU51jXK2Z4xTXaOwzxzrlJc5Wd9Rj1pRj1pez+q2WhyOxWH+FgQhL9wM3Gn7/iJw
jdb6MaXUZPi341prGZkIgiAIomAJhWd80sdv9nfy6/2dnO8bB6Cq3MXVO9rYsa6ZTSsbKC/Lviu6
XQ6WNFSypKGSbTZztj8Q5HzvOCe7RjjVOYI+G7aUnegHoKbSzc51zVyysZUtqxpF2RIEISVa628C
30yy7RQzboKCIAiCIAqWUDhOd43yyPPnePpQN9P+IC6ng4tVC6/YspRta5pwuwrjtudyOli5tIaV
S2tgZzsAQ2NTHD07xKFTg+w71sevwwpfU205e3Yt4+ody6ipLCuIPIIgCIIgCMLiQRQsIa8EQyH2
H+/ngafPcPSsGSPVUl/ONbs6uHJ7G9UV7qLIVV/tYfemJezetCQS//XkgS6eOtjNj351gnt/e5rX
7l7BDbuX52RNEwRBEARBmK+EQrNeB12wISNJIS/4/EGeOtjFA3vP0NlvpiLeurqR6y/pYOuappJK
+elwGKzvqGd9Rz2/s2cdT7zUyX2/PcU9T5zkkRfO8/Zr1nH5liUYJSSzIAiCIAiCMD8QBUuYFVO+
AI8+f55fPHOG4bFpnA6DV25dyo27V9DRWl1s8dJSWe7ihkuXc9X2Nn6x9wwP7D3D1+89xHNHe3n3
axR1VeI2KAiCIAiCIGSOKFhCTvj8QR5/8QL3PnmK4fFpysuc3Lh7Bddf0kFjbXmxxcuaCo+LN1+1
hldua+Mb/3OY54/2cvTsEB9881Y2rmwotniCIAhpOdc7RigEy+fB5JYgCKWFOAjmF1GwhKwIBIM8
+VIXP/vNKfpHJvG4ndz0ypW8ZvcKqsqLE1+VT1rrK/ir393FQ8+e4+5Hj/Hpu/Zx6w0b2BNOliEI
glCqnOsdA0TBEgQhB0TDyiuiYAkZs/94H99/+BhdA15cTgc3XLqc112+ktoF5kbnMAxuuHQ5K5dU
86WfHODbD2i6+r28/dp1EpclCIIgCMKCQ5Jc5BdRsIS09Ax6+d5DL/Pi8X4chsGrdi7jDa9cNS9d
AbNBrWjg9vdewud/uJ9fPnMWXyDIu169QZQsQRCERUgoFJLnv7BgEfUqv4iCJSQlGAzxy2fO8pNf
n8DnD7JxRT2/e/2GeZG8Il+0hF0GP/W9fTz6/HkIwa03bCiprIiCIAhCYTl8agDvlJ+LVWuxRRGE
giAGrPwyJwqWUuoLwLuBHuB9Wusnbdv+BLgdqAT+J7x9ei7kEpJzvm+cO+87zIkLI9RUunnf6zZy
2abFmbq8trKMj71zJ5/6/j4efeE8TqfBO69bvyjbQhAWAkqprcA6rfU9Sql6rfVQsWUSSpthrwxL
hIWNuAjmF0ehT6CUuh64DXgN8ATwZdu21cAXgL8G3gL8LvC2QsskJCcYCnHfU6f5hzv3cuLCCJdt
XsL/ff9lXL556aJWKGoqy/jYO3fR3lzFQ8+e44G9Z4otkiAIOaCU+nPgG8A/hH+6XSn1d0UUSRAE
oeiIfpVfCq5gAXuAs1rrvcB9wA6lVCOA1vqk1tqttf420Bvev38OZBISMOqd5nN3v8gPHztOVYWb
D711Gx944xZqKxdWEotcqa5w8+e37KChxsPdjx7nyQOdxRZJEITseSdwOTAQ/v4x4KbiibN4GfFO
c7ZnrNhizBu6Bryc6R7N6hjvpA+fP1AgiYRYJqf9DI/PT2tnSKKw8spcKFhLgOHw58Hw/6X2HZRS
/w7sAz6ptf7FHMgkxHDs3DB/f+czHDgxwNY1jXzi93eza0NLscUqORpry/mLW3ZQ6XFx531HOHJ6
MP1BgiCUEqNa66D1Jfw5mGJ/oUAcOjXA+b4xvJP+YosyLzjVNcKF/vGM95+Y8rP/RD8HT8p7aq7Y
d6yPw6cHCAbnobIyD0UuZeZCwcqE/405q/iXSqnrii3MYiIUCvHLvWf41+8+z9DYFDe/ag1/9js7
qBGrVVLaW6r50M3bAPjyPQfoGZooskSCIGTBcaXU/wEalFJvVUrdBRwqtlCLGxnZFQJfwJw3mPSJ
AjvXzEdrkMwy5Ze5ULA6gfrw5+bw/wsASqlVSqk/A8a01ncDfcC1cyCTAPgDQb55/xG+/8gxqivc
fOwdu3j9K1ZJhrwMUCsaeNcNGxib8PHvP9rPxJS8wARhnvCnwDhwHngX8HT4N6FoyDunIMy/Mf6C
oVDxTKFQqGAun5LkIr/MRRbBhzCDiC/H9HN/BphSSpUD1cBngCGl1AGgCTg6BzItesYmfHzpxy+h
zw6xckkNH37bdhpqPMUWa17xqp3tnOsZ5+Hnz/Gf9x7iT9+6TZRTQSh9Apjvnc8UWxDBJJvHpj8Q
ZNTrY9Q7zYolNYUTqoQJhkIZvWtkuLzwOH5+hL6RCXasbabCk+chvHSYvFJwC5bW+nHMF9l9wEXA
B4H7ge9rrQ8Afwn8M/Ag8C3gO4WWabHT2T/OP377WfTZIS7e0MJf33qRKFc58vbr1rFpZQMvvNzH
Pb8+WWxxBEFIjx/w2f6mmUmyJJQwwWCIZ3UP+uwgF/rH8fnnv1PTsfPD9Ax60+5nty5kEt/TM+jl
8OmBtPstdgLB+dWH+kbMkITxSV/eyx715r/MxUzW6q9SytBaZ6Xnaq0/CnzU9tMe2zaZSZxDTnaO
8Jm79jE+6ef1r1jJW65eI1aXWeByOviTN2/lH7/1LPc+eYrlrdVculEWohSEUkVrHZlYVEqVAdcB
O4onkZAp/kD0YHi+uzT5A0H6hifoG56gtaEy5b4Bm1KVSbVPdI7MVrwFj88f4LmjvTTVlrO+oz79
AVlQ6K5ZiHGbV0Id8kouFqzTSql/VEqtybs0QkHRZwb5t++9gHfKz/teu5GbX7VWlKs8UF3h5kM3
b8NT5uSO/znEOUk7LAjzAq31tNb6fuDV6fYNJ8QYUko9Fv6+RSn1rFJqXCn1mFJqeaHlTcV8VzZi
6Rue4KlDXSWX8rpY7RyMUrAW1rUuFt4pM5apf2SyAKUX9hoVYl1Sh2H9l3FhPsjFgXM35mLA31BK
+YA7gR9qrUvrKShEsf94P1/6yUsEgyH+5E1buUSsLHmlvaWa979+E1/6yQH+/cf7uf29l1Jd4S62
WIIgxKCU+v2Yn5YD7WmOuR74HOEETWG+hJko443Ao8DfAn+cP0mzYz4PuRPpC8fOm6u7HD49wOWb
zZVdgotYscjWgiUUl0Jfo0LoQJbI0r/yQ9YWLK11l9b6i1rrPcCfhP86w1at8nwLKMyeZ4/08O8/
2g/Ah27eLspVgbhYtXLTK1fROzTJ1352cH6ugyEIC5+rbH9XAg3ALWmOOQPsIjoJ0x8Df6C1voC5
xmNb/kXNgjw+bvyBIIOjU3NoKYk+z9hE4liQWHGK8YTN5zmzad5p30zmuPmiaB6/MFzaC0nnuR3n
0rJYCAuWxXxMMQ9mfoFSyuicUwoSpdTVwO9hvqB+BPwR8HrgbuAN+RJOmD0vHO3lqz89SJnbwUfe
th21oqHYIi1o3nzVas50j7L/eD8/+tVxfueadcUWSRAEG1rr9+VwzFEApZT9tyPh324GLgP+LF05
DQ2VuFzObE8fR0tLfPa8QCBIbc1I0u3ZsP9YL4MjU9Q3VNKSJjZoNtTWmFaqpuaaKIv/kRfOU1tT
Eflu1Wd8wkdtz8xCu83N1VHbC4kla01tBed7x1jVVot7ltfS5w9Q2zkKpK/D6HQw0iZNTdVUpfCQ
aGmpichr/22uOXR2mKlAIONz+/wBTnWOsGJpLR737O8Ti2Tnd3rc1A5OptwnG/y2e7CpuZrysvwn
6raua3NTNfU5JidLVtfaPi9OtyvlPqXK4Mgkg14/wxMBrtqV0iEhjkLVNZckF8eAU8B/AB/QWltT
TYeVUm/Oo2zCLDl4coCv/PQALpfBX9yyk3UddcUWacHjMAz+6A2b+b/fepb7nz7DyqU17N60pNhi
CcKiRyl1lhQGCK31ihzK3AP8N/A48JV0+w9mkC0uHS0tNfT2jsb97g8EGRk1M4z19IzMaob79Pkh
ADq7RjAKtOYOEJG3r2+UifIZhWFoJLqdrPqOT/oixwD09Y7R0V6fsD3ySSgUipx37/4LjE5MMzjo
ZXVb7azK9flnrlm6Ohw/PRBZMLi3bxRveWIFy+of9nbKpPxCkGndLE5cGKFnyEtX9ygbV+ZnMjjZ
/QIwNDaVtYzeST+9QxOsWFIdd4/5/IGZPt07hqcsf0qiRaT8/jF8k9lH5qRqj+HhCbxT5pB+ts+Q
uaZ/eDLrawmp2yObMhKRi3p9I2BorV8GUErt0lq/EN52VW7iCfnm6NmhsFugwYdv3i7K1RxSWe7m
tpu384/ffpZv/M9hljZWLtr1WgShhLgyxbasR3NKqbXAPcCTwJsWYhyy0zk3A6xMPaviXQTnxpXJ
fpbpsMKZnxTxucmfrr0mp4vvJpWLi7yVJXK6gEq9nVw8+vaf6AOgqsJFc11F1DZ7xveC982CuCPO
T9fAUiWXLIK/B3zc9v3jSql/Acg2fbtQGE52jvC5u18kEAzxwbdsZfOqxmKLtOhob67iD2/azLQ/
yBd//FLSmAJBEOYGrfVp6w+oAlaG/zYA30t1rFKqRim1LnxcRfjzV4ER4NbwPoXzpcsA+3grXy9i
p6O0ZrBjY48KMcacnDYtFNHnyb5xff4AXQNefHlSFqLWwUpT8cnpuVFQUpFLnJiVva4Uw5eDoRDn
emfiyRJl2pvLRCQFUa8K8AxZzOSiYF2jtY5kYdJa34JYrkqGnqEJPvuDF5nyBfjDN2xm57rmYou0
aLloQwtvvGIVfcOTfPWnB+bdgoaCsBBRSn0eM3b4p8CngbuA/0pz2M3Ay8D1mJl0rc/LgU5gFDhU
IJEzJP+jI6cjlyFC9mScHGAORn37jvVx/MJwVLB8LoPlc73jnOoa4XR38iQP2ZRrV1jsx41P+njh
aG/UJF6yckOh0JxZt3JK8mTpLLZDp30B9h3rY3B0KuWhk9N+eoYmslLssklK0Ts0Ea1gJZh8mMvk
IwU/VR7Ln5jyL4hFwbMlFxfBMqVUmeUOoZSqzrEcIc94J318/u4XGZvw8e4bNkjsTwnwxitXc6Z7
jH3H+vjhY8d5+7Xriy2SICx2dmutNymlHtVaX6OUuhh4S6oDtNbfBL45F8LlyjxJLJeQdKIHgkGe
OdJDpSc67qiQdfb5g1QkyCFgnTJdeIo1oBzzJvdeyEb8KOuC7cuZ7jGm/AFOd42yZXVj3HY7Z7rH
6BwYZ+OKBuqrc0uQkCmBHBQsq03tikrP4AST03702cFIuv5EHD07jHfKh9MwaKrLf0LrWAUhURPP
l+yOyQhFfQ4xo/HOosxQiBeP92FgcNnmxTUmzWV66quYCS3uUkr9EDgY/k0oIv5AkK/cc4DOfi+v
vmQ511zUUWyRBEw3gvfftJmljZX8Yu9ZHn/xQvqDBEEoJNZUuEcpZWitnwOuKKZAmXKycwR9eiDh
tvjBUW4MFGTR1XjsacfTYVkvrAD8GQo3oA0kWdg30zF0IBxPlIuikQj74H1wdIruAW+0QEbife10
h5OsDI/lN1yws3+cEW90mbmkLLfc7nLRU6y+UTBPkdj4vwRCTttcMwvuIljgE+SreKucQseklWI+
jlzWwboDuAb4AfBd4Eqt9Z35FkzInFAoxHcfPMrBU4PsWNvE26+V1OClRGW5iw+/bTvVFW6+/YBm
//G+YoskCIsZrZT6IGbmvweVUl8C6ossU0Z0D3rp6vcmdreJsnDkfo65iheNGpCnkddadDiWQg7Z
LAUJcmtPX8A8KOXAL0cXwe5BLye7RpIXm6TciAKTx5bz+QOc7h7l0KloxT8nD8FwW81GecjVKpht
ubFKbGf/OMcu2PtpfOE+f4AXM3B3LBrz2wBXcmStYIUXE94F1GK+lF6tlPr91EcJheTBZ8/x2L4L
LG+t5o/euCWhb7BQXJY2VvLht23H6TT48j0HONmZ/OUoCELh0Fp/APg+8DfAncAx5sn6jVbWskQW
ikLMEFsD3cHRKTr7x9PsnR1RFqKYbUaGrkmFnMT3J5Uvs5NaCloqGTO9ZqnimRJtSaeg5LPdkpWV
SwyWdd2THTnqTW95SyTP2IQP72R87Nls7plAIPrYnsGYxCgJjukZmmQi7O44WwrR9wvxDCm022Qw
FCqpxYXt5OIi+AvgI8DVmMktriJ1+luhgBw+Pchdj7xMXVUZH3nbdio8Eg5Xqqxrr+OP37gFnz/I
5+9+kZ6YTFWCIBQepdRTwDuAeq31d7TWn9Vanyu2XJkQybKWYPCab5ceO/rsIKe787uOUtQAdY5i
V8YmzIQQ3RmsR+a3WbCGcrA4zAwsUyhHGVY72SA1mSKV6OeJKX/e1zXy+YN09iduy3QD62AoxODo
VFQ7J7Jg2Us5di6xJdNOojY5cLI/kl49V2LLPdk1wlQJZGvMK3N/S86aY+eGefF4X0lmas5lNO7W
Wr8q75IIWTMwYmancxgGf/qWbTTW5j+wU8gvuza0cOurN/DfvzzKZ+/ax1+/62LqqsqKLZYgLCY+
CrwdeEEptQ8zg+DP5sM6Vg4HEJhbC0V0uaG8DdJTxSaFCOEwjLSD9GxdyQZHp5jyBzjTPcaShvis
+slirXw5uAtGYk/ycC2SKlK2z/arkqjdjpwetCkws5cJzJjAgdHEMXvJzuEPBJn2BRgen+Z09yiN
NeVsWG566KaLwXK70tsEMjWcDY1NRbme9g1NUFnuprI882HxpC+QdDHhwqdpn0dpBJMwNDZFTaV7
VtlKrf6XyEJpcb53jOoKN3UFTuwSSy61OqiUasq7JEJWWEktRr3YUk/oAAAgAElEQVQ+3n7tOllI
eB5x7UUdvP4VK+kenOBT33shLjhYEITCobX+jdb6w8Aq4LPAjcD5ogqVIZYLVaJBZN4sWCRWMsxt
+SOYxAXPUiaqK9xpXQWzlccqO5n7WiI5cjpRbockxRI3du2lbBTMKX/AlgU9P9KlSvkerazOfD50
aoD9J/ojVsHhcdv7z1IASXxsMmUm2XlTcfTsUNT3YxeGU1q5klkFI9szOmseSXLC4xeGeeFobz6L
nBXJLsfw+DRHzgxy5PRQ4h3yhM8f5GzvGIfPzN4tM1tyUbA6gGNKqSeVUo9bf/kWTEjNXQ8f4/iF
ES7fvITrLpaMgfONt169husv6eB83zif+t6+kjRvC8JCRSlVD7wX+BhmBsGvFVeizLAW/k2sIIQS
fu7sH+d4kiQRiYjWK2Kij9K5fQVDjE9m9izzBxNbhayPBlBfnca6n+OIMJkRLln9cokjiShzKY7N
2EUwfL1jZ/qzjn/KswUrVRpvuwx7D/fQN2y6xHvDSokV42Zv80TWUfuizy5n+iHrXLq2nUqZaKSw
glilB4OhqNi03qEJpsKLXOszgznLkT/xk9xT4es/OpGfCebkhvXi+Trm4iL4L3mXQsiK3x7s4uHn
z9HeUsV7b9yYd79qofAYhsE7r1tPMBjikefP88nvvsBH37FT3AUFocAopX4BbAF+AvyT1vrJIouU
MYnWCbKItr7MfLZip9a2z97LId2g6+jZIYbGp9i6uonqCnfKfZMqAeGfDcNI+24LAcfODjE5MZXQ
5S9boteaSvI5h7Jmi1WW02kQm90+naptx4i44OVHuFSXx57nMkSIgZGpSJKWZCTKz5VK1GAohM8f
xON22vYvzIA6mdXPHwgmVPwS7Z2qN/v8QQLBIOVlmQ3LB0Ymaaz1cKprlN6hCTZ01EeFiVjKnz8Q
wu3KPmnMbFrR3ibJLkc2yzTYGR6bon9kitVtNVHPh+SLayf+3TvpZ2hsipaWmpzkyIRc0rT/CqgG
toU/n8NMd5sUpdQXlFKDSimtlHplzLa3KaVOK6WGlVLfUkpJloYUdA14+fYDmgqPkz99y7aMTOZC
aWIYBr/76g3/v703j5PjKg+1n6reZ+nZF41Gu6wjb7KNjDE4BoENXDCExZAQAiTAzQch8MvCzXYT
vpuNJDe5IYSPQBYIDnwQSAJhdwI2GIONsRG2ZFvykbWvo9nXnqWXun9UV3et3dU9M2qN5jw/y9Nd
XXXqrVNV3e9b78aLn7ORsyOz/Plnf8LY1KXpQaNQrGP+BtgipXzfWjKugFKF2GpFLnJ57+e5fIFz
o3NkqniYHAqJO0SwitY1OWf1q6pe1asQ1GequNNQzw0Ng3Mjs6GrslaTP4xuHqTAzy/myOZsfZCw
PDQVR6u+Q9tY3hDB8mstYLkda52xVep1FnROIVj2IEO2tMxnGwt5epLHnx1xRIBc6uIMCytU6GL/
kWGeOFq5EId9TidmFzk7PMfEtHnPBaca1DIhy5+8C2Nz/FgOl0rRB41obzNQi1F8+PQEw5MZT+VA
vxFy+YLDA2rnyeNjnB6eqauATVjqKdP+v4F3Am8vLnoz8JEK698JvBd4OfAD4GO2z5qBe4rLXgS8
BXhDrTKtF3L5An//1adZzOZ528t309+5/Cd2isaiaxpveekuXnHrZi6OZ/izz+5f8XLICoWijJTy
m1LKNVn+q1RFsIpCcvD4qKd31NjUAmeGZzgSohKbheHZVzhFqJJttJTNc/TcFIsBT7CX05uoGtax
uJX9aiOGCRE8cGyU/cXcl4KPwRh+b07Gpxd48vgYUA4RLW1fY3VBu6cniFy+wKmhmcDzY8c9i/Ze
WG4RNM0tV9EAtedbueQwxzGIFkMj3XM5VTTo7d6Q1Sr+EHQJlPqluT+vU4yKIaWu9/bKkIWC/3mv
t891JaPn+PlpTgdUFR0qNsAuNSy3DWMd2+Ss06jxeyBUDY9320feUxdnODMy67u9dZ349hRcIerJ
wXqRlPL1wDSAlPKPgedUWH8fcEZK+SjwTeAGIURn8bMccCumgXYU81RsqEOmdcF/PHicU0Mz3HZ9
P8+7pq/R4ihWCE3TeOO+ndz9ou2MTy/yp5/Z70nAVSgUCs3yYPk96XcpGFbOi4WlsFYqTABehdfp
lQgpZwUL68SFaUan5qt6ucwQwcr7qdVbUb0qoe11DRqyRxn1eP6CDKHqY9v7K7lD6II2Dw6XKnoH
K5jAQ2MZLozP8eyZSQoFg2Pnp4K9nq5hZhfsniSnEJqmOSpHVlP87WX8Lc9tOA9j9XUqUesDziqR
rjVTS/8wXdcceZl+lTlrGS/s3A1PZjgfcp7s95ElyzOughOrZeTMZqrng65mrlw9BpZ1txsAQogI
lXO5+gDrkZk1q/0AUspFKeVTUsp54E+L8jxQh0xXPIdOjnPvj07T25HizXfuarQ4ilXgrudv5e2v
3M3CUp7/8/nHeeTpoUaLpFAoLiMiVg6NX4hglW1rLS9uUZeBVUGB9/OMBIWJVa0iWKNyZFTR44LC
0WoxzPzWXykVTvezsHwGD5I3jBprlaRfzOa5OJFhZHKew6f8K7BVOj9+ev25kbJSbr+GSwq2Te58
odyouWRoh5jI5Ta2PTMc4PGwDRuz5VwFXoN1ylHRIHJ9pOtaOWzYMFa0P16Y7abnamv8HFiUZQWM
HL8Rwoy7mo2Q6zGwHhZCfAoYEEL8BvA9lmkUCSF+B3gf8BdSyseXM9aVyExmiU98/RARXeNdP32t
aiZ8BXP7ngF+7WduIBbV+YevHeLrD59c9WpECsV6QghxgxDix0KIZ4rvPyCEeF6j5QqDpUzlQipS
9u+O0IqEy8pwBnWFDBGsYBfFot4wNfdeSmOskger1iqC1ZREj0G1QuFi7k3dBpZjv8WDms0sMTXr
r/hax1fpPNp7ZVleJHsfsLC459LA4MJ42cCyX8LnR+eK65RZKhpdBuXea0FyG0bZ2Ls0P5fViyv4
5WaFySus1B/OfZ2Zoa7+IZZB2yyH4+enS+cK4NCp8QprezECjMBatg/+LNwyN5Xme7nUU+Ti94Bv
APdjlmz/kJTytytscgFoL77uLv49b30ohHgD8GeYxtXv1CrPlY5hGNxz7zNMzi7xuhduZ9uGdKNF
Uqwy127t5HffspeudIIvPXicf/z6oVDx8AqFIhQfBd6B+dsE8AXgQ40TJzwVy7T7aBPOkKzaFQmj
9L/AXQBm+GG1ctsVB3F4i4pjVLOuqMODVaMnqvyB/WX1MCz3foLzzWqT3+PB8mH/M8MsZP3DL8Ps
rmSoECJnzbW4OVmuHOmJmjSgO52yvbcbBl7B7GFkus3o82N0at5WVCT4XISZb79jnc4sMTyZKb23
rxI05omh6ZIXrhZquSY0zXa/OG0tz3gTM4scOTNZMRyv2p6HJzOcHvbPvSrJ5Loo3JUJl3LeeyHs
d1OlBx1+89boh9P1FLnYDvwE+CvMH6onisuCuA/YJIS4FXgV8BiwKIRICiGagL8Fvgr8sRCiRQhx
aVstX+Y8/NQQjz87yu7N7fy3521utDiKS8RgTwu/97ab2T6Q5pGnL/LBT+/n4kSm+oYKhaIaWSnl
QeuNlPIIZj7wZU8kYiovfoqb79Nrm+If9kmtW9l1FGzwGWJ6bokfy2F+dPhi5XENA3l6gqlqjdWt
fWjVn/jXqr6Wp8B/4CAFrpoCWC0k8MCxUc76hJ7Vqv4lXUUqatUfwxgbZQ+WURo/yGB2L7Wv5jY6
5+azjiqL9jkr9fcKUJotoydI5glb0QTDMIteHD41EarSnBt3IRFwFu8AiEbK61jHEcbwDkMtHhXD
oHRQY9MLvj2lrOFOX5xhfGaBsxUMJKPKve7GbUwtZfM+xr3zmhud9KlgaZjfIxNVKvpVug99W1dU
OAarHP5qFourJ0Twfkyj6T7g+4AEvhi0spTyQcyng9/ELIbxHuBe4PPAc4Fe4KeBmeK/NdHw8VIw
NrXA5+47QjIe4R2vvLpC5SPFlUh7S4LffvNzePFNZhn3P7rnx1XLuCoUiqrkhBDbKOcRv4KqwWiX
B9ZvgJ8SVi1Eplr+ke84njG9O3FXBDPH8K63sJR3KMJ23D2TIFw4Va1PqC0lLJsPigio7FUJHNc1
t35yDQeUi64JTaOztdzr6ODx0ZJSHeYCtssZdHSO3kLWuQgrXwVP3/xSzmFc26eoVMQiYLhaen0a
hsHJoRmm5hY5fn7aZTSH8GCF8BLutPWUW66TZGJmkVNDZaOnklHmraXiLGzhrhxqbmN+XnsUTGWv
LHjvUb+G5o6vEwMW/HIwMcMN5Rn/XD9/GVwPgny+39zXzfDkfGl+CwWDZDxKJETz6nqpOZlHSrnN
/l4IcS1m2fZK27wfeL9t0T7b6zXxw3apKRgGn7r3MPOLeX7xFbvpbq/coE9xZRKL6rz15YLtA2k+
/V+Sj/z7QV5x62Zed/v2UF3tFQqFh/8BfAUQQogp4CTwCw2VKCTWk/O8T1lj/xLNdg9WHeFKeEN8
3Kz0g7+S1ySMalAhJMpPKbfP0ejUvKfxrRHwxle5xGuIgKm4+SndvqFZFZTz0al5z9zqWtmL6Uf1
EEjXyfQZylpUcHiw/MdzL7ZGX8zmS+W6A2WxHbyf1yiq66UByw22Kw5prlMwKNiMdLeCXw0/WTzr
RHR2DbZz5Oxk+R6r8oAjCLdRUdmD5TZ6qt/XJYOiKMzpoRmaYzpb+is32PUYuxXEujA2Rz5vOIwn
v9UNo3p4s2EYgQZ1pQcEfh4sXQds9tzx81OMTs5zzdZOCgVj1XWoZY8upXwa2LsCsihsfPcn5zh0
coI9O7q4fY+qXL/eue36DfzeW/fS257i3kdO88HP7K/6A6ZQKLxIKQ9KKfdg5hBvklLeIKV8otFy
hcEKpQobeuQMcwu3D6+SXjlsSPNRSH3Xq6S3Bjwdrxoi6LPdT46MBHr67QqaXzhSkDHpN3ej02WP
lP18PPrMxVKBBsfYPipnpVNy9NwUR85623VYPaH8qHaKC47jC1jbkV9UXBRoYfnn28zNVy+Pbadc
hr0sU65Q4HixgbRWjlusOlbBgFxx/nP5AudtfZAyC7kVKfqga1q58EaF4erZU8XxXJ/l84WaK1wC
jmIjYam0n1MXZzg7OutrnDo38y8lb18S1BjYLYNhON/7fSf6XbdWQ+aCYXjaHqw0NXuwhBB/5Fq0
iXIRC8UKcHE8w789cJTmZJRffMXumtzjiiuXzX2t/K+3P5fP3XeEh54c4g8+9ShvvnMXt+/ZoK4R
haIKQojP4KPzCCEAkFK+rcr2rwf+CXhCSrlPCLEFs0DGtcB3gDcVW46sGpYimq/irbLw60FTC4bh
qu/n95TY56vH15iwLYroOl3pJAtLOaYzSzV7GSqtm80XHE+tnevbvSZeQ8Xj4aki1GI2TyIW8Rhg
tRoYbmZt21vNdMFUGCt5sKpp9GFybOyjl72B/ut6qsZb+Ui1XmoBG1i93HSbB2s6s0RLKhboOc0X
jFLj2sxijuO2sLVDp8YZ7GlhsKfFd9uorocyijTNXnijUkif7f4LXcihwniu936GfC3jedf1fw0w
E6KnVDWvccEI+J6yLTp+YZreDjMvan4xRyyqlzxNc65+bPb7xG/cas90VltvqseDlbf9ywEHgFeu
pFDrmULB4JPfOMxStsBbXy5ob1E1PxRlUoko77zrGt79mmuJ6Dr33PsMH/vyU44vGoVC4ct9mDnE
Qf8CEULcCXwYWwVc4IOYv4M3ArcC71p5kb3oulbqIbSUzTM+XUwarxKi5KeATM0tIU9PkFnI+W7j
fu9X/ttX0a0iiwZsH0jTV1Sk/GLzwniwcrby4bX2vPF72p7zCb2E4GIaliFVrYpgIK6Qxem5JXL5
Ak+dGPNdXSM4hM2sKFfFmxFCJEcOVoAHa2puiWyu4FlulLYzX8VChmCVtwuWSUNjZn6JQyfHHf20
3FR7kOCXMwjQU0zDCHPuInrZg3VmZJalbJ5Fn+p41lCz81kePXyRobHqUScVz6HrozAPTSqNNzw5
zyOHhkr5We4HIxcnMgwXi2v55UdV+q7wwyrT7n64ccan8EYuX+DAsVGePG7eC9lc3pNjZg+VrtUz
aZb/r2mTmqmnodIf+y0UQugAUsrVacm8TvjPR09z9NwUt1zdyy1X9zVaHMVlyi1X97F9IM0nvnaI
/XKEo+emeNvLBDft6mm0aArFZYmU8p+t10KI64BrMFWWg1JKWWXz08BNwCcpR2zsAz4ppTwmhHgU
eDGmEbaq6LpWUiaePjHOYi7P9du7fJVn+xNfv9CcExemWVjKkYxHSzkZldSUs6OzDPQ0O4wqvxDB
AqaC5MxxCPkE3xoXrWqhCbtBZJiPpCuubw8R9CtmYHlMTDkCvFk2rDn19nzyJ5vLMzy5wIbOJtNQ
tn3mV6DAjaaBvoy09VAeLHslwFIVv/KyzEKOw6fGScQi3sIJhnu7kLKGuDQ0rSzzUoWCDQV7aT0f
kjF/tdcM+wvnfdOK61qcrWDwAUwWw1H9jDA303NZ2lvyxIsVI6dmFxkaz7C5r9VzeYcxKgwjOD/z
+HnzmhudWmDG1TQ4s5jjRDFEs6st6dkevAaZb6l01+v5xRwRXXM4mTOuao/27y3rGnN70ML01Aq6
/KwHM6vtwarHwFoAvJ0CzYcrRsBnihCcHZnly98/TltznLe8TDRaHMVlTndbit9683P45iOn+OpD
J/j/vvQkt1zdy5tfuot0U7zR4ikUlyVCiL8EXovZMkQH/lwI8Tkp5QeCtimWci+FExbpAyyteALY
XW3fHR1NRH0a7dbC0aFZWltT9PS0kjgzRQJoTadIpAqkZ5xKUlNzknSrqZgk4hHixeanPT2mMRU/
M0U8EaOrq7m07PzkAkbxCXNHRzPp5jjp0fKT987OZkez4EIkwqhrv7OLeUZnZrhxVw9txSiMmcwS
6RFznGhEN/cXjXJxepGOzmZ6imFbyeJ6HR1NGEAmG6xEtbQmWZicJ92aoqurlVhUJ91qnpLOrhaP
t6f1wkwpP6ejo6l0zLl8AV3TGJpaJGuY27S1pUqfp8fm0YrHrGtlA7ejo5me7maMSIT0VNkz0t7e
xPSCV5kemckyNZ+jw4AtPa1EEjHSEz5lqwPo6jLnaGzOG7HQ1paku7uFI+dnSLea3pjN/a2cHvIv
y93d3VJS4u0sGjCRyZXGzKHRnIqV5mJieqE0fsKldyfjEdo7msmikZ7NkkpGmV+o3gGhs3j+pxbz
zGW9z+g7OlIUdL2kUJvrt5bOtZ1oREfTnEVFLHmB0rXecsa5bVdnM/O5YmhhzmCLredoe3raYcz0
9LSSyixxZsw0yLu7mlnw8X52dbXQnIqxaMD0ovN6KF1brmNYMuDEyBw/dcNGwHyd13Tyuk5fZxPp
i2VjLh6LkKhSHbCtvYmWdNIxB+nWFJ2dzaVlTc0JpuZzjnViiVjpfVdXC+lW/+toPm+U1kslo8QW
rGsnRTwV5+yZqdLn0XiMlhbzogkq2xaP6ZwayRCP6aXtmluTnnusq6uF+cUc6WmvR9Ka27bRDFGf
6J6L04ukW1N0FA1Ha/2Vph4D6w+BQ8C3MA2qVwNXSSn/ZCUFW2/k8gU+8bVD5PIGv/CK3bSkYtU3
Uqx7dF3jVS/Yyk27evjUNw/z6OFhDp2c4M13XsXzrulTuVkKhZeXANdIKbMAxd6LDwOBBtZKMbEC
vewiusbEZIaRkRmmZ0wFb3R0lmy+UHpvMRrVSstiEd3MTwJGRkxlyfpsIhGhJWYaVZOTmVIi+Nh4
lKX5Jce4Fy/OEI/ppe+W8cl5z36ni3/l8VG2FRXVmYxznJGRGcanF5iemWdsLEq8+Kx7urjeVCJC
oWB4xrYzO7tAS0uS6Zl5Tp+dIN0cL61/8eJUyRAcnZonmyswOZkpKcpjMb10zI8cGiIZj6Jr5afp
UQxGRswHVZNTmdJT9bameHl+xmJEjQIjrjkYjWm+cmfmFskVCgxd1GiKaEzMLFY8Pjfj43E08N0m
YhQYaTJVOuvzlk1tgeOPjMz4Gljj43OlbeYzS2ZJ+3y+dM1MzQbLPA3850PlohJ6IcH0XOXeRgBD
wxHmZhcYn/YfO67B7Kw5dwDJiMZIKuq7roZGNKKVrvV0a8qxXiGbI2J475WpRKS07ODMPE3R8m9n
binLrM2rMjIyQ2YhV1p/OhnxlWVkdIZMMsbUlPcecd+Dbk6fNUPyLhbXG4vpRAqm3N3pFKPT8457
OognnnGOb83HsZPjpX0nIl454np52ZETY4FyHpD2uY2V5imKwbHTzv5hpwuFUNeDm588fYGutqTz
HhubLZ2D1qY4M7YWAKVrdSrj8Y5B+biixe8ca/16CTLQ6snBeomU8j+klHNSyoyU8guYoRGKZfC1
h05yeniW2/ds4Mad3Y0WR7HG2NjdzP98y17e9JKdLGXz/MPXDvFXX3iCi6rSoELhZghnY+ElzFLt
tXKBcrhgN878rFVD1zX/PBGfRfawwEqKmD3UxpkO5a36NT6zwI8OXyzlflUK0lkseszGphaY9Mnf
8qvEZuWX6T45WIlYhFjE5j2zbTjtamDs7g906uIMhlGuwmdta/1dWMqRWcwR9/Ew2udH0zR2DbY7
tjVccxRUatvelLZgGIzPhPdemfumYuZ+LXVM7KtmFnK+ZeStfmF+c+LGLxywtyPF5t7q3oFzo7M8
c3qC4cmA3yt3MY0KV52Bf5l8i9mFrKdxMFSOLo1FvapyIl5eZl0fqXiU3vZy41pLjmhA3tzCUrB3
78CxUQ4cK1fDtB9XDUUVA3EUjPDNmSwvPB8QAuk+59VCFmOx+gqX67rmldEo32ctSX+HRLX5uRxz
sLqEEK8EHiy+vx1QiR/L4MSFab7xw1N0pZO86Y6rGi2OYo2i6xovu2UzN+7q4bPfOsKTx8f4wCcf
5a7nb+GVt252hPUoFOuYUeAxIcR3MB8yvhA4blXIlVL+v+4NhBCtmCGBzUBKCLETszDGy4rVCZ/H
JfCAganUuBX4gmH4Kjf1VA60KzJj04ucsZW5BkoFBs6NztGZTlY0sAzDIJvL8+w5b7lxKOdBOcot
G+XP3MfZ1pwgEY/4JsW7DQT/ctAGkYhOrlDep7unWLkSnk0mh4HlNQzdc+/Xp8y+nmGY1YIrlaT2
Q0OrrBTWcrot2QsGB4+Pomsat1zdV91ICxAgHo2wkHUaDBFdY6C7mdM+56sS9jBMMO0r+26D8oos
cnX0fKuUL+a3q4ius21DmhMXyuGDHa0JBntbmJ5bYiGbqyhjZiHLweP+xUyCZTDHs66/5ZScd5c8
99+fifu8WrQ1xx3Nwx19qvzysYqfb+tPc2Jo2vN5ELpWzle0cv/OjsyWivM0J/1NmeqX8uVXRfD/
AX4X82ndecwflfespFDriaVsnk98/RAFw+Add11NKlGPzatQlOltT/Frb9zDe157HS2pKF/5wQk+
8IlH+cmRkZpKtioUVyjHga8Bc8AM8A3gMOXquH7cDTwL3AncUnx9H2Y9h/3F159cVamL6LpXIQoy
pPJVwodK29uVLZtakln05i8U3AZIhe8UTdMCK/OZn3uHKJQ8WJpHAdK0YAeOu/BB0JxYhTcsZc/d
qNWvAavbWHOX6Hbvy/JMBSrtRkDj4SpU0werFQXxW9ftyfM7n5XGTTfFuWZLp2/REKsAys6BttBy
gc+8aS5l2KjNlgxDpbm19nXN1k72bO+ybVNsm2C7ZnVNKxWFKBQMFpZyvrdImLLn1WS1zllnq38R
iko4m/b6nPOQBTRaU+V872oGn/V5rXaNvSCMNefTmaWSIZ1KRnnOVT2l3PPyd1PlcS87D5aU8lHg
diGEJqVU2toy+dKDx7kwluHOvYNcvaWj0eIorhA0TePm3b1cu62Tr/zgBPfvP8tHv/Qkuze383N3
7mJTr38fEIXiSkdK+Yd1bHMPcI/PR59drjy1YiobhqNEeb7gHxZl9ctKxaPMF8ORNB8TxbFtlV/1
ckidVdo5mGpV2SxF2m6glJQw3StppUKBE7OLrr44/utZoVEFH+Oouy1VVFanAkvcaz5NZoOOMaJr
FAIMzEjIEuZu7IZGW3Oi1CdL07Rl9xAD//NZadxUIkq6Oe57Xqzz292eYnRqgcmQ+TduD5Tbc2eG
y9WmfrqrUkZ13bEfPwOxvENzu9ZUzDH/1hm0riHrI2uNw6fNPKotfV6jPVejd9mwGZXuuW5ORsks
RAM9TX44woKreLACZcIsSsG8tU15owmfcvilfdZo2ei2LxK/LVOJqLP5M1bVvcoHEbrKZZ3U02j4
BswndS3AbiHE7wPfllL+aKWFu9KRpyf49mNn6Ots4u59OxotjuIKJJWI8qY7ruJFNw7whe8c5eCx
Mf7gU4/ywhsGeN3t20k3q2qDivWFEOJ3gd8CrDJhGmBIKddEDK2lFDx7phx2F+StyRYrsrWkYiUD
y8JZstvuwfKnORlz5G0UDMP0/lRRxCopOSUDyxEiaHkDKo/rx8kL5bCjagr4+MwCmYWsQ9GN6GUX
mYEZxnVhPON5Mm/pZWdHZx1/3QQpcAUzxq2ifH64y4O3t8QdjYgto7cWPGJUe+rvkcl/uf0z9+t6
sM9lPdPnNvZzhYLDQPU7VzOZJSZnl4KnxPIkWR4s3X8y/LyVYXpi2XHkYLl24L4uwGtAuikE3P8W
oYxhw8AwyjuuZjNa+6n10YKfB8uiOVluOl36pGxheceyhZ+utgernkcoHwXegZngC/CvwIdWTKJ1
wvxijk9+4zBo8N/vupqETzUfhWKl2NDVzK+98QZ+42duoL+zie89cZ7f+fsf8uXvH2fep8qOQnEF
8zbM5sDx4r9Y8e+aoNQfx1bUoRAQMmX13WlpKieBWwaPo7BEwGs7fon6uXzlZ8SaplXMA3OHOoEz
RLDWlk/2Sm9B+91uK7998PiYI1/KsUvD4PCpSd88KbuSF57DCqQAACAASURBVGRcgX+PMEu2eqK1
7flf4PS6zGSWHM1gN3ZXjlIoe9/KgoxPLwR4sCqcQ4ItLLshsJx8F8MwXA2QVyZ4Km4rXuEn3tMn
xzk3Ws71cR+DpdgvZp19lTwNmH3EtQqIhMWw2UqeCEoNzwOUqMtDag/lA2fYa73TWcDlfa5iYZW+
s2oNEbQZS55eYK78SLAXk/Fib93g581fSeoxsLJSyoPWm2J/EKWh1cjn7jvC6NQCr7x1Czs21haf
rFDUy3Xbu/jDd9zCz790F7GozlcfOslvffxhvvnIqVLFL4XiCudp4KyUMm//12ihwrLd5/eiEGRh
FYnqOrfs7nPkKNhNo4JhMDa1wFPHxzw5SRZ+IW1himhUDBHUvVUE7UUu3H2swF9RT8W9wThBsrnz
nO3rucfxmwtNc3rXmirkTQd5sPIBRUkqjQXFYg+293al2V4lckNnc4gwcK8SeuTspCPMMngrH9l8
jlWvLwrSu09XaOjE7CLHQjRmtuMnXyRiM1YrGIC5QqGiMm7lKlby5i2XglFbWKT72K7Z6kxBceZd
1okRnL9ZiXoMm6DwSHf4rmMbH3EiemWjeiWpp6JCTgixjeLxCiFewepcT1csjzw9xENPDrGlv5XX
/NS2RoujWGdEIzp37B3ktuv7uX//We595DT//sAxvvXYGe56/hb23TigKg4qrmT+GTgohNiP7eGg
lPIdjRMpPNGI7gn/KRgGeoWfYU0zDRZLifQLsQqq9Gffr5uZ+WxFpc+oohT65WAZNg+Wn4EVVjZP
MY4i7jGtz3vbm+jtSDnyOPxyqMx8IM2xJAi7gZG29c+aX8g5+vaU169yvC6vXlNA9bQwGJ4XJlM+
oWHOHD3/cEn/EEHNs149FAzDM747x2dTbyutTTHfEuxB2BV999yfdVXP9JPfrdC7c7Esaik+EoT5
UMR/v5qm0dGScMzJxu5mjpw172krP2lDZ3OpkbMzB6uOcFUrp82o/cRqGuwabC/JZ8eeL1qSzyZj
GCPKCLq4PXJcfh6s9wNfAW4TQkwBfw68b0WluoIZnsjw6f+SJOIR3v2aa31/GBSKS0EyHuWu52/l
L375+bz6BVtZzOb5l/ue5Tc//kO+8cOTpbAIheIK468xQ9u/Bzxk+7dm8ChwBoxWKPltKY/2EBpn
WGB1BSsa8Sojx89X9iIUjMp5GeUqgt4cLHc4XCX87BJrv+5D8yjFxRXSTeUCBqby6HzaXR7AOf9h
S+Hv2tTOrdf0k4hFAnNjIlWOV9PKXra25gQAgz6hgGGmrVxoLYQXMuC1Y59Vli0nHMswjKqP8Td2
N5c8tADJmNP4rJYjVs3A8sN93Vm5Vl7Dq+pQAPS0pUqNud1MzC6WKmV68uAw0wAstm9I096SqLgv
R4hgCNn6Opoc781+fPWVitc0jc500hGuCzDY08KeHV2lXnUl+Wy7cN+RhsODVVrq2c6iozXhs/7q
UM/jj1Ep5R4hRA+wKKUMX8x+nZPLF/i7rzzNwlKeX3rVNZ4LVqFoBE3JGK974XbuuHmQ/3r0NA88
fo4vfu8433zkFPtu2sjLbt5EW5Uva4ViDXG0nkqClxN+RkIlPd9SHsshec6Vw9gIQVXvKulXVT1Y
Vh8smwCW4hfRdTQtXOSmn+fHyi11K4DudUuFA7xuBzPMqhgxF4voZPOFYk+m8rpBTYXdWJuYRpv/
cVXzYEV1jVhUZ++u3pLB29OR8uSB1fJkPpR+7CiI4Pyo5IX02SzIg7Wpp4UzI7NEdD0wJNVOoWDU
7G3o72riZJVeS/awwGreUl9Dwp2TZT3ICLOtD8l4xGNc2DlaDIv0y8GKOfLJNHRdK3mZ/Ax6o0YP
VioR5cad3Txx1Gx+rGF5wusxsIr7dS3vaTc9yJGIRs7TU0tzblz6zD5u8VqsIFJfZ4oL43OlY1hN
6jGwPgu8REo5stLCXOl86XvHOTk0wwuu6+f51/U3WhyFwkG6Kc4b9+3krlu38t3Hz/Ltx85w7yOn
+fZjZ3nBdX3csXeTKu+uuBL4kRDiDzG9VvYQwe80TqTa8Ev0NgyDpkTMt3dV1GVg5fKGQ5kPoyTZ
FTg7lbY0qKxc6pqpBNrVv7KBpfnmxfiWA/dRji9OZNi2Ie05NveqpaqFutMYMDBIJaLMLWTpaUsx
PVdO0LePEVZ5tjw4leba12Nml724Y4cy7buv6jx1Yoxbr+kPXY679NrjEjT/LCx6jcagSMq+ziai
UZ1YRPcNE7OwjNqC4X/eY5FIYLGI5mSUXYPtDE0FV8NzeLA0jV2D7ZwamikVh6mGW6YBy4vkc3/6
4Wmo7FMN0H+/XgsrES+H9Vtj9nakuDjhX63Q8WDAJV5vexPDk87tErEIyXiUWEQvNfuFOou1VFnu
FwZo7Sfo/nWMazj+OPehadywo5vx6QV6V9nJUY+BdUQI8WngYaAURCyl/KegDYQQHwHeCgwDb5dS
Pmz7bBAzXOP5wDYp5ck6ZLrsOXhsjP989DR9HSne8rJdjRZHoQikKWmGDr705k089NQQ//mjUzx4
4AIPHrjArk3t3Ll3kBuv6lbhrYq1ygtdf8H8LV5DBpY3j6hgGIFFBSzF3HpKP51Zos3WosHbSFfz
en6Aa7Z0cuiUK8clQMPSNa0oV+Vj0XWNfL5AZiFLKhF1lLz281o0J2OeZZUKFCy5SmQH5c14bDSb
3IO9LTx9wjxuDWe/KbcHpr05USpx7dhX8eWG7ubA0MpqHqywOWlhH82b59j/BG3pa2VuPsfo9Hzl
SpHFv03JKFNzTsPEefjlN9GITl9Hk6Psvx2xqYO5hSxz81kmZhfJFwxiPiGqLakoE7P+xlBE12lN
x5nLGkzP+IfPuisydqaTNKdiPP5sOP+B/bpLxqK2UFzv/elHLKI7jLmwYbEe+8oly1Ixz6rS9WK/
v2dd52H7QNrHwDK/XPaKXgD2y5FiCHA9Fpa/C8ta7Cd20F4cuy8N659/aY2dSETZ2LP6D4tDG1hC
iD3F6oEJTP/2XcBo8WMD8DWwhBB3Au8FbgXeBXwMs0SuxQ+AozVLvoa4OJHhH776NNGIzrtfcx1J
n4pHCsXlRjwW4cU3beRFNwxw4Ngo39l/lqdPTnDkzCQdrQn2FT9TvbQUawkp5Yvdy4QQdzdClnpx
KyC5fNHAClDOLM+I9ffEhWm60knb9k4jwa34AaD5e7HcBlRnaxJNg7HpBWbns7SkKleli+gamcUc
B4+Psam3lYVignskotHWEqcrnWRseqG0fnMySn9nE7GIzplinkyQYZLLF5iYdnowwoQIaprmTKx3
rGd+N3a3pRidKivuHS0JetpTdLQmGJ6cZ2p2iZZUrFTMwhq9Up5VNQPKz8O1nDySfL4QqLi2tyTY
0NXM2KEFh3br0VmLAmwfSDMzt8RUZqlU2r5akYsg0VtSMTpaExw9axqiBcMAzXvslTx+1kdWiwL/
IhW29YtvErEIW/paOXVxJnBsX7y2dIkgD1Ys6rzP9JAeLPc1bL2zCqlYH4c1sCqRikdpbYp7qm/q
uhlmWCkHcefGtlJYo0PegBBB60h88yQDilw02wq9lL3EgSIRfNWtPLVo+h/GDA18O4AQ4jtSyleH
2G4fcEZK+agQYhPwDiFEp5TSegz2c0AfcEcNsqwZFpZyfPSLT5JZzPGOV17Nln5vR2+F4nJG1zVu
uqqHm67q4cLYHN/Zf44fPHWB/3jwOF976ATP3d3HS/ZuZPuG9KpX5VEolosQYjPmQ7/u4qIE8BLg
iw0TqkYsBSIWiZDLF5iZN5X4oFYLEVeIIOAwWnKuSnmRiA4uA0vXNN9CF/Y+URFdZ9emdnP8Q0MA
XBwPLr4BZvEMq2jYmeGyUmspvFcNtjNzZISlojyaprG1P81iNl82sAK+d5ayXgPCva6Vv+QIESz+
dRpfzpF2bmxjNpNlIWsKn4xH6SwarX0dTfR1NHFxvOwFsL4bK3mpqnmw/D+v4XG/i2yueoiXgcHM
/BJD4xn6OlIsZF1equLfRCxCoj3l8IY4IgR9D83/eEueDFuOnt+h+83Hzo1tTM4ulXqLVvpJCsrB
2tDVzMjkPJkqPSLtu7e/9pYS99++KRlzzpcWTv33qyIIZiGVi+MZNnSboYpBeZO1sHOwLdBrnCsE
G+hgPqjxw5K+JeUct1SRssIlbT9nLckYVxW/b+zbGQYsZfNeL3zAd9hqUcvs1ytVH2CZsFYXvFIC
kpTyh3WOe9ljGAb/9I3DnBud4yXP2chP7dnQaJEUimWxoauZn3/ZLj70K7fx8y/dRXdbih8+PcQH
P72fP/jUY3z3J2dV42LF5c5ngHHMsPT9QA9mCPuawXpq3NYcdygj2bx/wQBLEfVrFgz+/Z78iEUj
bOhsZufGNtqLVeyWquSrVKtSVy3vKHi7yt4RMOcjbJU/v8qM5dLQZpggQFdb0ncbXxlCGgUW8Zh3
LrrbUsFCBxDWO5HLF0IXKTg5NM2pizMOIxj8wtWcnkCL8kOB8OfbujQKBYOoj/fUz0PT3ZZi58a2
cA/77AaSa6xKYad+A2gOY80pa9D5SMZd7VA0/7BYN+6ZsDaJRnQ29rSUZA+632shqPqjrmtmiGCl
RuIB+7eOsSUVK1XDtOM26EwPVkmgEgPdzSVD2hzXemXwtE+5/kQsckkfAtfyzeZxDK+kIFciX3rw
OD+WI+wabONNd1zVaHEUihUjlYhyx95B/uSXnsf7f/ZG9u7q4dzIHJ/51hF+46MPcc+9z1St4KRQ
NIiclPLPgYtSyr8Ffhr4lQbLVBNWzlQ06s2VcmMv+1y1z1KRnvakZ5mlzG7pb6W7LeUbjVFPRbHQ
eUUu7McSVMnv1NAMo1MLvp95xvMoXoYjLLCvo4lbru5zlAJ3hxW68Tsy++Hu3dXr+Kw1FXMo57sG
29np01jasQ+fnfR2hDPKsrlgD4TfdTU07i2Y4PWmBO8L3NXu/Ne1zq1VaXnrhlbiPr0Zw9lQwWFj
mqbR4uOdgWDjIAzuazrICHGvpxPumMLex/FY7f0sdww4r7dK5yhfKHgeoNjvoyAj1b7YbmRayz3F
tOz2VYVDL51rKBbhcOJnpK8my0kGCvtNegGwfHhWSMb5Zex3TfDA4+f4xg9P0duR4j2vv14VBFBc
keiaxrXbOrl2WycTM4v84OB5HjxQ/relv5UX37SRW67uVbmHisuFVLG4UkEIsR04BWxtrEi1YS9l
bseuFG/pa6Wvo8mhjIU1ZtpbEjQlokSjOk8eHwO8+Vd+3pYwaGgM9pR79tT722hX3goFg239ac6P
zTkUK7+KioFyubxRjofmVnhfBWPC34PlXWg/B5GIezyNa7d2kssXHLmte3f1hjZe9+7uZd6nWXCp
MayN+cUc0ah/Dm3Ya8W9VpBS3dmaYGJmkb5O/8ptOwbaOFYs/mGNkUpEufUaM+BpbiHLOVc5+rCG
RhA6cO22Tl9lNsxVaW/0bD8/7vMadOo8uVQhPViapjHQ1cz5sbnSez88HrIqDPa00NMezji3n2d3
43OLWh+eBIXRTmeWSga6fb9Bxx003wO2XmGXglo0nhcIIU7b3vcW32uAIaXcHLDdfcAHhBC3Aq8C
HgMWhRBJKeWCEGIn5ZDBLUKIjJRyuMbjuKx44ugon/mWpCUV49d/5gbHEy+F4kqlozXBq2/bxl3P
38pTJ8Z44PHzHDg2yj33PsPn73+W51/bz4tuHGBzn8pDVDSUv8DM+f1L4AnMok2fa6hENWIpyrXm
7IRWmjU8ve/chlBE132rDVbj+u1dDsW0tyPF6LQzT+u6bV2hxrIe2hiGWfp7MZsvKZ214jQMLK+H
YXvnxWlghfNgaa4n/PY51DQ8xQQguES+v0zBXgPDMPd5w85uHn92xMw/G3Wut6WvtVSSO9wOvfvx
o7s9RWdbMtAAq1YsqTkZY++uXvYfKauHoa7nSh6PokHj62kMea9YRVgczXBdxxjkYXXfU2YVwer7
1DTY3NdqM7D814vHInS0JEpzW21sP101aBv73Ou6VmqEZr+eI7pZEh3gwLHyhRY0V5rPMvD3RvnJ
Zr1/6sSY7/q13EcrQS0GlqhnB1LKB4UQHwK+iem5+kXgXmASeC3wrG31B4B/Lq6zJnn6xDgf//JT
xCI6v/rGPaqZsGLdoesae3Z0s6fYa+LBA+f5/sELfPfxc3z38XNsH0jzohsHuOXqPkf8tEJxKZBS
ftl6LYToBFqllBMVNrlscSsMHS0JJmZN74Wf3RNWafRT0v08TfUYWO6h081xtm9Ic/yCGVLc0ZLw
JL8HjlX8W1epaBf244voGrm8QTRqen6CjRa7sRQsnx23UWAZOxCy6a9Hhsrvy/JpxYbUBolYJNDr
0JSMOUr4V92/R57ga8ytODuaxIbYl/t6rze8tLz/Cj3aQnvwvCGI7kIKQftpb4nT054qFYqJRvTA
nCfHPt2e1Arris0dVccD86GG330XmIOluQysIhG93CTYemAQNsczVP5ZBQ9Wte0vZYELqMHAklKe
qncnUsr3A++3Ldpn++yKyeU6dHKcj3zxIIYB77v7ek8sq0Kx3uhMJ3nt7dt59W1bOXhsjO89cZ4n
j41x/Pw0n7//KC+4rp99Nw5ckp4UivWNECINvFNK+dfF9+8Cfhk4KoT4FSnlxYYKWAf2ggGdrUl2
bEzz2DPmE34/lS5sQQm7btmdTpmln30UTvuTazc37Ogmmy+QyxXI5gqcKOZk+nkw7N6LWpLQ601Y
9zMu7MeXiOlMZZaI5fXKVeiqyOK3LB6LsHOgjeaiMpuIRdi+Ic3Y9GLNIV3gVYCD816cy1OJaKn6
pJ2ajZaQOVj+OJvs1kqY69ka1e9+CPIsAWzsbiGViBKL6py4UCGfWLPGL4/lvlf8DFkwj3nHQFvJ
wErEIp6HBXt39ZDNGRw8XvYAeU7RChRuSASF/FbIwbKwXzPOvl6a46+F3eBcjuieaQhYb1t/momZ
xUv+QFclRawQT50Y46NffBLDMHjv6/dw3fZwIQ4KxXogouulUu+jk/M8ePA83z9wgfv3n+X+/WfZ
OdjGvhsHuFn01pWYq1CE4O+BkwBCiF3AnwE/A+wA/gZ4U8MkqxGrB5P9iXNbS9ypcPo8NQ8fIlhe
b+dg8IPCSh6JVCKKlc0xbisJ76dQuRu+hsVatVztL9y2V21q57C7YbKNRDwKmSUWlnIVx7R/1uQT
2lcpXM5Ob0cTvSsU7RJUnMG9OEzoF5iGhjv3yTGuZz/1acxhN9s50MbRYq6WO9fJf1xnuKedSgZW
UzJKU7KFqTmvEeocn+L45WX1VsaMx3RHOFwsohOLRigY7gbO4T1YYQn00gauX35drVKn+5qwh8H2
tKdqCuutlPcYdA31dTYF5v6tJsrAWgG+f+A8n/4viaZpvPf117NnhzKuFIoguttTvP6FO/jp27Zx
4OgoDzxxnqdPjHP07BT/ct+z3HpNP7ft6WdLX6vqq6VYSbZLKX+u+PoNwL9JKe8D7hNC/FyF7S47
dgyk2b4h7ezd5DZ2fLbzM17amhNEdI2mRLTcEyrkfRdWj6xWUt3ZT6h2D1bISuylsd0hcO5QfiuU
qGAYRCsaWOXXjWq47hYvqGiI+/pwGxdtTXGSiagnB2xTb2UDK2wOlh+pRJTO1iSdaW+p7iC621Nl
AyuEMe4nT3MyxtxCttSEuKKMVbyKesmA89+Hm0Qs4skpunpLJ9lcvpgPZg87LXqAPPs0/+4YaGMm
kw0dUpuIRZhdCvKm+W8TtLy1KcbFYmD1/JJ/axb7vXzTzh4iEY2I7gy5rXYOk/Foqfm4e0z3Nb0S
fb9WEmVgLYOCYfDl75/g6w+fpDkZ5X137yk1WVQoFJWJRnT2il72il6GJzJ878B5Hjp4gft/cpb7
f3KWjT3N3HbdBp5/bZ8n4V6hqAO7lrgP+KTtfbgkARdCiDjwT5il3ueAD0opP1qvgGExk/OdyyzV
YrCnhbMjs7T73DP2J/5WVbl0U4yNPS1VvUx+uI2hoCRyrYIh6F5W0zMVtwer2uq2wduaE0zNLfLc
3b0ej0NYeSyFLmxY3mqgaRqxiE42XyDdFA9UWN2itDXHHQZARzpJfx1P+d0hirWGeFo6U9h+ZbXu
y/IMbulvLYX6bR9IE43ooULGrIiKWMR/Xeuab0461elrt3YyObvIkbOTjuV+BpbD4Ld7aHQrxM65
T+u4e9pToav+AfR0pOjobIZsC0+dGHf0sAueS//l9l5VuwbNBsdTGZe3z7ZpIsBQreax9uRNVfBg
rUTfr5VEGVh1MjW7yCe+foinT07Q057k13/mxrq+nBQKhfkj+MZ9O3nd7dt56vg4Dz15gSeOjvKv
3z3Kvz9wjOu3d/KC6zewZ0eXKoyhqJeoEKIXaMVsMvyzAEKIFqDe+r1vwCzWdCPwDuDDQoh7pJQV
HvmvDpaCNNjTwoauJt8wJV3TuH57F4YB+XyBC2MZOlqTju3drythV47amuJstfXcshOmKbBdxrDo
mJ66sKq5fWyxuZ1CwfCdJ2cYUrA81njLLbawXKJFA6tSyXu3IjvY20IiHikZHfXagmHDtKqh6xrX
besiHqLS20BXM9l8IdS10pyK8byr+9A0jVQ8yvxSztPIthp7d/UGHld/ZxOxiE57q/OBhq5rvg8c
+jubmMlk2bahejXdkgfLtfN6wzB1TWNjTwsjIzMMdDc7elWG6Vllx37Nt6RitG/p4Nkzk/S0p0pG
ZRg5g+6dpkSUzGKOSIVCFu4tlQfrCuDA0VE+9c3DTGey7NnRxTvvuppWVYpdoVg20YjOjVd1c+NV
3czOZ/nRoYv84MkLHDg2xoFjY8RjOnt2dHOz6OGGHd2BT8UUCh/+HDgENAF/IKWcEEKkgB8A/1jn
mPOYZd4vAsPAQvF9Q6mUA2JXLu2e4Xp0NrsCtX2gLfgpdRXjzf651e8mFBXya/bu6sEw4CfFCn0A
fbYGvLqmoQfk8NhlrPRAxypIUKtyutJYnslKXiCPx1PT6EonSwZWTfNuw23U1av8A6FD3eytPrb0
tVYNz7TOZ7o5XlcoZ6Xy3tGIHpjf4zFqu1voTCd53jXeRt6lbez5iDWG7dXCcoewH5uum+0GrIqF
uwbbmV/0Dxv0yBFwMNdt76JQMHj2jNMDaJ8Tb4igMyTxwvicryf/UqEMrBoYm1rg8/c/y/4jI0R0
jTfdcRUvvXlQ5YkoFKtASyrGHXsHuWPvIGeHZ/nR4Yv8+Jnh0r94VOf67V3s3W0aW379YxQKCynl
vUKIDUBKSjldXDYvhPgtKeW36hz2y5jtRUYxf0/fJaWcD1q5o6OJaHT5DwV6esoKZrrVzEfp7Gqm
ZxmFEqKJGOmJBc/4lRieWaJQNOb6+9OBHpSFpRzpYTORvbfHm1tpGAbpc6aiv2WwnR5XVdH00CxL
2TwdHU0O2YamFxmfWiCdTtHT00pW05hezNOUjDKwwQw9my9ANltg15aO0J6mhQJMzZsKYl9nU+B8
DM8ssVQwCyL4rVPPnNZD+/g8enSJdNGL4nd9dKQT6NOL3s/PzwCQakoEynjjbjh+zhxn1+YOejpS
5HIFFrN5T/h2LBlnaMq7n9UizD4uhRx+pOazpEcypfe7tneXqkdW4sLUArOZLNs3ttHT00q+YJTO
E0BvbyuxZXyP9PS0kkVjbC7rWGbHum56elp972vDKMvU35d23NO1zrd9X26GZ5YwbOGZ3d0tTGRy
pfXtv/vNC1nOjplfv4Mb2xncGC5lZ7WuD6WRhGBqbolvPXaa+398lqVcgZ2Dbbz1ZYJNvaq0tEJx
KRjsbWGwt4XXv3A7Z0fmTCNLDrP/yEjpgcdVg23s2dHN9Tu6GOhqUg8+FB6klFkg61pWr3EFcDdw
e/Hf64APCSG+IqUc8Vt5YiLjt7gmenpaGRkpK1vTM6ZCMT42h5ar33k2PbdUGss+fsVtpuZL20yM
B1cCKxgGhVyO9uYEowEFE6xxIoW0Z//dLTGOns2Q6Gl2HvvUPKAxOTnPyMgMEcOgLRWluy1ZWq8t
EYFEhPGx8FGbk5OZkjwtcT1wPjJzC0zPzBMl6bvOVB1zWg9T0/PMZJYgn/fsa3N3E8MT87TGI5ya
mac1FXd83t+W4MjZSTZ2pgJlTOrl82NkWx3nesRV6n0xm78kxxwW9/1yKZlfzJXmAmBsbJZMiAeB
mzpTzDfHSGgGIyMzFAzDM069lQqt+RgfzzjGdM/R0kKWhWyOsbHZQK+ktX3QPR2WStfL1GSGaVtu
V26hmfZUFE2D2el53HtuS0VJxILvWTcrcX0EGWjKwArAMAyOnZ/mh08N8YMnL5DNFWhrjvPWl+/g
Bdf1K+VNoWgAmqaxqbeFTb0tvPb2bZwfnePHcoQDR0d55vQkz5ye5F+/e5SudJI9O7q4fkcXV2/u
UKGEitXiDuBJKeWjQogs8DvATcByjLbGUMdPWjyod44LXTPza0Kt6+Nlam9JcPPuXs9yTQOMcoig
rmls7K43nc41bgV5LDb1thDVdfq7/D2HlRrZriSWhH57a0nFSqF312/v8vTa6kwnSzlKYagULgeE
yqFaL7inNOz1oGkaTbZQXveZWQn9sylZWf3fs7OLfN5YVshnaFkSUUL2IkbXNAYq3OMrcf+vFMrA
KmIYBhMzixw9N8WzZ6Z44ugIY0V3elc6yStv3cxP7dmwLLesQqFYObRiwu7GnhZe81PbmJpb4qnj
Yxw8NsZTJ8b57uPn+O7j54hGdHZvbuf67V1cs7WDge5m9YBEsVIcBe4WQmwHXoqp4x5trEj1kSj+
ttVSAKDRDy4Ge1oYnlmiq3tlC0w5+nJV+K6I6DqDFSJZ6qmMVw8leavsLujchvk+HOxu8TTBDRrr
um1d3upv65CVKiO+UkUu7LQ2xdmzvYv5xbyjSbJ9H3r00pzDPTu6wz+MWEOX1bo0sJ54dpQfy2EK
BYPMYo7x6UVGpuZZXCqHV6QSEV5wXT+3XN3LNVs7YftCNwAADY5JREFUK1bnUSgUjaetOc5t12/g
tus3kC8UOHZumoPHygbXUyfGS+tdvaXD/Le1g+628GVuFQoXHwduBh7HLAP/61LK440VqT4S8Qh7
d/XUFHrUmoqXiiWsBPEaH2CmElFuHuxY8RAwPaQHqxqXyIFV9mCt4g4rGZJuwharuNKxXzo37Ohe
VgVcXdMoGCvrUWpKxhyeslq5WXi9yvUSZOS7r+g1ZF+tTwPr4acu8GNbiHwiHqGnLUVvR4odG9Nc
NdjO1n7/xD6FQnH5E9F1dm1qZ9emdt6wbwfj0ws8fWKcw6cmOHxqgkcOXeSRQxcB6G1PsXtLO1cN
mut3tyWVh0sRCillBlhTTYorUWuERlMyys27e1dE6btld98lq7pXDUclt2UYWGE8PivB5TJvCif2
35GVKsJ0Of02NUJHvowOvyrr0sB692uuY3xmAV3TSMajpBKRy+qiVSgUK0tnOsntNwxw+w0DGIbB
+dE5Dp2a4PDJCeSZCR48cIEHD1wAoKM1wVWDbaaBNtjOQE/zJYlDVyiWQ6Mu0ZW6N5ZjyKw0zhDB
+sfpaE0Qj0ZWvSDW5r5WsvkC2wP6kCkaw0rek5axng+brHSF0N2WdBS5WEu6+ro0sHRdU2FBCsU6
xZ679dKbN5EvFDg7PMeRM5McOTvJs2cmefTwMI8eHgbMBNydg21cNdjG9g1ptm5Iq5LwisuG3Zs7
uDieaWi/lysNuw5Xb7U2MJ/wP2dXzwpIVJlUIhq6iIji0rGSxsDG7hbOLbNa31qkt6OJ9pYEkYhG
LmesqcgypSUoFIp1TUTX2dLfypb+Vl763E0YhsHFiXmOnDGNrSNnJ0u5XGDGgPd3NbFtQ7r0b1Nv
syqAo2gI7S0JZVytMCvlwVKsb1Yy8iFsxc4rkXgxdy1Se4/ohqIMLIVCobChaRr9nU30dzbxwhsG
AJiYWeTYuSlODE1z4vw0J4dmuDA2xMNPDRW3gf7OJgZ7zH5dgz3NbOppoUvlcykUaw77LaspC0tx
GVBrARhF41EGlkKhUFSho9Xsw2P14ikYBkNjGU5cmObEhWnODM9ydmSWC2MZHntmuLRdKhFhY3cL
A91N9Hc209eZor+ziZ721JoKdVAo1hOpeIRYJEIsqtOkwoEVy+D67V1ElxFmatHaFCv+XWNunHWM
+uZQKBSKGrGaHQ50N3Pb9RsAs0Ty+PQiZ0ZmOVs0uM6OzHH8/DRHz015tu9uT5Y8Zd1tSTrTSTrT
CTpbk7Q2xZTnS6FoELFohL1i9XOnFFc+tfSVq0Q0orN3V++aqqK33rkkBpYQ4iPAW4Fh4O1Syodt
n70c+BjQAfytlPIDl0ImhUKhWEk0TaOrLUlXW5Ibd3aXlmdzBYYnMgyNz3NxIsPQWIah4l97bped
aESnszVBZzpBa1OclqYYrakYrU1xWouvm1MxkvEIyXiUZNx82q6MMoVCobgyiUVV1MNaYtUNLCHE
ncB7gVuBd2EaUzcWP9OATwD/BnwT+LYQ4otSyidWWy6FQqG4FMSieqlqoZvZ+SwXxzOMTS8wPr3I
+PQC4zPlv8+cngy9H7PtRIRkIkIsohON6ER0jUhEIxLRiepa8X35R7pgGGD+h2EYpcaohmFQMMzP
C4XiP8OgULAtK/41DLjr+VvYd9PG5U6VQqFQKBRXBJfCg7UPOCOlfFQIsQl4hxCiU0o5DuwABoGv
SSm/K4SYBV4MKANLoVBc8bSkYrRsbGPHxjbfz3P5ArPzWWYzWWYyS8zMZ5kpvp5byLGwlGNxKc9C
6V+u9DpfyJEvFMjlDfJ5o66mp7qmoevmX03XiGgauq6ha2a7C/O1dln1MFIoFAqFotFcCgOrD7AS
ECaKf/uB8eJnuD7fUG3Anp5W9WuuUCgUijXFSv129fS0rsQwVwxqPpyo+XCi5sOJmg8nqzUfKqBT
oVAoFAqFQqFQKFaIS2FgXQDai6+tzO/zts8A2ov5WF22zxQKhUKhUCgUCoViTXEpDKz7gE1CiFuB
VwGPAYtCiKSU8jhwHPhp4BVAE/DtSyCTQqFQKBQKhUKhUKw4q25gSSkfBD6EWSXwOcB7gHuBzxdX
+SVMw+ufgd+TUj692jIpFAqFQqFQKBQKxWqgGXVUllIoFAqFQqFQKBQKhRdV5EKhUCgUCoVCoVAo
VghlYCkUCoVCoVAoFArFCnEp+mCtGkKIe4BfcC3eJqU8eemlWT5CiDjwT5hFP+aAD0opP9pYqepD
CJEAPoF5LOeA90gpH2ioUHUghHg95jl5Qkq5TwixBfgCcC3wHeBNUsr5RspYCz7HkwQ+gpkL+XYp
5T2NlK8WfI7lWsxczqsxi+m8VUp5ppEy1oLP8dwOfBzYBvwEeJuU8kQjZQyL+1hsyz8NvJU1/D3d
KIQQH8Gcu2HMe/XhBot0SRBCRIB/BO4GJoHfBH6Ez/ewEOJtwJ8CMeAPpJQfb4zUq48Q4iXA/cAf
Ap9iHc+HEOJXgf8FZIFfAx5mnc6Hnx4JfI11Nh9hdTe/OSjO4aeBVwJHi+seqVWGte7BehfQWvz3
O5gTcbahEi2PNwCvxSwG8ingw0KIlsaKVDf/HXgj8ELgv4B7iqX41wxCiDuBD+NsHfBBIA/cCNyK
eQ2uCQKO5x+BLY2RqH4CjuVvMY35qzAblv9eA0Sri4Dj+RTwA2A3sAv43QaIVjMBx0KxkuwrGyLU
Gqc4p+8FXo55TXyssRJdUt4K/CzwPOBfMJUmz/ewECIN/B3wfzDvlQ8LIXobIvEqUzQ6/wYYLy5a
t/MhhLgO+Gvg54F/AN6HqTCvy/nAR48E/op1NB9hdbcKc/A2zMrmtwAjwF/UI8eaNrCklItSyllM
T9xvYlqfuQaLtRzmMS+Ai5hPKReK79ci1wHHpZQHMJ8abAF2NFakmjkN3ATYn1zsA+6TUh4DHgVe
3AC56sXveD6GqbysNfyO5d3AO6WU54EJTCNrreA5HinlTinluzGPZR4Ya5BsteI5luLDlb8B/nej
hFrj7APOSCkfxazIe4MQorOxIl0y7gVukFI+A5wEmoHX4f0evgVIAV8p/osDtzVC4EvAuzHvsyeL
7/exfufjVcAJKeW9UsoPSClfALyI9Tsffnrki1lf8xFWdwuag32Ynq9ngG9Rp563pg0sG+8FZiiX
fl+rfBl4ABjFfOLwa2sp/MzFGWBL8WnAc4vL+hooT81IKY9IKd1KbR8wVXy9ppR4v+ORUv6wUfIs
h4BjeUZKOSqEuBvzafd3GiNd7QRcawgh3oT5fXASMxTosifgWH4B84f+3xog0pWA+3sHoL9BslxS
pJQXpZRHhRBdwG8DT2AqQu7vYev3ZYryHK2Z7+ewFA3rDwC/YVvs97u0LuYD2IrZW/XrQoijQohf
Zn3Ph0ePBNKso/moQXcLmgP3umkhRFOtcqx5A6voKn8v8HdSyrXq7bG4G7i9+O8vgA8JIXoaK1Ld
fBLTyDqD6W6FteuNU6wRhBD7gP8feBAzf2mt81XM74M1EyLophjm/CfArzZaFsXaRAjRCvwn0IOZ
L7qe+SPgc1JK2WhBLhMMYDPmd8yXMHOK13R9gWXi0SNZ3/PRMNa8gYXpzuvDTOJb69wBPFkMA/lX
zNyymxorUn0Unzruxnwa8D+Ki081UKSV4gLQXnzdjSvPRNE4hBA7MJ/ePQzcJaVcarBIdSOESAkh
3g0MSCkfA74P3NlgseplL7AReASwlEJZTDpWhMP9vQPr5LunGF76WczcyjullD/G/3v4QvF9O1f2
HN0FvFcIsYCZ4/z7QIT1Ox8XMEMEHwG+iGlMzLN+58NPj1zP94tFLXPgXndSSpmpdYdXglV7GzAr
pTzUaEFWgKPA3UKI7cBLMZ/MHG2sSPUhhHglZn7PXcA7gP1SyguVt7q8KD417cOM+U8JIXZiVm16
mRDiM5hhaB9ooIg1EXA884CV2NorhNgipbzsDeGAY/k4MI2Z7IwQoqmeL8VG4D4eYBNmSOBzhBB/
jJmYuyaqxvkcywRwDeb32UbgPsxiF1fyj/lKcx/wgWKhkFcBj0kpJxss06Xi9cCrMXNFnyp6RP2+
h3+EmSrwOmAWMyT1+w2ReHW5E7PiGZiVzh4Fmli/8/E14PeFEM/DLEywgJkusl7nw0+PfIZ1NB81
6G5Bc5AG/lYIsRv4b8C365HjSjCwBoChRguxQnwcuBl4HPNk/7qU8nhjRaqb7wAHgf3As8DPNVac
urgbswqPxbPAWwCBeVz3YoZCrhX8jud7mAnBYBYgeA9mTPvljt+xWFiG/CnWxrGA93gkpiL1Ucwf
xx+xdox597EcAF4spXyg+NQd4JiUMnvpRVubSCkfFEJ8CLPAxXngFxsr0SXlVcW/X7At83wPSykX
hRDvAv4S0DBbg6yVwjChKSbpAyCEyGDm2vwjZn7jepyPx4UQ/xOzSEEOs7Lv/azT+cBHjwT+nfU1
H6F0t6A5EEJ8DngZ5u/uM8A76xFCMwyj/kNQKBQKhUKhUCgUCkWJKyEHS6FQKBQKhUKhUCguC5SB
pVAoFAqFQqFQKBQrhDKwFAqFQqFQKBQKhWKFUAaWQqFQKBQKhUKhUKwQysBSKBQKhUKhUCgUihVC
GVgKhUKhUCgUCoVCsUIoA0uhUCgUCoVCoVAoVoj/C3c+HD0I9iVxAAAAAElFTkSuQmCC
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h3 id="Student-t-model-evaluation">Student-t model evaluation<a class="anchor-link" href="#Student-t-model-evaluation">&#182;</a></h3><p>This shows that there is substantial range for the degrees of freedom from around 7 to 12.</p>
<p>We can also compare this model fit with the actual data in the training and test period:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[19]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">compare_distributions</span><span class="p">(</span><span class="n">moc_anomalies_train</span><span class="p">,</span> <span class="n">train_samples_student</span><span class="p">[</span><span class="s1">&#39;Y_obs&#39;</span><span class="p">][:,</span><span class="mi">0</span><span class="p">],</span>
                     <span class="n">moc_anomalies_test</span><span class="p">,</span> <span class="n">train_samples_student</span><span class="p">[</span><span class="s1">&#39;Y_obs&#39;</span><span class="p">][:,</span><span class="mi">0</span><span class="p">])</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAzYAAAG4CAYAAACXanLAAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz
AAALEgAACxIB0t1+/AAAIABJREFUeJzs3Xd4VFX6wPHvtBBSJIWEIj3ACRCkCKICAgtSVIoK2Cu2
ZdF1rT9XXV1de1eUtaCCBcWGsqJSBBEVpXeOIZSAtAiEkJ4pvz/unTCElEkyk0yS9/M8PoaZW87c
OXPPfe85570Wj8eDEEIIIYQQQtRl1tougBBCCCGEEEJUlwQ2QgghhBBCiDpPAhshhBBCCCFEnSeB
jRBCCCGEEKLOk8BGCCGEEEIIUedJYCOEEEIIIYSo8+pVYKOU8iilWpV47Vql1ELz7ylKqUcr2EY/
pdRpwSxnTVNK2ZRS3yuldiilugdge9U6RkqpdkopZ3XLUc7231JKPVyJ5Z9QSt0SoH0X17cKlhuh
lGpThe07lVLtqlS4E7czWCm1rbrb8WM/W5VSzSq5zo0+fy9RSl1ZzTJcopQ6pQrrLVJK9a7OvqtC
KTVTKTW6kus8oJR6N0hFEkEg7VXppL2qcHlpr4KkLrdXgVrfj+1X5RgtVEpdG6QincReUzsKBVrr
qX4sdh2wDFgf5OLUpJbAICBca10UgO3Vq2Oktb6vFnb7D+A/QHot7LvGaK2TK7O8UsoGPAO8GcBi
/Bv4CciqzEpa66EBLENl9nt1bexXhBZpr6S9Ko20V8FTl9urAK5frsoeo9rQoAIb865IK631DUqp
CcBDgA0oAm4DkoGrgTFKqUTgReBR4GJzE8uBv2mtc8w7uR+br79vLnMbsBP42Xyvt9Z6kFJqDPAY
EAZkA5O01muVUoOBJ4BfgTHAYeBvwJNAF+B1rfVDSqko4D2zfI2ARcDkkid9867UNCAeyAfuBRYC
SzB65zYopS7RWq/zWScCeAfoaZbvM631XeZ7HYB3MRqaI8DNwBkljtEp3mNayjFWwHSzPA7gQa31
rAq+o4qO1RJgHBAOXKu1/kEpFQ/MAjoBm4FcYE8p207BOAGdYm7/Ja31VPNO9zat9X+UUjuB5zAa
w1OBvwJDgZFABjBKa31EKeUBWmut95jb9gCtS+yvGTADaIfxvb2itX7evAs7FOiilLoHmINxchxp
lusNrfXj5jZGAa9g1NG3yzhmTwONtda3mv9uCuzC+N66AlOBSMAN3Ka1Xlhi/eLPX/LfSqmuGHWq
BVAAXKe1XlmJOuk9Lh0p4/sr8XEWAE2UUluBUeZr7ZVSSzC+36XAFVprt1KqP8ZvNBb4E7hca729
xP7fBhSwxLxjdAPG72wYxm/7a8qu/zuBKzHq0i9m+W8E4oA7tNYf++wK887kenO715jL/VVr/aVS
ygI8CFxhfvY55jZc5mf7CbgImAQ8DryltX7frPfPAxHAUYzzz0qlVGOM3+aZGOecrYh6Rdoraa+Q
9qqht1cbzePZD+N6/VGt9Tvmsv8BJgAWjPpzJUbwWby+1nqZz7avBSYCh4CzgTzgQq11qlIqppz9
eIB/Atea348Tsy4ppW4DbsH4vWrgBq11hvlbnAU0xTgP1WisUa+GolXSa8D5WusuwGRgjNb6v8Bv
wD1a6+cxKsEo4HSgGxCDcecC4A3gea11J4wLjs4+224KrDUbCTvGyeJGrbUCvgSe9Vm2N8aJIgnj
hzwVOB/jwuufSqlwjIukTLOsnTEqVjffD6OUsgIfAVPNiPoGjIoVgXFScmmtk30bCdNfgWiMH3xv
4Fql1ACfzzhLa90R4+T9XinHqDzPAv8zy309MF0p5ShrYT+OVS9gubm914AHzNfvBTK01u0xGtoR
ZeziIeC/WutuwFnAMKVUo1KWS9Fa98a4SHgP+ATjRGfFuPj01wPADvP7GAo8oZRqrbV+EPgD44T3
MXAPxgmjO8b3Ol4pdYF5N2g6xgm4C0b9sJWyn08B36FLo4FFWuujGN/hM2YZngT+62/hzTo1B5ip
te6McQL70vyeKqyTpSjr+/N1Pcfr6g7ztcEYv0MFDAH6K6WigbnAP836+RIwu+TGtNbXe7fhc5If
Cpyhtf6E8uu/r6aAW2vdHbgdowEpTTTg0VqnYFxQvWUerysxzidnYPzWk8x9e50OdNNa/+x9wWyM
PwFuNb+/p4EPze/lOqC5uZ2LgOFllEfUD9JeGaS9Opm0V9Tb9uo5jOOYjBF0/FsplaKU6obxe08x
P+sXwLAy2jtf5wKvaq2TzGP1tPl6qfvxWc+itVZaa5f3BaXUmcDd5r6SMXrznjDffhLjO00yP2v/
UsoSNPUxsFmijDGAW80o+okyljsI3KKUaqu1Xqa1vqOUZc4HZmitc8wv9B1guHm39HSMEzHAqxhR
s5cDo6KhtXYCiVrr5eZ7PwIdfJbN1Fov0Vp7gE3AD1rrXPNvG5BglvUspdRwwKa1/qvWem2JsrbH
uND5yNzvSoy7IH3LOlDmcs8BY7XWHq31EXO/HcwGaojPZ/wSo8JXxliMOztgDAUIx7iTUlZZKjpW
x7TWX5p/rwa8Y37PwTxJaK13AiXvqngdBC42714e0lqP01oXlLLcHPP/G4C8Et9Py7LKX4rbgFvN
cm0H9mN8TyWNBl7TWhdorXOAmRgNUieM4RjzzeXeLW0nWuvfAItSqof50oUcP2n29Pm75PGsSDKQ
iHnnTWv9E8ZdwLPxr06WVNb3V5HPtNZ5WutsIBVoBQwE9mitF5hlmwV0VP6NA1+ktc431yu1/pey
jh3j9+9P2aeb216IcS7ohPEdv621PmrW87c48aJjntbaXWI7/czP+JO5vc8wLkLbYdT5z7XWTq31
IeB/fnxuEXqkvULaqzJ2Ie2VtFejMXrq3FrrDOBzjGOdifFbu0IpFau1fkVrPdOPsm32qa+fYRyb
8vbjVVr7cj7wqdb6oPnvtzh+g+0czB5i8/uu0REF9XEo2mBtdrdCcfdbaZO5xmBE4KuUUruB2/XJ
3YwJGF3aXkcwfjixGHdlMwG01kVKqYM+y7m01r7jG29TSl2D0QUaDnh83jvmux5GdzZaa49Syo3x
I/xEKRWHcUcmWSn1PsYwFt+TXAJGo+O7bW95T+ju9KWU6gQ8r5RKNvffGqNBjMMIfI96y+MtWyWM
AB5QSiVg3A2wUHEwXd6xOurzt4vjd4PiSrzn+535uhejS3U2EK6Uelxr/Vopy3m/k+Lvo5R9+qMv
xl2vNua6LSj988cALyilHjf/3QjjLmMcJ46TLetzgXGSGqOMCZYDMIY8Yf7/NvOOkY0TL2gqEoNx
B3WLMUoDMIZFxPtZJ0sq6/uriO8x8K4XAySZF4NeBRi/g4rGgR/2/lFO/S/JZTbiFZXde8HllYlx
vogB7lJK3WS+bsdodE8qk4+S5x/v9hIpvc5Hl1EmEbqkvTq5vNJeGaS9kvYqBpitjievaAx8orX+
Qyl1EXAX8IpSailwi9Z6dwVl821njmCcG8rcTxnreSUAe0tsL9H82986HhT1MbDxi9Y6DbjO7L68
GvgQY4yqrwMY42294s3XsjDuOERorXPNrs6E0vajlDob4wR1htZ6p1LqXKow0Uxr/TrwulLqVIyT
wtUltnMAiFNKWXwaC295y/MqsAoYp43x/j+Zrx/COEnHA38qY45AEpBWYv2SP/hYALML/xNgotZ6
ntmFnldeQapxrI4ATXz+nUApjaN5B+WfGEMm+gLfKj8ywpShuJtdKRVbxjLvAy9gDCfwKKX+KGO5
vcCzWusT7ooopbpgnJi9Sq1jpk8xuny9d1GPmXXlTaCfNsZ9dwJ+L2XdUr9Ds1xZuozJgn7UyWDa
C2zRWvep5nbKqv9VZVFKxZu9KGAcy8MY5f1K+zch3OuE84/5G4wzXy+tzot6StqrYtJeVY20V3Wz
vdqLUdc3lnxDa70YWKyUisQYAvkkxwPEsjT1+TuO4wFLmfspR1nnG6jl9qk+DkWrkFIqQSm1QCl1
ijn8YznH77QUYUSvYHS/XamUijAbg0nA1+YJZwvGGEcwJin63qnxlYjRDZqujImP1wCR5onX3/I+
qJS6HkBr/Qewo5T97cSYQHaJuc7ZGF39v1Ww+URgjdlInIvRnRxl3smYjzFhDIy7WfPMRsj3GO0D
UpRSVmVMAjzPfD3S/G+l+e+/A4VAVAVlqcqx+gWjOxulVBLGHaCTKKXmKmNsKhiT8o5S9vdWkX2A
tyv9eoyGo6REYJXZSFyDcTy8n9/3GH4J3KCMNKcWZaTuHQlsA5zKmIgKxryKssr7C9AM4/vyduUn
ADnAVrP+3gTFczdK/SzKmPTnPX67gD1KqfHme02VUrOUUpF+1smqKAKs5h278vwKtFBK9fOWWyn1
Xhl1xcnxY11SqfW/imX3utws03CMi6PfMb7jq8x6jVLqZrNOlOc3oLlS6izz35di/MZ3YnzfY8w6
4/u7E/WMtFcnlU/aq8qT9qputldfYswVQillV0q9oJTqrZQarpR6VSllNUcSrPP5POW1d0op1cv8
ezzGcL8y91PBZ/oauEgZyTDAOK98bf7tW8fPxpjzVWMaZGBjjiH8FlihlNqMMc53kvn2F8BTSqnn
Me4qzMO4Q7QR2A28bC43GbhfKbUJ4wTwB6X/UL7FiIbTME68L2KcoD6tRJHfw7go0sroyiw0X/P9
TB6MC58pSqktZjkn+AyfKct/gOeUUhsxUmz+G2PiWH+MCZ2jlVLbzeUuN9fxPUafYJyM0jg+cRFz
2MPTwBql1Brz/TkYjW9kGWWp6rF6AmirlNqBkdnj8zKWewVj8vUWjDGzr2mtUyvYdlnuB6YppdZi
fP7SUis+CHyhlFqP0UC8DrxpNmafAh8ppe7AuAu5C+Pu1VaMDEPLtJGx5SbgbbPMbsoYXmF+/3Mw
JvHONV9eh1F/f8c40czFuCgqOYTlTaCdUioV41h+6rNNb53aipHhZZFZpyqsk1W0D2N8e7p5QiyV
1joP48T8inlsvsDooi/tNzgb+FkpNbGU98qr/1XhAsLM88IMjCwxbozvZi6w2jxeY4DvytuQeZwn
AlPNdSYDl5qf8U2M38Z2jPr+RRXLK0KctFcnkPaqaqS9qpvt1YMYWdc0x+exrTc/WwTwu/mbvgT4
Vynrl/Qz8A+z7o3B6HGknP2UyZw78yTwo3lMYzDqGRgJJkYrpdKAKRjZ42qMxeMJRNDaMCmfbnSl
VAZGVoqSWVyEEA2AMtI9b9NaN9ghviJ0SXslRMOlzPl7WuthtV2WYGuQPTaBoJT6BCMqRSn1F4xJ
bqWNBxVCCCFqjbRXQoiGQu4sVt2/gHeUUpMwujWvMrsbhRBCiFAi7ZUQokGQoWhCCCGEEEKIOk+G
ogkhhBBCCCHqvJAZipaRcSykuo5iYyM4ciS3totR58hxqxo5blUjx61qyjtuCQnRlXkoXoNSW+1U
qNfzUC5fKJcNpHzVJeWrnrpavvLaKemxKYPdXpkH9govOW5VI8etauS4VY0ct7ol1L+vUC5fKJcN
pHzVJeWrnvpYPglshBBCCCGEEHWeBDZCCCGEEEKIOk8CGyGEEEIIIUSdJ4GNEEIIIYQQos6TwEYI
IYQQQghR50lgI4QQQgghhKjzJLARQgghhBBC1HkS2AghhBBCCCHqPAlshBD10ty5cxgwoA9PPvlo
hcsWFOQze/aHVdrPY489zLXXXl7uMlOm3MR9991Z7jLvvfdOlfYvhBBChIJ9+/YyYEAfli5dwurV
KxkwoA+pqbpGyyCBjRCiXlq6dDEOh4OffvoRt9td7rKrVq1k9uxZNVSyk23fnsbrr79aa/sXQggh
AqlHj17Mn7+UpKRONbpfCWyEEPVObm4Oq1at4KKLJnLkyGE2bFhf/N6CBd8yYcIYRo4cwiuvvMC+
fXu5557b2b9/H+PHj2bevLkMGNCHY8eOATBgQB9mz/6QoqIiHn30X4wYMYixY0ewaNH8csvw5pvT
GDlyMJMn30BeXl7x67Nmvc/YsSMYPnwQU6e+CMDVV19SvK/K7kcIIUTomzdvLoMG9ePdd99i6ND+
PPXUf5gxYzrnnjuQRx55kKKiIp577ikuuGAYF154Hu+++xYAHo+HV199iQsuGMZFF53P/PnflrmP
stqPKVNu4uGH72fKlJsYOXIIX375OQAHDhzgzjtvY/jwQVxxxXh+/nkZYIxEuO22W7j77r9z7rkD
mTt3Dvfc8w9GjBjEZ5/NBmDFiuVcfvnFDB3anzvumEJubu4JZVm3bg3Dh59DWloqBQUFPPLIgwwf
PohrrrmULVs2AfDNN//jwgvPY9iwATz00H0UFBRU+zjbq70FIYQow8MPN2Lu3MCeZkaPdvLww+Wf
/H755WecTidXXHE1P/64hB9/XEKPHj05dOhPnnjiEW6++W90796DW2+9mT59zuCqq65j/vxveP/9
T/j++wWlbjM9fRcOh4Np095mwYJvefnl5xg6dHipy+7enc6MGdP5xz/upmfP07nhhqtITEyksLCQ
9PRd3HXXfdjtdu6++3bGjBnHXXfdx7PPPsH8+UsrtR8hhBCVU1vtEoDL5aJp06aMG3cxs2fP4m9/
+zs33HALr7zyAsnJXfn22/8xdeqb7N+/j/vvv5vTTutJdnY2H3/8AdOmvc2mTRt47rknOOus/kRH
R5+0/fLajxUrljN16pv897+v8M47bzJ27EU8+uijHDlyiJkzP+azzz7m3/++n88//xqAjRs3MG3a
dJ5//imef/4pXnxxGmFhDt577x0uvngimzdvYuzYixgyZBhXXTWR+fO/oV+/s0r93J98MosNG9Yx
c+bHfPvt/3jmmcd5++0PeOmlZ7n55ikMHDiI1157mR07tpOc3KUa34QENkKIeujHH5fQpUs34uLi
GTDgHJYt+4EpU25ny5ZNFBYWMnToCJo2bcqiRT8BsHnzRiwWC+Hh4WVuMy4ujkOH/uT22yeTl5dH
Xl5umctu2/Y7AIMGDaVp06bFXfEOhwOHw84LLzxT3Itz6NAhwsLCAIiIiKjUfoQQQtQtZ589kKio
aD7++EP69z+HnJwcwGi3unXrjlLJKJVMTEwMa9euJicnm1NPbUW3bil065bCxImXlbnt8tqP5ORu
tG/fgZ49Ty/umfn111+55JIraN68OaNGXcCsWe/x++/GnJgWLVqgVDLJyV04cGA/PXr0ZPPmjfzw
w2IA4uPjef/9mcyc+TZ5eXkcPnyozHKtXbuajIyDTJp0BU6nk9zcXAoLC+nYsTPvvvsWWm9h5Mjz
qx3UgAQ2QoggevjhAr/uYgWS0+lk+fKfyM7OZsCAPsWvb9++DbfbY/7L+H9WVhaNGoWdsL7FYgHA
7XZRWFhY/Ponn3zExo0bmDr1DX7+eRmvvz7Vj9J4issEsHLlb3z++Sc8+uiTxMTEcuutN+PxeE5Y
o2r7EUII4Y/aaJd8ORxhWK02AOx2OzabMStk27ZUlEouXs7t9mC1WnG7PXibCbfbTVZWFlFRUdjt
J1/Cl9d+hIU5ALDZrMXtjre9A4pfs1qtxeU0/m0r3pd33YKCfJ555gkmTLiMCRMuZdKkq05qy0p+
5q5dU3j44ceKX7Pb7Tz33MssXryIFSt+5Z57bufBBx+p9ggFmWMjRAjKyYHt2y2sXGllyRIb2dm1
XaK6Y9WqFWRnZ/PYY8/wzjsfMH36+0RGRrJ06RK6dOmKw+Fg/vxvSU3VjBkznOXLf8Zms3H06FEy
Mg4SH98UgA0b1vH99wuKT/y5ubnYbFbCw8NZufI3gDLvUHl7aBYs+I6NGzewY0da8TYAoqNP4Zdf
lmGz2Thy5DA2m9HIbd++rVL7EUKImnD4MCxfbuPQIUvFC4squeGGm9m0aQOpqZrvv19IVtZR+vTp
R/fuPdi7dw8bNqxj7tw5jBs3kqyso6Vuo7Ltx5lnnsmSJYs4ePAAX3/9JTExMXTqpCosa0FBIS6X
i6ioKLZs2UROTjZZWUfLTNSTktKd7du3kZ2dzeLFC3nrrf+Sl5fLAw/cS6tWbbj11jtISupEevou
P45U+SSwESLErF9vpWfPKM48M4rzzotk4sQI+vaN5PXXHeTn13bpQt/SpYtp1aoNgwYNoVMnhVLJ
DBhwDj/++AMJCYncc8/9fPrpR9x221+5+OKJnHPOEPr06YfNZmPKlJvo3bsPZ5xxFg8/fD/p6buI
ijLGMV9wwVgaNQpn8uQbGD9+IomJzXj22SdLLUObNm25/PKrePvtN5g+/b90794DgDPOOJPu3U/j
vvvuIjY2nrPO6s+zzz5JSsppxMfHM3nyjZx//hi/9yOEEME0Ywb06BFJcnI0Y8ZE0K9fJO+/76Cc
m/Oiilq3bsuoURdw++2TmTr1Bf7+97tISenO4MF/4eKLL+Hee+9gxozp3Hffv4iLiy91G5VppwDu
v/9+4uObcsUVE1i58jceeeRJIiIiKizrKaecwoUXTuD9999l8eKFTJp0M1999QXZZdyFveiiifTr
dza33HI9X3zxGcOHjyIyMork5K7ce+/tjB9/AU2axDBu3Hj/DlY5LOV1HdWkjIxjoVEQU0JCNBkZ
x2q7GHWOHLeq8R633MP5nH9+BJvSIpkwoYjERA8uF3zwgYNjxyyceqqbN97Io2/f8tMXNxRS36qm
vOOWkBBdJ2/JKqVeBq4CDgLXaa1/9nmvFTAbOAtor7XeqZSyAW8CFwOZwN1a69nl7aO22qlQr+eh
XL5QLhuEdvkOHbLQp08UHo+Hs85y0batm9mzHWRnWxg40Mmrr+bTvHntXrqF8vEDKV91lVW+8top
mWMjRCjYu5fIJ54h8o13mFsYy7sT5jDl1Q7Fb99+ewEvv9yI1193cP31jVm0KJfExJC6FyBErVFK
DQOmAGcCNwOvAT19FlkGbCux2lXAJcDpwLXA20qpz7XWzqAXWIg6YNo0Bzk58NhjBdx4YxEAt91W
yD33hDN/vp0LLohg9uxcOnSQtqimvfLK83z99Vcnvf7mmzNp3bpNLZQodEhgI0RtcrmI+ufd8P4M
IoqKOEQc7dnJQ98NJuuXWRSd1R+AuDhjwmPTpm4eeSScyZPD+fjjPMypGUI0dIOB3Vrr35RSrYHr
lVJxWuvD5vuXAc2AoT7rfAP00FpvU0rtBCKBaOBIjZVaiBB16JCF6dPDaNECrryyqPj1li09vPde
Hs89F8bTTzdi9OgIPv44j5QUGUVQk6699kYuueSKk14va4haQyKBjRC1qPH012n8zlu4kzpx18G7
eDPvKn696wO6PDeZJhPGcuyV/1Jw4fExp5MnF/Hrr3a++87OCy+EcdddheVsXYgGoxngnU3rDUya
A4cBtNa/KKXG+a6gtT4AHFBKxQP3Amu11uUGNbGxEdjttXM3ISHh5GdWhJJQLl8olw1Cs3wvvIDZ
WwNt2pxcvqeegtat4dZbrVx8cSSrVkH79rVQUELz+PkKRvkCuc36dvwksBGilljTdxH5+CO44+L4
+LafeOHvCfzjHwUk3HEJR/s255RrryB68o0Und4Xd5u2xjpWePnlPIYNi+SZZ8IYONBFv36uWv4k
QtRNSqlo4FsgAZhQ0fJHjtTOM4Xq6jj4UBDKZYPQLN+hQxZefjmSxEQPN91kLbN8l1wC+fkO7r47
nPHjXXz1VS5hYaUuGjShePx8Sfmqp5w5NmWuI1nRhKgNHg/Rd9+OJTeX7Eee4O25CQBcdpnR5V80
cBDZjz+NxeWi8Yy3T1g1NhZeeCEfj8fC7Nlyb0IIYB8QY/7d1Pz/3vJWUEpZgA+ATsAwrfXK4BVP
iLrjyy/t5ORYmDy5kMaNy1/26quLGD++iNWrbTz+eKOaKaAQ5ZDARoha0OiTjwhbvIjCIUPZNfAy
Fi2Cvn1dtGt3fBJmwdiLcMfFEf7hTErmee7f30VsrIfFi+2SdlMIWAi0VkqdCVwArAAKlFLhAEqp
jhhD0wDaKqUSgYuA0cBNwEalVJSZKU2IBu2334yfwfDhFefRsFjg6afzSUpy89prYSxYID8hUbsk
sBGihlkOHSLqwf/DExHJsWde5Is5xjMBxo8vOnHB8HDyL78a66FDNJo754S3bDY45xwne/ZYSUur
k9l5g+rDD2cyfvxo/vKX/lxxxXh++GExANOnv87IkYOrvf3HHnuYa6+9vNxlvvjiU44d86+Lf9++
vQwY0IelS5eUuczq1SsZMKAPqam6zGU2blzP6tUNr+NBa70UeB6YB/QGJmMkB/jIXCQVmGb+vQR4
GiMAAvgYOGb+N7BmSixE6Fq50kZsrIekJP/umkVFwZtv5uFweHjwwXDKeEajEDXCr3EslX0+QEXr
CNGQNX7vHaxHjpD9r0dxt2nLp586sNthzJiT747lXXM9jV99icZvv0nBhEtPeG/wYBdffulgyRI7
HTsWnbRuQ7V580Zee+1lnnnmRZKTuzF16gs888xjnH32AK6++nouv/zqoJchOzubF198hjPPPJvo
6JqbmPnRRx/Qvn0HevfuU2P7DBVa6zuBO31eGuzzXlnR/3XBLJMQdc2BAxbS060MH+7EUol7Zikp
biZMKOLDD8P47js7o0ZJ1nRROyrssfF5PsAIjGcBvFZikWVAbiXXEaJhcrkIn/kOnohI8q+5Dq2t
bNhgY9QoiI8/+e6Yu207CocNx7FqBfb1a094b9Ago+FYskTm2fjav38/ABaLldjYWO699wG++mo+
DoeDmTPf5sILRwEwZcpNPPTQfdx449WMHDmE779fyM03X8d55w0t7uEZP340L730HFB2b8/8+d8w
fvxozj13IP/+9wO43W6uvfYyXC4XEyaMYd++vXz77ddcdNH5jB49nBkzpgOQmZnJ5Mk3cO655/DB
BzNK/Sx79uzmmmsuZeTIIcyf/43PZ9zH5Mk3MHRof666aiJpaduYPv11lixZxDvvvMn06a+zYsVy
Lr/8YoYO7c8dd0whN7d2Jr4LIeqOFSuMoWR9+1Y+Kc0ttxg32KZNcwS0TEJUhj9D0QZjPh8Ao5u/
h1Iqzuf9y4CplVxHiAYpbNF8bHt2k3/xRDzRp/DZZ0ZQcsXJ6eiL5V93AwDh77x1wuutWnno1MnF
smU2CkN3bZBkAAAgAElEQVQ063Pkww8Qd3pKQP+LfPiBcvfZq9fpxMbGcdddtzFhwlhefvl5/vhj
T6nLrlmzmgceeITIyEiefvox7r33AVq1as1HH73n92fUegvXX38Tr7/+DgsWfMuKFb9y993/BOC9
92ZjsVh46qn/8Le//Z2XXnqNGTPeZtu2VGbP/pAdO7YzY8YsYmJiS93222+/QUFBIR988Alun/Ed
W7ZsIjm5C5988hVNmsQwc+bbXH319TRr1pyrrrqOq6++ns2bNzF27EXMmvU5mzZtOCEwEkKI0ngD
mz59Kh/YJCe7GTrUyfLldlavlpkOonb4c6u30s8HqGid0tTm8wHKEuq5vUOVHLdyzJoJQON/3Eqj
+GjmzIHoaBg9GiIiyjhul1wE97en8eef0PiVF420aKZRo+Dll2HbtmgGDaqJD1BJEWFgDewcoIiI
MCJ86ljJ+paQEM28eV8zZ84cli5dyty5X/D99/OZP38+kZGNsFgsJCREExZmp1u3rvTp052uXbuQ
mZlJv3496d27J0uWLCEhIRqbzUrjxg4SEqJPWDc83IHdbiUhIZoWLRKZMeMtcnJyACgqyqFly5YA
tGwZz/r16ykqKuKFF54GwOksIj09lfT07fTocRo9eiQTEWHj3XffokmTxid8nh07ttG//1kkJ7dn
7NgLmDdvLrGxkUREtGf27A+45ppLycnJoWfPnrRsGYfdbqNJk0hatoyjbdtTeeutt3jvvXfIy8uj
oCD7hG3L71QIUdLKlTZsNg89e1btMQKTJxeyaJGdadPCePPN/IpXECLAQmYMS209H6AsoZ7bO1TJ
cSubNX0XcfPm4Ty9D5mtOrLyuxx27oxk4sQiIiIc5R63iMuuIvLxR8j66DMKxl9S/Hq/fjYggjlz
CujaNQS7be75l/FfoJnHqrT6lpOTzaFDhxg9egKjR09g2bKl/N//3cEvv6wkJ6cAj8dDRsYxCgud
NGrUmIyMYzidbjweCxkZxygocOF0usjIOIbb7SEnJ5+MjGNkZmYXr5ufX4TT6WbNms28+OKL3Hbb
HfTvfw6XXDKOrKw8IiKM89nhwznk5xsXCM8++3LxU6GjoqL59tv5FBUVkZFxjIwM4z7Q0aN5J3we
p9NFbm4hGRnHOHTIeP3IkRyef/5pbDYH//3vO7zyyvNkZ2eTkXEMl8tNTk4Be/Zk8NBDDzFhwmVM
mHApkyZdRXZ2fvG2y/udSsAjRMNUUADr1llJSXETGVm1bQwY4CIlxcXcuXZ27bLQtq2k7RQ1y5++
wko/H6CK6whRrzV+710sHg9510wC4OuvjXHIo0dXPPG/cPBfAHD88tMJr591lguHwyPzbHzMnj2L
G264mtWrV5KVdZQ//tiNzWajVas2ld5WfHxTtm7dwtGjmfz668n5T3JzjV6aqKholi37AYfDQWbm
EaxW49S6c+cOlOqC3W5n9eqVHD2ayeOP/5sDB/aTlNSJzZs3snPnDr79dl6p+09K6sTKlb+xf/8+
Fi78zme/uYSFNaKgIJ+tW7eQk5NNYWEhNpuNvXv3kJWVhcvlIioqii1bNpGTk01W1lFcLnmYqxCi
dOvXWykstFRpfo2XxQI33VSI223h889lro2oef4ENlV5PsBJ62itMwNeeiHqisJCwj+YiTsmhoKx
F+HxwNdf24mM9DBoUMWNiDPlNNzRp+D46ccTXo+KgjPOcLFunZVDhyTtM8CVV17LqFHn8/DD9zNu
3HnMnfslDzzwb1q0aFmFbV3DH3/s5pZbrqdHj14nvd+xY2cGDhzE888/xcGDBxg79iKmT3+d5s1b
0qpVG/71r/vIy8vjrrvu49NPP+bWW2+hUydF+/YdmDDhUtq0actNN11LWBmP677++htxOOxMmnQl
zZo1L379ssuuZNOm9fznPw9x2213kp6+izlzPmPgwMF8//1C5s6dw4UXTuD9999l8eKFTJp0M199
9QXbtqVW+hgIIRqG6iQO8DVihBObzcOCBXLDTdQ8i8ePp/sppZ7DSIu5F7gWeBbI1FqPU0qV3MAM
rfW1Jdep6KnOGRnHQqq/UoZUVY0ct9KFffUFTW64htyb/0bOo0+waZOVIUMiGTeuiDfeyPfruJ1y
xQQaLfiOQ+u24va5SH/ppTAee6wRb7yRx7hxDSvFptS3qqlgKJpEyGWorXYq1Ot5KJcvlMsGoVW+
664L5+uvHaxalU3r1kZVr2r5xoxpzK+/2ti8OafUjJ+BEkrHrzRSvuopq3zltVN+hdNVeT5AKesI
0WCFf/kFAPmXXwXA//5n/PTOP9//QKTo7IE0WvAdjp+XUXDxxOLXe/c27q5t3SpZaIQQQlSex2P0
2DRv7qZVq+oHIsOGuVi+3M6iRTYmTmxYN9xE7ZIrISGCLT+fsEULcHZIwpXcBYB58+w0auRh6NBK
BDb9BwDg+HnZCa+3b2+kAd65U37OQgghKu/gQQsHD1rp1ctVqQdzluXcc422beFCGY4mapZcCQkR
ZGE/LsGSm0PhyPPBYiEtzcKWLTaGDHESFeX/dsqaZ9OihYewMA87dsjPWQghROVt22a0H507uytY
0j/JyW5at3azeLGdoorz4wgRMHIlJESQhX3zNQAFoy4AjmdDO++8SnbP2+0UnXkW9u1pWPcdTzJo
s0Hbtm4JbIQQQlSJN7BJSgpMYGOxwLBhTo4etRQnJRCiJsiVkBDB5HLR6Nt5uJsm4OzTFzCyodls
HkaMqPy446KzBwKlDUfzkJlp4ciR0tYSQgghyuYNbDp2DExgA8eHo0l2NFGTJLARIojsq1Zi/TOD
gpHngc3Gzp0W1qyx0b+/i9jYym9P5tkIIYQItLS0wAc2/fu7aNzYw8KF0mMjao5cBQkRRI2++R8A
haPOB+Cjj4xhaBMmVG3QcVnzbNq1MxojGY4mhBCislJTrTRt6iYmpuJl/dW4sRHcaG3jwAHJIi9q
hlwFCREsHg9h8+biiYikcOBg3G6YPdtBVJSHCy6oYvrLMubZeHtsJLARQghRGQUFsHu3JaC9NV59
+hiPI1izRtomUTOkpgkRJLbfNfYd2ykcei6Eh/Pjjzb27LEydmwRkZFV327xPBufXhvpsRFCCFEV
O3ZYcbuDE9j07OkNbGQ4mqgZchUkRJB4h6EVmMPQZs0yhqFdemn1HlZWdEY/AOzr1hS/1rq1B5vN
w86d0t0vhBDCf6mpgZ9f49WrlxHYrF4tgY2oGRLYCBEkju8X4rFaKRw2nKNHjYdyJiW5OeMMV7W2
6+zSDY/Fgn3TxuP7ckCrVvIsGyGEEJUTjMQBXrGxxlDptWtteDwB37wQJ5GrICGCITcXx+qVOLv3
wBMTyxdfOMjPt3DZZUXVf6pzVBSudu2xb1yPb0vRvr2bjAwr2dnV3L4QQogGIxipnn316uXi6FEL
O3bIiAIRfBLYCBEEjlUrsBQWUtTfmA8za5YDq9XDxImBeQSzK+U0rJmZWPf+UfyaJBAQQghRWdu2
WXE4PLRpE5wuld69ZTiaqDlyBSREEDh+WgoYz53ZtMnKmjU2hgxx0bx5YBoOZ7cUAOybNhS/Js+y
EUIIURkejxHYtG/vxh6k52h659lIAgFRE+QKSIggCPtpGR6rlaJ+Z/Hee0bSgKuuCkxvDYCzW3eA
E+bZSGY0IYQQlZGRYSEry0JSUnCGoQGkpLix2z3SYyNqhFwBCRFoubnYV6/EeVoPsm1N+OQTB82b
uxk+vHrZ0HwV99hs9O2xMXqDJDOaEEIIfwR7fg0YD+rs0sXNxo1WCguDthshAAlshAg4x8rfsBQV
UXT2QL76ys6xYxYuv7wooN387lNb4W4Sg81nKFrbtm4sFsmMJoQQwj/ewKZTp+AFNmAMRysosLB1
q7RPIrikhgkRYMXzawYMZObMMCwWD1dcEbhhaABYLDhTumPbsR1ycgAID4eWLT0yx0YIIYRfvIFN
MIeigSQQEDVHroCECDDv/Jp10f1ZtcrG0KEuWrcOfLYZZ7cULB4P9i2bil9r187NH39YycsL+O6E
EELUM8F8ho2vXr2M7UtgI4JNAhshAiknB/uaVTh79OTdz+OBwCYN8FWcQGDjyZnR0tPlpy2EEKJ8
u3ZZaNLEQ2xscPfTubObsDCPDEUTQSc1TIgAcqz4FUtREfn9BvLppw5atHBz7rmBSxrgy1Wc8tk3
M5okEBBCCFExj8e4Cda2bXB7awBsNmO4W2qq1fe50kIEnAQ2QgSQ4+dlAKxuMohjxyyMGeMM2rMB
nJ2T8djtJzzLpk0bo4HavVt+2kIIIcp28KCF/HxLjQQ2YCQoyMmxsG+f3HgTwSNXP0IEUNhPP+Kx
2ZiVPhCAUaOC01sDQHg4rk6dsW/eBG6jYfI+APTAAWk4hBBClM2baKamAhvvPJ7ff5dLTxE8UruE
CJTCQuzr1+LsmsKXi+OIjfVwxhmuoO7S2TUFS24Otp3bAWjWzGg49u+Xn7YQQoiy7dpl3ABr27Zm
xoZ17my0T95MbEIEg9QuIQLErrdgKSjgQOve7N9vZdiw4A1D8/ImELCZ82yaNZMeGyGEEBXbtcu4
BPQOYQ4277NypMdGBJPULiECxL52DQA/F/UFYOTIIA5DMzlTzMxo5jybiAho0sQjgY0QQohyeQOb
mhqKlpRkPERaemxEMEntEiJA7GtXA/Bx2hmEhXkYMqQGApuuZma0zZuLX2vWzC1D0YQQQpQrPd2C
1eqhVauaGYoWEQGtW3ukx0YEldQuIQLEvnYN7kbhfLX9NAYOdBEVFfx9ehIScMfEYEtLLX6tWTMP
R45YyM8P/v6FEELUTbt2WTn1VA9hYTW3z44d3Rw8aOXo0Zrbp2hYJLARIhDy87Fv2cS+xNNw4mDE
iOD31gBgseBK6oRtx3YoMh4E6s2MdvCgDEcTQghxsvx82LevZp5h48s7zyY1VS4/RXBIzRIiAOyb
N2JxOlnu7ANQc4EN4OrUGYvTiW3XTgCaN/dmRpPARgghxMm8zzqTwEbUN1KzhAgA+xpjfs28g305
7TQXLVrU3KOVnR07A2BL/R3wzYwmP28hhBAn86Z6btOm5toqOJ7yWQIbESxSs4QIAMc6IyPaL64z
6NcvuM+uKcnVyQxsthnzbLxD0aTHRgghRGlqOiOal/chnampthrdr2g4JLARIgDs69ZQGBaJRnH6
6TUc2HTsBIBtW8keGwlshBBCnKy2ApumTT3Exbmlx0YEjdQsIaorJweb3kpqVC/c2Go+sGnXHo/d
jr14KJp3jo38vIUQQpzMOxStbduaHYoGxjybnTstFBTU+K5FAyBXPkJUk33DeixuNz8V9qVpU3eN
j1nG4cDVrr3RY+PxFPfYyFA0IYQQpdm1y0pkpIf4+NoJbNxuCzt2yCWoCDypVUJUk2OdkThgcXZf
Tj/djaUW4glXx85YMzOxHDpE48YQE+ORoWhCCCFO4vEYgU3btn62V9nZNProA8I/mFn8WIHqkMxo
IpikVglRTd6MaCvpU+PD0Ly8CQTs5jyb5s3dkhVNCCHESQ4ftpCTY6FNm/Ln19g3rINJk2ia0olT
bvsr0f+YQszYUVh3p1dr/+3aGb1E3uFwQgSSXPkIUU32dWvIDWvCNjrSu3ftBDZObwIBc55NYqKH
zEwLeXm1UhwhhBAhyp/5Nfa1q4kZNRTefht3fDw5d99H/riLcKz8jdi/DCBs7pdV3n/r1kZA5X2W
jhCBJLVKiGqwZB/DnraNzY17Y7FAr1611GNTIrDxpnyW4WhCCCF8VZQRzXL4EKdMutoYdvbhhxxe
sZ7cu+/j2OvvcOyFqVgKC2gy6Soc3y+s0v4lsBHBJLVKiGqwbd0CwC85PUhOdhMdXTvlKA5s0rzP
sjEaDhmOJoQQwle5gY3bTfTfbsK2O53cO++Fyy4Dq9mOWCzkX3E1mXPmARD59GPGhJ1KatIEmjTx
sHu33HgTgSdXPUJUg90MbNY6U2ptfg2AJzYOd9OE4pTP0mMjhBCiNOnpRrtQWgbPiBefpdGiBRQO
/osR2JTC2et0Ci4Yi2P1KhyLq9Zr06qVm927rVWJi4QolwQ2QlSDbetmADaSQu/eNfugs5KcHTth
Td8F+fmS8lk0OEqpl5VSR5RSWil1don3WimlflZKeZRS7fxZR4j6yttj4x0S5mVft4aIpx7DdWor
sqZNB5utzG3kmEFP5DNPVKnXpnVrN7m5Fg4fljZKBJYENkJUg33rVgA207VWe2zAyIxmcbux7dju
85BOaTRE/aeUGgZMAUYAy4DXSiyyDMit5DpC1Evp6VYSE91ERJz4esSzT2LxeDj2wlQ88fHlbsPV
LYWC88fgWLUSx+JFlS6Dt7dIhqOJQJPARohqsG3dzB57W4iKonPn2u2xcXU0Uj7btqX6DEWTn7ho
EAYDu7XWvwHzgB5KqTif9y8DplZyHSHqHZcL/vjDctIwNNuG9TT67huK+vajaNAQv7ZVnV4bSSAg
gsVe2wUQoq6yHD6E7eAB1nI+KSmu8nrta4Srk5FAwL7td5oNl6FookFpBhw1/z5i/r85cBhAa/2L
UmpcZdYpTWxsBHZ77fzQExJqKTOJn0K5fKFcNqjZ8u3aBU4ndO5sO3G/r70AgOORh0lIPMW/8g05
G8aNwzFnDglrl8Pw4X6XIyXF+P+RI41JSKjURziJfL/VU9/KJ4GNEFVk18YwtI2k0KVL7fbWADiT
jqd8btQIYmM9kjxAiAA6ciS34oWCICEhmoyMY7Wyb3+EcvlCuWxQ8+VbvdoGRNCsWQEZGYWAkd0z
7rPPKOrZi8zeZ4NPeSoqn33y7cTOmUP+a69zrNdZfpfjlFOsQCRbthSSkVFQ1Y8j32811dXylRfs
SB+gEFVk22IkDthEN5Sq/cDG3aYtnrAwbNu8mdHc7N8vP3HRIOwDYsy/m5r/3xuEdYSo00rLiBbx
4jMA5N75f2Cp3M0wZ49euNq0Jez7hVBY6Pd6MhRNBIvUKCGqyK6NVM+h0mODzYarfQdsaWng8dCs
mYesLAu5tXOTWYiatBBorZQ6E7gAWAEUKKXCAZRSHTGGmQG0VUollraO1jqz5osuRM1JTz/xGTa2
bak0+uIzilJOo3D4yMpv0GKhYPhIrMeycPz6i9+rNWkC0dHyLBsReBLYCFFFtq1bcGFlK8koVbsZ
0bxc7ZOwHsvC8uefxSmfZTiaqO+01kuB5zGSAPQGJgPfAB+Zi6QC08y/lwBPl7GOEPWaN9VzmzZG
YNP4zWlYPB5y/3FXpXtrvArPNQKisPnf+L2OxWL02sizbESgyRwbIarC48G+dTM77UmcEteIuDhn
bZcIAFeHJABs29No3vxUwMiM1r59aAReQgSL1vpO4E6flwb7vFfqFVsp6whRr6WnW7HZPLRs6YGC
Ahp98SmuxGYUjrqgytssOnsA7sgoGn33DTmPPOF3gNS6tYfNmy1kZkJsbJV3L8QJpMdGiCqwHDyI
9cgR1jpTSE4OgWFopuLAZkdaccpnyYwmhBACYNcuC6ee6sFuN3pYrJmZFIy/BOzVuM/dqBFFQ4Zi
27kD27ZUv1eTeTYiGKQ2CVEF9q1G4oCNhGhgsz2NxEQjsMnIkMBGCCEaurw8OHjQWjy/JvyjDwDI
v+Tyam+7wJyfE/ad/8PRvIGNd96PEIEgtUmIKvAGNpvoFrKBTUKCEdgcPCiBjRBCNHTenpG2bd1Y
Dhwg7PuFFPXohatL12pvu3DocDwWS6Xm2bRubbRRe/ZIGyUCRwIbIarA5vMMm1BJHADgbt4CT+PG
Zo+NEXAdPCg/cyGEaOh8Uz2HfzYbi8tF/qXV760B8CQk4Dy9L47flmM5UuYzbk/gTWAgQ9FEIElt
EqIK7Fs2U2RxkEqnkOqxwWrF1a4Dth3bSUzwBjZyN0wIIRq64oxorV2Ef/whHoeDggvHB2z7hcNH
YnG7CVu0wK/lW7XyBjbSRonAkcBGiMryeLDpraRZO9OslZ3osh+AWytcHZKw5mQTnXuQiAiPBDZC
CCGKA5sU51rsWzZROHwUnrj4gG2/YPgowP+0z7GxEBnpkTk2IqCkNglRSdY/9mDNPsZaVwpKhVBv
jck7z8a+w0ggIIGNEEII71C05OXvA4FJGuDL1aUrrhYtCftpGf48nMZiMYaj7dkjl6IicKQ2CVFJ
dr0FgM10Da1haKYTM6O5+fNPC67QmQYkhBCiFqSnW4lo7CZm0RzcsbEUDj03sDuwWCjq2w9rxkGs
6bv8WuXUUz1kZVnIygpsUUTDJYGNEJVkS9sGwFaSQypxgFfJlM8ul4XDh6XXRgghGrL0dCsjm63E
tn8fhcNGgMMR8H04T+8LgGPlb34t36KFcXNw/365HBWB4VdNUkq9rJQ6opTSSqmzS7w3QimVppQ6
rJR61HwtTCn1vlIqSym1Tyk1JRiFF6I2eB9A9jud6dIl1HtsJOWzEEI0dJmZkJVlYZz1fwAUjBgV
lP0U9TECG/uqFX4tLw+SFoFWYWCjlBoGTAFGAMuA13zeswBvAV8CE4EHlFI9gfHAOKA38A7wolIq
KuClF6IW2NLSANhGRzp1Cr3Axp3YDHdklAQ2QgghgOOJAwZmfY3Hbqdo8F+Csh9n9x54HA6/e2y8
gc2+fdJGicDwp8dmMLBba/0bMA/ooZSKM99LAloBc7XWC4FsYAiQB7iAA8BBIN/8txB1ni0tlT3W
1jRtG0FERG2XphQWC672HbDtlJTPQgghYOdOKy3YS7s/V1N01gA8pzQJzo7Cw3Ge1gP7xg2Ql1fh
4t6haAcOyFA0ERh2P5ZpBhw1/z5i/r85cNh8jxLvtwBeBJYAf5r7uFlrXW4Nj42NwG63+V3wmpCQ
EGJ5fOuIen3ccnJg7x9sZSjdulkD+lkDety6KNi4nu7xh4FTyc1tTEJC4DYfSup1fQsiOW5CNBy7
dlm5AGMYWuGIkUHdV9HpfXGsWol93VqcZ55V7rLNmkmPjQgsfwKbqrgYGGj+dyHwvFLqS611Rlkr
HDmSG6SiVE1CQjQZGcdquxh1Tn0/brYN64kDNIrWrQvJyCgIyHYDfdwiTm1LJBCTsR44le3bA1fW
UFLf61uwlHfcJOARov7ZtcvCBOYCx583EyzOPmfAG9NwrFpRYWAjc2xEoPnT97cPiDH/bmr+f6/P
ewAx5nybePO9ocAGc/jabCAa6BWQEgtRi+xpRuIAjSIpKfTm13h5Ewg0yzIyuGVkSKMhhBAN1b60
fIaxkMJOybjbtQ/qvooqkRktPt6Dw+GRrGgiYPypSQuB1kqpM4ELgBVAgVIqXGu9HdgOjAFGARHA
AmAb0EUp1QE4F/CYrwlRp/lmROvYMYQDm/ZGYBOTYSQ6kDk2QgjRcLX+fTGNycc5Mri9NQDuVq1x
NWuOfeVvFT6o02o1hqNJj40IlAoDG631UuB5jMQBvYHJwDfAR+YiN2IEPDOA+7XWm4BpwCJgDfB3
4B9mECREneZ9hk1d6bEJ25VGXJxbAhshhGigiorgrENmmucgD0MDwGLB2ecMbAf2Y/1jT4WLN2/u
4cABC+7QbVJFHeLXHBut9Z3AnT4vDfZ573ugY4nlc4HLAlA+IUKKLS2VAksj/gxvTfPmFWd8qS2e
pk1xR5+CbYeR8lm6+YUQomHasxvO93xNVlg8TvM5M8FWdHpfGn39FY5VKyho1brcZZs3d+N02vjz
T0vxIwqEqCq52hHCXx4PtrQ0ttGR9h0tWEK5E8RiwdUhCdvOHSQ2dZGZaaGg/uUOEEIIUYHDP/9O
S/aR1mEo2Gom+2xRnzMAjOFoFfAmEDhwIJQbVVFXSGAjhJ8sBw9iPZbFVo8K6fk1Xq4OHbDk59Ml
ejcgCQSEEKIhsi37GYDMngNrbJ/OHj3x2O1+JRCQzGgikCSwEcJP3oxov9M5pOfXeHkTCHSxG+WW
eTZCCNHwxG34EQDPOQNqbqeNG+NM6Y59/ToqGi7QvLnRnu7bJ5ekovqkFgnhp7qSOMDLm0AgyS2B
jRBCNEgeD+3Sl7GfZiQOSKrRXTt79sZSVIRdbyl3uRYtpMdGBI4ENkL4qa6kevbyBjat8oyA7OBB
+bkLIURDYt2xnfiCffxkPYfEZjW7b2e37gDYNm0sdzkZiiYCSa50hPCTzefhnB061J3AJvGoN7CR
RkMIIRoSx88/AbCp6cAaT3jjTDECG/vG9eUu5x2KJtk7RSBILRLCT7a0bRy2xuNoFkt0dG2XpmKe
uHjcMTHEZEhgI4QQDdIPywD4I6kG59eYnMld8Vgs2CvosYmOhshID/v2SRslqk8CGyH8UVSEbddO
trrrxjA0L1eHJML37cSKSwIbIYRoYBzLf+YQcdCtS83vPDISV1JH7Bs3gKf859N4H9IpRHVJYCOE
H2zpO7E4nXVmGJqXq30S1qJCOth2yRwbIYRoQKy702l8IJ2lnEObdrVTBme37lizjmLds7vc5Vq0
cPPnn1YKC2uoYKLekisdIfxg23Y8I1pd67EB6NPkd+mxEUKIBsTxizG/5gcG0bZt7bRbx+fZbCh3
uWbN5CGdIjAksBHCD95Uz3XlGTZe3sDmtMapZGRYKhoNIIQQop7wBjZLOYe2bWvn5O/qlgKAfVP5
gY1kRhOBIoGNEH7wBjapdKqTPTbKlkpenoXs7FoukBBCiBrh+HkZx2xNWEcP2rSprR6b04CKe2xa
tJDMaCIwpAYJ4QfbjjQAdtqSaNOm7nR7eAObDk55SKcQQjQU1v37sO/Yzm+O/iQ0sxARUTvlcDdr
jjs+XnpsRI2RwEYIP9i2p7HH0ppm7cKx22u7NP7zNInBHR9Py1x5SKcQQjQU9t+WA7CwYGCtza8B
wGLB2e00bLt2YjmWVeZix59lI4GNqB65yhGiIrm52Pb+gfbUrWFoXq72ScRn7cSGUxoNIYRoABxr
1wDwi+fMWptf4+U059nYNm0qcxlvj82+fXJZKqpHapAQFbDt2A4Y82vat6+DgU2HJGxuJ+3YKYGN
EIBbwREAACAASURBVEI0APZ1RmCzmt6122ODT2a0TevLXEayoolAkcBGiArYthvza+paRjQv7zyb
TqTK3TAhhKjv3G7s69ZyKKEzxzil9gObbt7AZmOZyzRqBDExHjIyJLAR1SNXOUJUwJs4IJVOdT6w
kR4bIYSo32w7t2PNOsr22N4AtT4UzdWpM56wMOwby+6xAUhMdEuCG1FtEtgIUQFvj00qnejQoe4G
Np35XQIbIYSo5+xrVgOwztEHgHbtarndcjhwqi7Yt24Bp7PMxRISPBw+bKWoqAbLJuodCWyEqIA9
bRsurOxv3L54gmNd4g1suobJUDQhhKjv7GbigB/z+xIe7iExsfbbLWdKdyz5+cXPhCuNt5x//ik3
4ETVyVWOEBWwbk8j3dKWVh3sWOvgL8YTFY07IZFObGP/fgue2m/jhBBCBIl93Ro8VisLMnrTpo07
JNotl5kZrbzn2XgDGxmOJqojBKq7EKHLciwLW8ZBtKdznRyG5uXqkETLwp24C4rIzKzt0gghhAgK
lwvH+nUUdkxmX1ZUrc+v8XJ26QaAbeuWMpdJSJDARlSfBDZClMM31XNdTBzg5eyQhA037dkhw9GE
EKKesqX+jiU3h0PtvIkDQqPdciZ3BcC+dXOZyyQmGmWVB0mL6pDaI0Q56nriAC9JICCEEPWffa2R
OGBn09AKbDwJCbibJmDfUl5gIz02ovoksBGiHN6JjnU+sEnqBBiBjfTYCCFE/eQwH8y5vlFfIHQC
GwBnl67Ydu2E7OxS35ehaCIQ5ApHiHL49tgkJYXGWOWqcCV1BEChpcdGCCHqKfvaNXjsdlYUnAZA
u3ah0245k7sAYP99a6nvS4+NCAQJbIQoh217GkXYyWzSlri40GkgKsvVvgMei8XssZFGQwgh6p2i
IuybNuDs0o1teyIAaNMmdHpsXMXzbEpPINC0qQer1UNGhrRRouoksBGiHLb/Z+++g+s673Pff1dB
JUiCBSAJgiQqFxq7CtWLZcuyZMVVdlzm2kns5Hqck9xxbnKvy/jMyWTOnHsd5xxPYse+PnF8nCiS
YiuWZUuWVSxLVGFvKFyoJAGCBAESLCBRdln3j7U3CBaA6GuX5zOjAbTX3hs/bm5i7We97/t729vo
oIx15SZGMv+uzc4mvHptbMRG/+xFRFKNdaQJY2iI8OYtHDtmUlgYJTc36KquCFf7wcYaZ52NZcGy
ZZ6aB8iM6N0jMg6j/yxm/1mak3x9TVy0soJVnOLiiYtBlyIiIrMsvr5meMMWurqMhGn1HBdxqoCb
dUbzNBVNZkTBRmQcqdIRLS6+zmbBiZaAKxERkdlmHzoAQPfKLUQiRkI1DgDwFi4ismbtuCM24DcQ
GBgwuHRpHguTlGIHXYBIohobbDYn8R42cfHOaCvONRMKVZOREXBBIrPIcZzvAJ8FTgOfd1337THH
Hga+CywB/sF13W84jpMJ/BPwOHAJ+BvXdf9+/isXmR12YwOeZeHa/maYiRZswG8gkPXySxhnzuAt
W3bd8XgDgd5egwULEmvESZKDRmxExhEPNs2sT+rNOeMiFX6wqaRFQ/2SUhzHeQj4MvAwsAM/xMSP
GcAPgeeAJ4CvO46zGfgY8CFgK/Aj4L87jpM3z6WLzI5oFKuxgUhFJR0n/YU1iRhsRhsIuDduIHBl
k06do2R6FGxExmG1p8YeNnFjWz6rM5qkmPuBTtd1dwEvAJscx1kaO1YOFAPPu677CjAAPAAMAhGg
B3+UZyj2/yJJx+w8jjlwkXBNLZ2d/u/3tWsTb8TjZg0ErrR81sdTmR5NRRMZh9XayqCRw9Cy1eTl
DQZdzoxFi1YTyshhfaiZAydNIPnDmkjMCuB87Pv+2NeVwNnYMa45vgr478DrQB/+ufCPXded8B/6
kiW52LY1e1VPQUHBwkB+7mQlcn2JXBvMUn1vtwOQfes2TtdnAbB5cy4FBTN/6ll9/e70Nw5deKyV
hTd43gr/+htDQzmTrj0t/n7nUKrVp2AjciOeh9XWSqNXSWxpSvIzTS6sqGB9VzMvnQq6GJHAfRS4
J/bfh4FvO47znOu6veM9oL//8nzVdpWCgoX09iZuN8NEri+Ra4PZqy/3nd0sAM6XVNL8bATbNsnM
HKB33Hfz/NY3amkRyy2L8L4DnLvB82ZnW0AubW3D9PaOzH99s0z1zcx49U0UdjTWJ3ID5sluzMuX
cHFSYn1N3PC6SvK4xGBrd9CliMymk0B+7Pvlsa/dY44B5MfW2yyLHXsPcDg2fe0ZYCGwZX7KFZld
dmMDAOGaOjo7DYqKPOxEvHSdnU2krBzrSBN410+VKyiIT0XTdGmZHgUbkRuwWv2WyKkWbAynHACr
rS3gSkRm1SvAGsdxtgOPAbuBYcdxsl3XbQfa8bufPQLkAi8DrUC14zhlwHsBL3abSNKxGuuJ5udz
eUkRPT0ma9cm7nkrXF2LeeE85snrL7DFmwf09irYyPQo2IjcQKoGm6yN/gTmvBPNAVciMntc130D
+DZ+44CtwJeAF4GnYnf5An7g+THwNdd1G4DvAa8C+4E/A/6PWAgSSS6XLmG1txGuqaPrhP+xLpGD
TaSqGgDrBht15udDRoan5gEybYk4UCkSOKvtSrD5UnnidZaZLqPKXzC0tE+bdEpqcV33K8BXxtx0
/5hjrwEV19z/MvD781KcyByy3SYMzyNcU8vx434gWLMmcc9b4XjL58ZGQg++96pjhuF3RtNUNJku
RWKRG7BjIzYtxvqE3AtguuItn4sGFGxERFJBfH1NpHYDnZ3xYJO4561ItT9iYzc13PB4PNjcYAmO
yE0p2IjcgNXWyilzFUvWLSQzM+hqZo+3OJ/+jELKI80MDARdjYiIzJTVWA8QG7FJ3D1s4iIlZXjZ
2VjukRseLyz0GBkxOH/+hodFJqRgI3KtwUHMzuM0RVNrfU3c6fxKSung1LFQ0KWIiMgM2Y0NeIZB
2KkeHbFJ5DU2WBbh9VXYzUcgcv2euAUF8QYC+ogqU6d3jcg1rPY2DM9LucYBcedWVmIR5cL+jqBL
ERGRmfA87MZ6ImXlkJtLZ6dJRobHihWJO2IDfgMBY2gI6+j1/ToKC9XyWaZPwUbkGmMbB5SVpV6w
CZX662xG6tXZVkQkmZndJzDPnSNSUwfAsWMGxcUelhVwYTcRbyBgNTVddyy+l01Pj4KNTJ2Cjcg1
7BRt9Rxn1/id0cxmNRAQEUlm9pj1NZcvQ1+fmdCNA+LCNbHOaDdo+RwfsdFeNjIdCjYi10jVPWzi
FmzzR2xyOxVsRESSmRXriBau3UBXVxKsr4mJxFs+N10fbOIjNgo2Mh0KNiLXsNpaGDEy6cleR1FR
Ys9Tno5lt5YQwmb5GTfoUkREZAbsJOuIFhddVUR00eIbbtJZWOgHM23SKdOhd43IWJ6H1dpKKxWs
KzMwU/BfSEZuBh12JWsuuWijABGR5GU3NhDNW0h0zdoxm3Mm/ogNhkGkugarvQ2Ghq46pOYBMhMp
+LFNZPqM06cxL16gyatKyWlocd2LHPK9c4S7e4MuRUREpmN4GKu1hUhVNRhGUmzOOVa4qgYjEhmd
/h2Xlwe5uZ6mosm0KNiIjGG3pfb6mrj+wvUAnHtX62xERJKR1dqCEYkQrq4FGJ2Ktm5dcozEh6uq
AbCbGq47VlDgacRGpkXBRmQMq6UZSN1Wz3HDpX6wGdyvYCMikozigSBc7QeEzk6TrCxvdPF9ootU
xzuj3bjlc1+fQTR1T8MyRxRsRMZI9Y5ocWas5TNHmoMtREREpiUeCCKxEZvOTn8Pm2RZGxofsRmv
gUAkYnD2rEZtZGqS5O0vMj+sNJmKlrvFDzY5xxVsRESSkRUfsamqYWAAzpxJjj1s4ryly4isWHnD
ls/ay0amS8FGZAy7pZkzZgHk57N0adDVzJ1VVQvpZhXLTivYiIgkI/tIE5HCFXjLlnHiRHI1DoiL
VFVjdXViXLxw1e3x6XRaZyNTpWAjEnf5MubxYxz2alN6tAagqMjDpYrll4/B5ctBlyMiIlNgXLyA
1Xl8dJ3KiRN+AFi9OjnW18SFYxt1Wtess1HLZ5kuBRuRGLvFxfA8Dnt1Kd04AMC2oXOBg4mH1dYa
dDkiIjIF8SAQDwZdXf7HueLi5Dp3hWv89UHXNhCIj9hoKppMlYKNSIwVm+fbQG3KBxuAM7GWz16T
pqOJiCST+LqUeDDo6vIDQHFxco3YROINBK5p+VxY6J+DT5/Wx1SZGr1jRGJs9wjgB5tUn4oGMLjW
8b+q5bOISFKJdxKLB4P4iM3q1cl17gqvr8IzjOtGbNQ8QKbLnsydHMf5DvBZ4DTwedd13x5z7GHg
u8AS4B9c1/1G7PY/A74JhIA/d13332a5dpFZZbn+L9Z0GbGJOuvhd+A1KdiIiCQTu6kRzzAIr68C
/DU2huFRVJRcIzYsWEB0XQl2Yz14Hhh+kFHzAJmum47YOI7zEPBl4GFgB36IiR8zgB8CzwFPAF93
HGez4zh1wN8BnwZ+APxp7L4iCcs+0kRf5ir6WZoWwWZxzSoGWEDWUU1FExFJGp6H3dRAdF0JLFgA
+CM2K1d6ZGQEW9p0hGvqMM+exTzdM3pbTg4sXOgp2MiUTWYq2v1Ap+u6u4AXgE2O48Qb4ZYDxcDz
ruu+AgwADwCPAR2u677ouu43XNe903XdJLuMIOnEGLiI1dVJk1lDYWGUvLygK5p7a9YZuDgs6WlG
2zuLiCQH4/RpzLNnCcc25oxEoLvbSLqOaHHxdUJWQ/1VtxcUeJqKJlM2maloK4Dzse/7Y19XAmdj
x7jm+CpgETDsOM4vgSrgb13X/d5EP2TJklxs25pC6XOvoGBh0CUkpaR83dr9+cr7hupwbjUD+TPM
98/csgV2UMW2yD4KBvuhpGRef/5sScr3WwLQ6yaSnOzY+ppwtb++pqfHIBIxkm4Pm7hwTR0AdkM9
oQcfGr29sDBKR4dFOOx38hSZjLl6q3jAWuAPgI8A33Ec51nXdXvGe0B/f2LtpVFQsJDe3otBl5F0
kvV1y35nDwuBempZu3aE3t7hef35QbxumZnQbDjgwbmd+wgtWDavP382JOv7LWgTvW4KPCKJzY51
EIvERmw6O5OzcUBcuDYWbBqvHrEpLPTwPIMzZwxWrEjO0SiZf5OZinYSyI99vzz2tXvMMYD82Bqa
ZbFjJ/Gnor0L/Aw/QK2blYpF5kB8T4B66igtTY9foLYNp5f5ndHsFq2zERFJBvGtCeJ72CTr5pxx
0XUleLkLsBuvbvmsBgIyHZMJNq8AaxzH2Y6/dmY3/jSzbNd124F24HHgESAXeBl4HnAcx7k9dvsQ
oF0AJWHZsY5ojdSkRavnuEvF/l42HFGwERFJBvaRRrzMTCJl5cCVVs/JOhUN0yRcXYPV4sLIyOjN
avks03HTYOO67hvAt/EbB2wFvgS8CDwVu8sX8APPj4Gvua7b4LrufuCr+N3S/gj4Y9d1z85++SKz
wzrSxJncYi6wOC06oo2qrCCKQbRRLZ9FRBJeNIrtHiFSsZ54C7T45pzJOmID/jobIxzGGjN7QCM2
Mh2TWmPjuu5XgK+Muen+McdeAypu8JhvAd+aYX0ic844fw7r1Ela89+HMehRUpI+wWZVaSYdlFLU
3sz8rioSEZGpMo92YFy+TLi6ZvS2Eyf8a9TFxcl77op3RrMb64nE1twUFvp/ntOntZe8TJ7eLZL2
rCNHANgfqmP1ao+cnIALmkdlZVGOUEXO+dMY5/pv/gAREQmMHWuJHK7dMHpbV5fBwoUeixcHVdXM
RUYbCFxZZ6OpaDIdCjaS9uKtM3deqqO0NHmveE1HPNgAWK2ajiYiksjshsPAlU5i4K+xSebRGmB0
BGpsZ7T4VDQFG5kKBRtJe1ascUADtWnVOAAUbEREkkn8g398xObCBbh4MXk354zzFucTWbP2qk06
ly9XsJGpU7CRtGe7/lS0RmrSq3EAsGgRnFrsd0ZTy2cRkcRmN9QTXV6AV1gIXOmIluwjNuCvs7FO
92D09gKQlQX5+Z6aB8iUKNhI2rObGjm7eB2XyEu7ERuA4VJ/LxujWcFGRCRRGRfOY3Uev2oaWnwP
m+Li5B6xgTENBJrGrrOJasRGpkTBRtKa0deH2dfL0QX+L9R0G7EBWOoso49l0KRgIyKSqOIL68c2
Dujs9D/GrV6d/OeuSE28gcCV6WiFhR5nz5pjt7cRmZCCjaS1+ELMg95GLMtj7drkv+o1VeXl/jqb
rBMdEAoFXY6IiNyAdYPGAak1YqPOaDJzCjaS1uKtM98a2MSaNV58v7O0Em8gYEbCWEc7gi5HRERu
4EatnlNhD5u4SGkZXnY21phgs2KFH2xOnVKwkclRsJG0Fh+xefPilrRr9RxXWjqmM5oaCIiIJCS7
4TBeRgaRyvWjt3V1GViWNxoAkpptE66qxnabIBwGYMUK/7zc06OPqzI5eqdIWrMb6olk5dBKhYIN
YLUq2IiIJJxIBPtIE5H1VYydWnDihMnKlR62HWBtsyhcU4cxPDy6/cDKlX5g6+nRiI1MjoKNpK+R
EawWl7NFtUSxKClJz2CTlwd9y2Itn5vdgKsREZFrWR3tGIODV62viUT8KVqp0DggLlznT7OLz6aI
j0Qp2MhkKdhI2rJamjFCIY7mbwRI2xEbgMz1axkmUy2fRUQSkD3aOODK+pqeHoNIJPk35xwrUuef
j+36eLCJT0VTsJHJUbCRtBU/UTTa/omitDR1Tg5Tta7cpIVKrJYW8NL3dRARSUTWaOOAKyM2XV3+
h/2iotT5nT26l039IeDKVLRTp/RxVSZH7xRJW/EOMzsHN2MYHmvXpu+ITWmpxxGqsC9dwDzdE3Q5
IiIyxuiITc2VYNPdnTod0eK8RYuJrCvx/7yeR14e5OZ6GrGRSVOwkbQVDzav9W1i9WqP7OyACwpQ
vOUzqDOaiEiisRvqiaxYibd8+eht8T1sUmnEBiBctxGzrw+z5xTgj9oo2MhkKdhIevI87MbDhIvX
4Z5aktbra0DBRkQkURn9Z7G6TxAZMw0Nruxhk0rNA2BMA4HYdLQVK6L09RnxDtAiE1KwkbRknD6N
2dfHuRL/F2i6dkSLKymJ4uIAavksIpJI7NiGlWMbB8CVEZtUah4A/ogNjG0g4OF5Br29GrWRm1Ow
kbQUn698Ylm8cUB6B5ucHLhYFGv5rBEbEZGEYR86CFwZyYjr7jbJzvZYujTVgo3/57Tq1fJZpk7B
RtJSfH3NkSz/ylBJSWqdGKajsHwBJyjCbGkJuhQREYmxD+4DILR561W3nzhhUFTkYaTY5/1o0Wqi
S5ZcNRUN/D17RG5GwUbSUnzEZk9oE6ARG/DX2bg4WN1dMDgYdDkiIgLYB/YTXZxPtKR09LbBQejr
M1NufQ0AhkG4bqO/KenAxdGWzz09+sgqN6d3iaQlu7Ge6II8dveVA1pjA1Be7gcbw/OwOtqDLkdk
ShzH+Y7jOP2O47iO49x5zbGHHcdpcxznrOM4fz3m9j+L3dbjOM7vz3/VIhMzLpzHbm8jvHEzY4dm
Tp5MzfU1ceHaDf65qLFRU9FkShRsJP0MDWG1NBOpqaXjmM2KFVEWLAi6qOBVVERpxl9nY7VpOpok
D8dxHgK+DDwM7AC+O+aYAfwQeA54Avi64zibHcepA/4O+DTwA+BPY/cVSRij62s2b7nq9nhHtKKi
1LwoN7YzmoKNTIWCjaQdu8XFiEQYrq6jq8vQNLSYsrIrwcZuaw24GpEpuR/odF13F/ACsMlxnKWx
Y+VAMfC867qvAAPAA8BjQIfrui+6rvsN13XvdF03NS9/S9KyD+wHIHRdsPE/5BcXp+ZbdrQzWsNh
Vq70z9GaiiaTYQddgMh8i3daOb1yI9GoQWlpap4YpmrtWo92ez2EwWrViI0klRXA+dj3/bGvK4Gz
sWNcc3wVsAgYdhznl0AV8Leu635voh+yZEkutm3NZt2TVlCwMJCfO1mJXF8i1wY3qe+If75a/OA9
MOZ+5875X2tqsikomNvdpQN5/e7cBpmZ5BxpoKxsITk50Ndn37CWpP77TQCpVp+CjaSdeOOA1gX+
FSGN2PhsGyhZy0hrBpZGbCT1ecBa4A+AjwDfcRznWdd1e8Z7QH//5fmq7SoFBQvp7b0YyM+ejESu
L5Frg5vXt3TnLoylSzmTuxTG3K+lJQvIZMGCS/T2zt05LMjXL7+qBvvwYfpO9VNYuJgTJ6C391LC
1DcZqm9mxqtvorCjcT1JO3ZDPZ5hcDCqPWyuVVJh0kY5ZmsreBrJkqRxEsiPfb889rV7zDGA/Nga
mmWxYyfxp6K9C/wM/0LfuvkpV+TmjHP9WMeOXtc4AK6ssUnJrmgx4boNGENDWG2trFwZpbfXIBIJ
uipJdAo2kl48D7vhMJGycppP+IlfHdGuKCvzaGY91vl+jLNngy5HZLJeAdY4jrMdf+3MbvxpZtmu
67YD7cDjwCNALvAy8DzgOI5ze+z2IUBDlZIw7IMHgOv3rwF/jc3ixR55efNd1fwZbSBw+CArVnhE
owZ9fWogIBNTsJG0YnafwDx3jnDtBjo6/Le/gs0V8ZbPoHU2kjxc130D+DZ+44CtwJeAF4GnYnf5
An7g+THwNdd1G1zX3Q98Fb9b2h8Bf+y6rtK8JAz7oN84ILxpy3XHTpxI0T1sxojUxoJNQ/2YvWwU
bGRiWmMjacWONQ6I1NbR8bTJsmVRFi8OuKgEUlER5Rfxls/trYRv3x5wRSKT47ruV4CvjLnp/jHH
XgMqbvCYbwHfmvPiRKYhI9YR7dpWzxcuwMCAkbJ72MSFa+sAv+Vz4T0KNjI5GrGRtBJvHDBcVcfx
4wYlJal9Ypiqq1o+a8RGRCQw9sH9RJcXEC1afdXtXV2pvYdNnLdoMZG1JdgNh1lR6C+uOXVKH1tl
YnqHSFqxG+oBOL50E+Gw9rC5VmGhR1dufJNOLTcQEQmCceYMVudxQpuubxzQ3Z3ae9iMFa7bgNnX
R0mW3wNEIzZyMwo2klashsNElyyh+VIxoI5o1zIMWFSxnPMswtSIjYhIIG62vgZSf8QGrjQQKDl3
EIBTpxRsZGIKNpI+BgawOtr9xgFH/U32yspS/8QwVeUVHi4OVkc76q0pIjL/MuLBZpyOaJAuIzb+
fnMrT/nBpqdHH1tlYnqHSNqwmxowPI9wbd1oRzSN2FyvvNxfZ2OGRjA7jwddjohI2rH37wWubxwA
6bPGBq6M2OS11ZOb641OwxMZj4KNpI34+ppw7QaOHlWwGc9VLZ/btc5GRGReeR4Ze3YTKV5DdOWq
6w53dxsYhseqVak/YhNdXUw0Px+74RBFRVEFG7kpBRtJG2ODTUeHQX6+x5IlAReVgCoq1BlNRCQo
5vFjmH29hLbdesPjXV0mhYUemZnzXFgQDINw7Qas9jbKV1zkzBmTwcGgi5JEpmAjacOuP4Rn24yU
Oxw9amq0ZhxjWz6rM5qIyPzK2LsbgPC2W647Fo3CyZNGWqyviQvXbcDwPG7P9bdrOHlSozYyPgUb
SQ/RKHZTI5FKh5NnsxkZUavn8eTlwfmCcgCsVgUbEZH5ZO/ZBXDDEZveXoNQyEiL9TVx4Vp/nc3G
6AHgSlc4kRvRu0PSgnW0HePyJcJ1G0YbB5SUpM+JYapWVebSxWpMjdiIiMyrjL278TIyCG/YdN2x
eEe01avTacTG74xWecnvjBZ/DURuRMFG0oJ11foaNQ64mXgDAbu7Cy5dCrocEZH0MDiIffgQ4Q0b
ITv7usPx0Yri4vQ5f0XWO3gZGazu9YNNd7c+usr49O6QtDDaOKCmVsFmEkpLo7RQCYB1tCPgakRE
0oN9+BBGODxB4wB/tKKoKH1GbMjMJOxUk99Zj0VYIzYyIQUbSQt2YwMA4Zo6Ojr8X4qlpWl0Ypii
sjLvSrBpbwu4GhGR9HClccCNg018tCKdRmwAInUbsEaGqKRFIzYyIb07JC3YjQ1ElxfgFRbS0WGS
l+exfLmCzXjKyqK0UgGA1aFgIyIyH+xYsNGIzdXiG3Xekb1fe9nIhBRsJOUZAxexjh8lXF2L5zHa
6tnQ78ZxlZSMCTYasRERmRcZe3cTXV5AdO26Gx7v7jbJykq/C3Pxzmh35e5TVzSZkN4dkvKspkbA
X1/T02MwOKhWzzeTnQ3Dq0uJYijYiIjMA/NkN9aJLkK33Mp4V966ugxWrfIw0+zTW7i2DoAN1HPh
gsHAQMAFScJKs38ako7seLCprVPjgCkoKsvkOGsx2xRsRETmmr1n4mlow8PQ22um3foaAC9/CZHV
xVQOHgK0l42MT+8MSXl2o98RLVJdM6ZxQPqdGKaqrMzvjGb39mAMXAy6HBGRlDbaOOCW2254PL62
JN3W18SFa2pZMniS5fSqM5qMS8FGUp7V2IBnmoTXV40ZsUnPE8NUxIMNgNXRHnA1IiKpLWPvbjzT
JLRpyw2Pp2tHtLhITXw62mF1RpNx6Z0hqc3zsJsaiZSVQ04O7e3+W76kJD1PDFNxVbDROhsRkbkT
CmEf3E+kqgby8m54l3hHtNWr0/PCXLimFoCNHNKIjYxLwUZSmtl9AvP8OcKxKz2trSYLFnisXJme
J4ap0F42IiLzw244jDE0RGicaWhwZV3J6tXpeWEufh7fyCGN2Mi49M6QlGY3+RtzRqpriESgo8Ok
okKtnidj3boobYZaPouIzLXR/WtuuXHjAGB0lCJdR2wi5RV4mZkasZEJKdhISrMa/WATrqmjq8tg
aMigvDw9r3ZNVWYmhIpLiGAq2IiIzKGM3buA8RsHgEZssG3CTjW1NNBzIhJ0NZKgFGwkpcU7ooVr
amlr89/ulZVpelKYhjXlNkcpwVSwERGZMxl7dxPNzydSXjHufbq7DRYv9sZbgpMWIjW15DBEzol2
vPQcuJKbULCRlGY3NRJdkEd0zVpaWvy3e0WFgs1kxRsIWGf6MC6cD7ocEZGUY/T2Yh076u9fB+Ee
LwAAIABJREFUM8E86a4uk6Ki9D5/xdfZVA4d5ty5gIuRhKRgI6lrZASrpZlIdQ2YJq2tCjZTpZbP
IiJz62b71wCcPw8DAwbFxek9THF1ZzR9hJXr6V0hKctqacYIhwlX+78IW1tNDMOjrEzBZrLU8llE
ZG5l7PHX14S2jd84oLMzvfewiQvXbgDindHUQECup2AjKWvs+hrwg01xsUdOTpBVJRcFGxGRuWXv
3Y1nGIS33TLufdK9I1qct3w5lxatYCOHRsOeyFh6V0jKsmMd0SI1tVy8CD09pqahTdGaNR7tplo+
i4jMiXCYjP17iVRV4y1cNO7durr8j2tr1ugcNlhRRwnH6Gm+GHQpkoAmFWwcx/mO4zj9juO4juPc
ec2xhx3HaXMc56zjOH99zbEHHcfxHMf5z7NYs8ikxPewCVfXaH3NNGVkQGTNOkLYCjYiIrOtvh7j
8uUJp6GBpqKNZWzyZ2HEt3MQGeumwcZxnIeALwMPAzuA7445ZgA/BJ4DngC+7jjO5tgxC/gfwNnZ
L1vk5qymRiJFq/Hyl6gj2gysKzfpoFQtn0VEZtu77wITNw4A6Oryp6KtWZPeU9EAMrb5wWbxsfqA
K5FENJkRm/uBTtd1dwEvAJscx1kaO1YOFAPPu677CjAAPBA79ifAceDwrFYsMglG/1msk92Eq2sA
RvewUbCZutGWz/1nMc71B12OiEjqeOcdYOLGAeBPRcvI8CgsVLCJt3wu6jusvWzkOvYk7rMCiG9g
Ef9UsxJ/JGZF7P/HHl8VCz7fAO4Dvj+ZQpYsycW2rcncdd4UFCwMuoSklBCvW+M+ALK2baGgYCGd
nf7N27fnUlAQYF0TSIjX7QY2bWK0gcDy/lNQuTbgiq6WqK9botPrJpIA3n2X6KLFRCrXT3i3ri6D
oiIPUyujiVSuJ2zYVIcP09cXdDWSaCYTbKbjvwBPuq7rOo4zqQf091+eo1Kmp6BgIb29Wpg2VYny
umW/s5uFwIWSSoZ7L9LQkMuCBSa2PUBvb9DVXS9RXrcbKSiweCMWbC7sPcRwaXXAFV2RyK9bIpvo
dVPgEZkfxtkz0NxM+P4HmSixDA3B6dMmd98dnsfqElhWFqfz17Oh/zCNbR5l5UEXJIlkMtn/JJAf
+3557Gv3mGMA+bH1Nstixx4Fvuw4zhBwL/7am6/PTskiNxfviBauriUSgfZ2vyPaBJs6yzjU8llE
ZPZl7N8L3HwaWny/lnTfnHOsc2tqWcgAPbuOBV2KJJjJBJtXgDWO42wHHgN2A8OO42S7rtsOtAOP
A48AucDLwEPARmAzsAf4x9h/IvPCbmzAs20ilevp7DQYHja0vmaaios9Oux4sGkNuBoRkdRg7/OD
TXjrtgnvp45o1wtX+etnB3ergYBc7aZT0VzXfcNxnG/jNw7oBj4HvAicAz4EfAH4AfBp4Guu617V
f89xnMtAn+u6mgkp8yMaxTrSRKSiEjIz1ThghmwbzHWrGW7L1IiNiMgssfftASC0ZfyNOUF72NxI
5tYqeAaspnr85dwivkmtsXFd9yvAV8bcdP+YY68BFRM89v7xjonMBbPzOOalAUZq/JaQ8VbPlZU6
KUxXaYVJW1s5Tls7eB6a0yciMgOe509FKy3FW758wrvGWz1rKtoVi+7yR2wWd2rERq6m/hqScsau
r4Erwaa8XMFmukpLYy2fL57HOHMm6HJERJKaebQD8+xZuP32m943PmKzerXOYXEZleu4bORS1K9g
I1dTsJGUYzf5wSYS28OmqcnCtj1NRZsBNRAQEZk9GbFpaNw28caccGXEZvVqjdiMMk2O5tZQEWpi
5FIo6GokgSjYSMqxmhoBf8QmGoXGRpPKyihZWQEXlsSuDjZqICAiMhN2rCPaZEZsOjtNVqzQOexa
pwtryWKEvnfbgy5FEoiCjaQcu6mB6MJFRIvXcPSoweXLBjU1Gq2ZiauCTYdGbEREZiJj7x4824Yt
Wya8XyTit3vW+prrDZT4szIGdh4JuBJJJAo2klqGhrDaWv1paIZBQ4MFQG1tJODCkltRkcfxrPiI
ja6OiYhM28gIdv0hwjV1kJMz4V1PnzYIhw11RLsBr84PNhxuCrYQSSgKNpJS7BYXIxIZbRzQ0OC/
xWtrdVKYCdOErNKVXCYHq01T0UREpsturMcYHr7p/jUAnZ1aXzOe3NuqAVjQ3nCTe0o6UbCRlGKN
dkTzr+RcGbFRsJmpkjJopQKzrc1v+SwiIlMW35gztHXi/WvgSkc0bc55vZWbCznDUgpOK9jIFQo2
klLsWOOASM2VEZuCgiiFhfogPlPxdTbW4CXM0z1BlyMikpTiHdHCUwg2mop2vYJCaDTrWHWpDQYH
gy5HEoSCjaQUu9HvaR+uruHcOf+koNGa2VFW5qnls4jIDNn79hBduIhIReVN76vNOcdnGHAivw4T
D6vZDbocSRAKNpJSrMYGIquL8Rbn09ioaWizSXvZiIjMjHH+HHZrC+HNW/3FizfR2ampaBPpL94A
wOVdjQFXIolCwUZShtHTg3W6h/CGjcDYxgHqiDYbFGwkkTmO8x3Hcfodx3Edx7nzmmMPO47T5jjO
Wcdx/vqaYw86juM5jvOf57VgSUv2/n0Ak2ocAH7zgPx8j0WL5rKqJLahDoCh3eqMJj4FG0kZdsNh
AMK1/hUcdUSbXStWeHTlKNhI4nEc5yHgy8DDwA7gu2OOGcAPgeeAJ4CvO46zOXbMAv4HcHa+a5b0
lBHbmDO05ebBxvP8EZu1a3UOG8+i7f56WuuIgo34FGwkZdj1sWBTFx+xscjM9Kio0ElhNhgGLCgr
4CJ5mAo2kljuBzpd190FvABschxnaexYOVAMPO+67ivAAPBA7NifAMeBw/NbrqQrOxZswttu3jjg
9GmDwUFDwWYCZduW0MVqFndqKpr47KALEJktdsMhAMJ1GwiH4cgRE8eJkpERcGEppLzCo6Whks0d
RyAandQccZF5sAI4H/u+P/Z1Jf5IzIrY/489vioWfL4B3Ad8fzI/ZMmSXGzbmpWCp6qgYGEgP3ey
Erm+hKnN82D/XiguZlndlcYB49XXGtsyrKoqg4KC4E5kCfP63YBlwS7qeP+ll8AOw5IlQZd0nUR+
/SD16lOwkZRh1x8mumgx0bXraGs2GR42NA1tllVU+Otstg7txzzZTXR1cdAliUzXfwGedF3XdRxn
Ug/o7788txWNo6BgIb29FwP52ZORyPUlUm3miS6W9fQw/OjjXIjVNFF9Bw/aQA7Llw/R2xuax0qv
SKTX70YKChbSmlMHgy/Rv2M34e13BF3SVZLh9UvG+iYKO7rcKqnh0iWs1hbCdRvAMNQ4YI6sX68G
ApKQTgL5se+Xx752jzkGkB9bb7MsduxR4MuO4wwB9+Kvvfn6PNUraciO7V8zmfU1AMeP++cxTUWb
WH+RvyG3d1gbdYqCjaQIu6kBw/P8YIMaB8yVq4JNW2vA1YiMegVY4zjOduAxYDcw7DhOtuu67UA7
8DjwCJALvAw8BGwENgN7gH+M/ScyJzL2TX59Dfgd0QDWrtUeNhMJOX6wUWc0AU1FkxRxbeOAPXss
DMNj40aN2Mym8vIozYYDHlhtLUGXIwKA67pvOI7zbfzGAd3A54AXgXPAh4AvAD8APg18zXXdqy7t
Oo5zGehzXbdvPuuW9GLv34tnGIQ3bZ7U/Y8d8y/QrVmjC3QTyd7qEH3BwGhUsBEFG0kRo8GmdgPD
w7B/v0VNTVS9/2dZdjZcKl4PnWC3NAddjsgo13W/AnxlzE33jzn2GlAxwWPvH++YyKyIRMg4sJ+I
U4WXN7nF0MePmxQWRsnJmePaklxJdRatVFB8vIFLnue38JS0palokhLshkN4GRlEnCoOHTIZGjK4
/XaN1syFVdWLOMlKcDViIyIyGVazi3H50qTX10QicOKEoWlok1BREeUwG8gd6sfsORV0ORIwBRtJ
fpEIdmMDkfVVkJnJzp1+O9bt2xVs5kJlZZQjVJHRfRwuB9MlSkQkmcQ35gxPMth0dxuEw9rDZjLW
rvVoMmMbdTaqgUC6U7CRpGe1t2EMDo42Dti1yw82t92mYDMXHCfCEaowPE+d0UREJsHe63dEC29V
R7TZZlnQt6rO//6I1tmkOwUbSXp2/ZWNOaNRP9isXRulqEhD+HMhPmIDYLdqnY2IyM3Y+/fiZWcT
rq6d1P3VEW1qhiurAQjv04hNulOwkaQ3tiNaS4vJ2bOmRmvm0NhgY6mBgIjIxC5fxm5qILxhE2Rk
TOoh8Y5oGrGZnAWbyhgiCxo0YpPuFGwk6Y0dsdH6mrm3aBGcLVgPgKURGxGRCdmHD2FEIoQmOQ0N
NBVtqsrWmzRRTd7xI37nBUlbCjaS3DwPu/4wkbXr8BbnjwYbdUSbW7nOai6Tg6HOaCIiE8rYH1tf
M8nGAQDHjxuYpsfq1ZqKNhmVlVHqqSMjNIh1rCPociRACjaS1MyT3Zi9p0c35ty502LJEo/KSl3l
mkvrq8DFwW5rgaheaxGR8dj7/GAT2rx10o85ftykqMib7My1tBdv+QxgNWk6WjpTsJGkFu80E9q6
jZMnDY4f99fXmHpnz6n4OhtreBDzRFfQ5YiIJKyM3buILl9OtLRsUvcfHoZTp9TqeSry8uB0QQ0A
dpMaCKQzffyTpDa6N8DWW0bbPN9+ezjIktLC+vVqICAicjNm9wmsE12EbrkNDGNSjzlxwsDztDnn
VEVq/GATPqgRm3SmYCNJzd6/F88wCG/azBtvaH3NfFHLZxGRm7P37AIgdMvtk36MOqJNT8GWIs6x
GKO+MehSJEAKNpK8IhHsA/uJrHcI5SzihRdsCgqibN2qk8FcKyjw6F7oAGC1qIGAiMiNZOz2g034
1tsm/RgFm+mpqfWop468k60wNBR0ORIQBRtJWlazi3lpgNDWW3j7bYszZ0weeyyMZQVdWeozDDDW
lxHFwGjWiI2IyI1k7NmJZ9uENm2Z9GM6OvyPZmVlCjZTUVPjd0YzoxGsVl1wS1cKNpK0RtfXbNnG
c8/ZAPze72l9zXwpq8vmGOswXAUbEZHrDA1hHzpIeMNGyM2d9MM6Ovy1OKWlWmMzFaWlUZrsOkAN
BNKZgo0krXhHtKGN20anoWl9zfypq/PX2WSd7cE4fy7ockREEop98ABGKOQ3DpiCjg6TRYs8li5V
sJkK24bz6/xgYx6uD7gaCYqCjSQte/9evOxs3ujfyJkzJh/8oKahzacNGyJXOqNp2F9E5CoZe+Lr
aybfOCAahaNHTUpLo5NtoiZjmJv8YBPeq2CTrhRsJDldvozd1EB4wyaeeyEHgMcf1zS0+VRVFaXZ
iDcQ0HQ0EZGxMnbvBJjSiM3JkwbDwwalpVpfMx2lm/Nop5SsI4fB04hXOlKwkaRkHzqIEYkwvOUW
fvUrm8JCTUObb7m5cHH1egAsNRAQEbnC88jYvZPIqiKiq4sn/TA1DpiZ6uooB9hMzsVezJ5TQZcj
AVCwkaQUbxxQn3MrZ8+qG1pQMjb5U9FGDh4JuBIRkcRhHj+G2Xua8BQ25oQrwaakRMFmOmpq/GAD
YNcfCrgaCYKCjSQle5/fOOC7e+4A4EMf0jS0IKzdtpSTrMRuVAcaEZG40WloU9i/BqC93f9Ypo5o
01NQ4NGxaCMAdv3hgKuRICjYSFLK2L+X4UXL+clbldx9d1jT0AJSVxflEBtZeOa4OqOJiMTEGwdM
vSNavNWzRmyma7jaDzbefgWbdKRgI0nH6O3FOn6Mnd6tgME3vzms7jEBiQcbALupMeBqREQSg717
F15WFuENm6b0uI4OkwULPAoKNGIzXcs2r+YsS+CQOqOlIwUbSToZu94F4JWL2/nIR0Js2qQrW0FZ
vtzj+GK/vabVoJOIiIhx/hx2w2HCm7dCVtakH+d5fqvnsjK1ep6J2rooB9nEgu5WGBgIuhyZZwo2
knTMHW8B8LZ9L1/96nDA1chI9QYAwvu0zkZEJOOdtzGiUUbuumdKj+vpMRgcVKvnmdq82W8gYHge
dpPOS+lGwUaSzrlfvM0QWdR8fitr12q4PmiLb68khE30gE4gIiIZb70BQOjue6f0uCuNAxRsZqKi
IkpTpj8FUA0E0o+CjSSV5348wOregxzMup3/9Jcaq08EVRttmqgm72iDv222iEgay9zxJl5W1jQa
ByjYzAbLgpEafyaBd0DBJt0o2EjS2LXL5Ff/9x5MPIo+uZ3Fi4OuSADq6iIcYiNZoUuYx44GXY6I
SGCMs2ewGw77oSY7e0qPvdIRTTMRZmrxdocRMgjvUbBJNwo2khS6ugw+97kc7or4Q/wLH7sr4Iok
bt06DzfTvzpmq4GAiKSxjLf9NaChKa6vgSsjNmVlGrGZqY23WDRQS15HA0S0HUQ6UbCRhOd58Gd/
lk1fn8mnVr+OZ9tTHuKXuWOaMFDmd0aLHlCwEZH0lTnN9TXgB5vcXI/CQo3YzNTmzREOsJnM8CBW
e1vQ5cg8UrCRhPfkkxm8+abN4w/0s+rkfsKbtsCCBUGXJWNk3+4Hm8Gd2stGRNJXxltv4uXkENqy
bUqP8zw/2JSUqNXzbFizxqNtQWyPtfpDAVcj80nBRhLaqVMG3/xmFnl5Ht/++BsYkQihO+8Ouiy5
xvp7C+hlOVnNGrERkfRk9PZiH2kidOv2Ke1fA/657tIlQ9PQZolhwKDjB5uRXVpnk04UbCRheR78
5V9mceGCwTe/OczK5h0AhO7U+ppEc8utUQ6xkWX97doQTUTSUubbbwIQunvq62tc1/845jgKNrNl
wZ21AIR2Hgi4EplPCjaSsF5+2eLXv87grrvCfPazITLf3oFnmoRu2x50aXKNlSs92hf4DQSsJk1H
E5H0k7HDDzZT3ZgToLlZwWa2Vd2xCJf15Dfv1VYEaUTBRhLWj3+cCcDf/M0w5tBl7P17CW/YhLdw
UcCVyY0MVvrrbC7s0EadIpJ+Mt56Ay93AeHNW6f82PiIzfr1+gA+WzZvjrKT28kZuYDV2hJ0OTJP
FGwkIfX0GLz6qsWWLRFqaqJk7NuDEQoRukPT0BJVznZ/2H/gLQUbEUkv5qmT2K0thLbfARkZU358
c7OJaXqUlyvYzJaCAo/mfL+Dqr13T8DVyHxRsJGE9O//bhONGnziEyEAMt58HZje3gAyP9a+fz1h
LLJcNRAQkfSS+erLAIzc/+CUH+t50NxsUVLiTbXngNzE4OZb/a+vK9ikCwUbSTieB089lUFmpsdH
PuIHm8zXX/P3r7lLHdESVe22TBqMOopP74dQKOhyRETmTebLLwEw8t6Hp/zYvj6D/n6D9eu1keRs
W/W+GgbJxtipYJMuFGwk4ezfb9LcbPHII2Hy88E4ewb7wH5Ct96Ol7cw6PJkHFlZ0LrsdnK8QcL7
NWojImlieJiM3/2WcGkZkfLKKT9cjQPmzh33muxjK8tO1sPly0GXI/NAwUYSzlNP+fOTP/nJ2GjN
m7/D8DxC0xjil/l1sc6fz9z3C10dE5H0kPHu25iXBqY1WgNqHDCXKiujHMq+DcuLYB9U2+d0MKlg
4zjOdxzH6Xccx3Uc585rjj3sOE6b4zhnHcf569htluM4/+Q4znnHcY45jvPEXBQvqWdoCP7jPzJY
sSLKfff5w/IZr78GTG/ussyv3AdvAcB7e1fAlYiIzI/MV2LT0B6aXrDRiM3cMQwYqPPPSxdf3h1w
NTIfbhpsHMd5CPgy8DCwA/jumGMG8EPgOeAJ4OuO42wGPgt8Argd+DfgnxzHsWe9ekk5L79sc/68
wcc/HsK2Ac8j8/XXiC5dSnjj5qDLk5uofLSMMyyloF0nEBFJD5kvv4SXu2DaXTubm00Mw6OiQsFm
Lix8yA82Q2/sDbgSmQ+TGbG5H+h0XXcX8AKwyXGcpbFj5UAx8Lzruq8AA8ADwIvAJtd1jwBHgQWA
FkfITb3+ugXAY4+FAbBamrFOdDFy7/1gWQFWJpOxuhj2Z97OqsvtcLo36HJEROaU1d6K3d7mn6Om
2dLMdU3WrPHIzZ3d2sS34dHVnGIFS1s0RTodTGYUZQVwPvZ9f+zrSuBs7BjXHF/lum4P0OM4zjLg
r4ADruvGH3tDS5bkYtuJ9cG1oEBZbDpm8rrt2AGLF8NDDy3wc8yTbwGQ/cFHyU7xv49Ueb+dqbwD
Gl4k/OZhVv3J7835z0uV122+6XUTmbmZdEMDOHMGentN3vve8GyWJWNUrvfYm3kbjww+T193N15R
UdAlyRyas+lhjuMsBH4NFAAfv9n9+/sTq1tFQcFCensvBl1G0pnJ63b0qEFHRx4f+ECIs2eHAFj0
yxfIAs5svYNoCv99pNL7zdu+DRqg8993YH90btdFpdLrNp8met0UeEQmL/OV3wAw8tD7pvX4pib/
qxoHzB3DgL6yW+HI85x9cQ9L/vDxoEuSOTSZqWgngfzY98tjX7vHHAPIj623WQZ0x77/V6ASeMh1
XY3/yU298Yafs++9N9bLf3iYzLd3EF7vEF1dHGBlMhXrPr6FKAYLDqmBgIiksIEBMt55i1DdRqKr
pjcK0Njof3Uc7WEzl+y7/Y06z/9mX8CVyFybTLB5BVjjOM524DFgNzDsOE6267rtQDvwOPAIkAu8
DHwE+CDwRaDecZw8x3ESa56ZJJw33vDfIvfe6w/JZ+zeiXH5MiMPvCfIsmSKyrfkccSqpfTMHryQ
pleISGrKfON1jJERRt47vdEauBJsNGIzt0o+tokoBjmHdZ091d002Liu+wbwbfzGAVuBL+E3B3gq
dpcv4AeeHwNfc123Ifb/AE8DF2P/3TOrlUtKiUbhzTdtioqilJd7AGT+9lUA7V+TZAwDOotvJ9e7
TM8rjUGXIyIyJ7J+9QsARh7+wLSf4/Bh/2tlpYLNXCrfkodr11Lat4fQpZGgy5E5NKk1Nq7rfgX4
ypib7h9z7DWg4pr7fx74/CzUJ2mivt6kv9/g4YfDGIZ/W+YrL+FlZzNyx93BFidTFrnlVjj2Pzn9
iz2sfGRj0OWIiMyu4WEyX3qRyOpiwlu2TespPA/27YOysigLtbRtThkGnKi8l+qmevb9616qvnhH
0CXJHJnUBp0ic+13v4uvr/GnLpmdx7GbGhm5+17UAzP5rPiQv2+AvVv72cj80EbSMp8y33wd88J5
hh/7PUavxk3R0aMG587Bpk1aXzMfsh+7H4ALz/4u2EJkTinYSEJ4801/fc099/i/4K+00Hx/YDXJ
9K15qIJzRj5rTuzE84KuRlKdNpKW+Zb5/HMADH/wQ9N+jkOH/PPexo0KNvOh9HN3EMFkZf1vdV5K
YQo2ErihIdi506K6OsKKFbH1NS//Gpj+3gASLMMyaS3YTlmklRM7u2/+AJGZuR9tJC3zJRQi68Vf
Elm5ivAtt077aQ4e9D+Cbd6s9TXzIbNgMS1LbmXTyC5a9g4EXY7MEV2dksDt2WMxOGhcafN86RKZ
O94gXFNHtHhNsMXJtJ277T3wy1/T+y+/pXj7p4MuR1Jbym8knej7CyVyfbNe229+A+fOwZ9+loIV
i6f9NPGOaA88kMvi6T/NnEvkv1uYWn2n7n0v9nM7OfHkHu565INzWNUVqfT6BWGq9SnYSODeesv/
oHDXXf76msw3f4cxPMzw+zQNLZkt+eSD8EvIe+sVQMFGEk+ybCSd6BvRJnJ9c1Fb3r/8GznAufc+
Smiaz+15sHdvHpWVBiMjF+ntndUSZ00i/93C1Otb8vE74TmIvPQyvb33z11hMan2+s238eqbKOxo
KpoE7t13LQzDY/v2+PoaTUNLBWsequC4uY6a7le1n43MNW0kLfMjHCbrheeJFK4gdOvt036ao0cN
zp832Da9hmoyTVn33cqQmcPG3lfp6Zle0wdJbAo2EqjhYdi716K6Okp+PuB5ZP7m10SXLSO89Zag
y5MZMEyDpnXvI987R+ez+4MuR1KbNpKWeZHxzluYZ84w8ugHwZr+2yXeOEDBZp5lZXGi/G5qaeS3
TyboMJnMiIKNBOrAAYuhIYM77vBHa+zDB7F6TjHynvfN6KQhicF7n7+56vmnXw24Ekll2kha5kvW
L34OzKwbGlxpHHCLrt/Nu9zH7wPg5L++GXAlMhe0xkYC9e67fniJB5t4m2etr0kN5X90N6Hv2xTu
fwX4v4IuR1KYNpKWORcKkfX8fxBdXkBo+503v/8EDh70z31btsDIyGwUJ5OV/YH74G9h/fHXaGz8
KDU16kqXSjRiI4F65x3/l/vtt8eCzUsv4Nk2ofsfDLIsmSX56xZzeOEd1Fzazbm2M0GXIyIybZmv
v4p59ixDH/4o2NO/Lux5/lS0srJoQndDS1Xh2g0M5S3jIV7hqX/T9f1Uo2AjgQmHYdcui/LyKCtW
eJgnusg4sJ/QnffgLdJv+1TRt/UhTDyO/fCNoEsREZm2rJ89A8DwR5+Y0fPEGwds2qSNOQNhmkQf
uI9iTnDo6RZCoaALktmkYCOBaWgwGRgwuPPOWJvnF38JwPCj89NbXuZH/iffA4D5itbZiEiSGhgg
69cvECkpJbxlZiv+DxzwZyps3KhgE5Tww37X1QfO/ZxXX9V63lSiYCOBiU9Di7d5zvrV8wCMPPJo
YDXJ7Cv5UB19ZgE1x18mEvaCLkdEZMqyXvwlxuXLDH30CTBm1ib47bevnoIt82/k/R8gmpHJEzzD
U09lBF2OzCIFGwlM/Jf7HXdEMPr6yHjnLUK33EZ05aqAK5PZZFgm7rr3stI7Seszh4IuR0RkyrKe
/XcAhj82s2loADt22OTleWzerEXrQfEWLSb04HvYyGGOvdRKd7f2tEkVCjYSiGgUdu60WbMmSnGx
R9ZvXsSIRhn+gKahpaLhxx4HIPSTZwOuRERkaozeXjJff43Q5i1Eyitn9FwnTxq0tZls3x6ZSf8B
mQXDj38YgA9Hfsr3v58ZcDUyWxRsJBCua9Lfb4xOQ8v81S8AGP7AYxM9TJJU6ZfeQz8FHSaZAAAg
AElEQVT51Bx8BiKafiEiySPrF89iRCIMf+TjM36uHTv8mQp33x2e8XPJzIy8/wN4WVl8yn6G//W/
Mjh3LuiKZDYo2Egg3njD/+V+111hjIGLZP7ut4Sra4mWlQdcmcyFvGVZvFP0EVaET9Dz03eCLkdE
ZNKyf/oMnmky/OGPzfi53norHmx0gSdo3sJFjDzwHqrD9ay5dIR//meN2qQCBRsJxGuv+WPwDzwQ
IfOV32CMjKgbWoqLfNK/2nnx+/8ecCUiIpNjtbaQsXc3obvvI7pi5Yyfb8cOm/x8j9para9JBPHp
aJ/JeoYf/CCDwcGAC5IZU7CReTc46HdEq66OsGqVR+YLfjc0ra9JbZu+vJ0TxmqqG/6D6OBw0OWI
iNxU9lP/CsDQpz4z4+c6dszg+HGTO+4IY6nDcEIYefgRvKws/mDBM/T1mTz9tDqkJTsFG5l377xj
MTRk8OCDEbh8mcyXf0NkbQmR2rqgS5M5lJNnsd95gnzvHEe/pz1tRCTBhcNkPf0k0cX5DD8y8/Wf
8Wlo99yjaWiJwlu4iJEH38uqs41szmzgW9/K5Pz5oKuSmVCwkXn329/609AefDBM1m9exLw0wPCH
PzrjvQEk8S34gj9H3XtS09FEJLFlvv4qVs8p//yUkzPj59uxwz/33XWXgk0iGf49fzra3237MadP
m/zX/5oVcEUyEwo2Mu9ee80iN9fjttsiZP30aQCGPvaJgKuS+VDzqTpa7Co2Hf8VQ6cvBF2OiMi4
sp/8FwCGPvXZGT+X5/kd0ZYvj1JVpfU1iWT4kceILlnCPe4/UVt+iR/9KIMDB/TxOFnpb07m1fHj
Bi0tFvfcEyH7Yh+Zr71CaMMmIk5V0KXJPDAtg+ZbP0EOQ7T/t+eCLkdE5IaMM2fIfOkFwtW1hDdt
mfHzHTpkcuqUyb33RjQ5IdHk5DD06f8N6+wZfvzok3iewV/8RbZ2JkhSCjYyr+LT0B54IEzWc89i
hMMMa7QmrRT+n58ijMWa//iefxlTRCTBZP/saYxQyG8aMAtJ5Oc/9xelP/649q9JRIOf+0M802Tj
m//IE0+EOHTI4i//MouoBteSjoKNzKvXXvMXTz7wQJjsnz2DZxj+/GVJGyV3r+LVpR+jbKCe7id3
BF2OiMjVPI/sJ/8Fz7YZ+ujML7x5HvziFzZ5eR4PPqhgk4iia9cx8r5HyNi/j//34zuoq4vwk59k
8ud/rpGbZKNgI/NmZATefNOmtDRKOW1k7NlF6J77ia5cFXRpMs+8//QnAAz/P98LuBIRkavZB/Zh
N9Yz8r5H8JYvn/Hz7dtn0tlp8v73h8nOnoUCZU4M/uEXASh85gc8++xltmyJ8NRTGXzuczm8+66l
0ZskYQddgKSPt9+2GBgw+MQnQmT/7BkAhj72RMBVSRC2/u/bOPjfbuOWk7/i4O86KL6vNOiSREQA
yPnh9wF/etJsiE9D+9CHQrPyfDI3QvfeT7iikqznnmXJf/4bfvrTAj71qRxeesnmpZds1q6NUlsb
ITcXFi3yqKqKsnFjhNraqAJrAtGIjcybJ5/0f7l/+EMjZP30abycHEYe1aac6cgwoP+zX8LE49TX
fhh0OSIiABg9PWT9/GeE1zuE7ntgxs8XjcLzz9ssWuRx332a05TQDIPBP/wixsgIOT/5EQsXws9/
PsjTT1/miSdCnDlj8OKLGfzsZxn86EeZ/NVfZfPIIwvYunUBv/mNdlxNFAo2Mi/6+gx+9SubqqoI
d3pvY7e3MfzwI3gLFwVdmgSk+hsfpMcq4q7mf6ar8WLQ5YiIkPOTH2GEQgz+wRdnpWnA7t0W3d0m
H/hAmCxtj5Lwhj/xKaKLFpPz/30PY+AilgUPPBDh7/9+iJaWAVz3Ivv3D/Dqq5f4zncG+dznRrh4
0eAzn8nlq1/NYmgo6D+BKNjIvHj6aZtQyOAznwmR+/1/AGDo818IuCoJkpmVwdFHv8giLtL0F/8a
dDkiku5GRsj+5/9JdOEihp74/Vl5yp//3J/xr2loycHL+//bu/PwKKqsgcO/6jXp7BshrA4q10Fh
wA10UEBUUHEBZHQUFLdBEB33XYRRHHFGB2VUUFw+AVFcBgURwREHFRVX3PAqKJvsZO8kne6u+v6o
joSYQMjW3eG8z1MPobur6vRNp06fW7dupVA+djyOXbtInPHYHs+5XJCRAe3bW3TvbnL++SEeeCDA
4sVldO0aZuZMD6NHJ8q1OFEmhY1odpYFs2d78HotLujzA55FCwj+oRfBPsdHOzQRZZ3vu5hSI5mB
n/6Tbz4qi3Y4QogDmHfhazi3b7NvyJmc3OjtFRbCCy+4yc01OeEEGYYWL8rHjMPMyiLxsWkYBfn7
fP3hh5ssWVJG//4h3nnHxbRpnhaIUtRFChvR7D780MnatQ7OPDNE7rzpGJZF+ZhxTXKaX8Q3Z5ss
Np57Nbls55srniAkM6EKIaIk8cnpWIZB+aVNM5rg6ac9+P0GV15ZidvdJJsULcBKTqHsmhtwlBTj
+/fD9VrH54PHH68gL8/k/vs9fPSRXHMTLVLYiGb33HP2Ef3SYTtImDOLcF47AmcNjXJUIlbk3H8V
xZ4sRm17kFkPy7U2QoiW5/r8U9yffULlqYMxf9el0dsrK4Mnn3STlmZx8cUyDC3elI++jHDbPBJn
TsfYtq1e62RlWcyYYV9kM2ZMArt2SedtNEhhI5rVjh0GCxe6OPTQMH31Mzj8pfZc8R45VStsVkoq
FddeTzpFuB6cyoYNkgyEEC3L99ADAJRfMbZJtjd3rptduxxcdlllU4xqEy0tMZGy62/GKC8naeo/
6r1anz5hbrmlki1bHNx3n3zPiQYpbESzmjjRS2WlwWUXl+ObOR3L56Ni1OhohyVijHHV5ZSmt2Ns
aBp/vzpfLr4UQrQY10cf4l2ymMrj+xI8oV+jtxcMwmOPeUhMtLj8cjlbE68qLhhFuPNBJPzf0zi/
X13v9a66qpKuXcPMmeNm1apmDFDUSgob0WzeecfJSy+56dkzzBjfLJy/bKLi/AuxMjKjHZqINYmJ
mHfeSiIVnPLhZGbOlAHpQogWYFkkT54IgP+Ou5vk2s9nnnGzcaODCy4Ikp1tNXp7Iko8HkrvnYIR
CpFywzXUt8fN7Ya//S2AaRpcd509gZJoOVLYiGbh98PNNyfgdFpMm7CR1HvvxPL5KLvqr9EOTcSo
wAUjqeiiuIInWTrxU779Vg5PQojm5fnvEtwff0hg8OmEjund6O2tXu3gnnu8ZGaaXHttZRNEKKKp
ctBpBM48B/cnH5Pw3DP1Xu+kk8KcckqIZctg0SJXM0YoapJvDqJZTJniZcMGB+PHV3L087fiyM/H
f+udmB07RTs0EatcLsof+TeGAdNDl3PNX6C8PNpBCSFaLdMk6d5JWIaB/7YJjd5cRQVceWUCgYDB
1KkV5OZKV31rUHrfA5ipaSTdczeOrVvqvd6kSRW4XPaQ/ECgGQMUe5DCRjS511938cQTbrp0Mbn9
qEUkvPwiwZ69muyiTNF6hY7tTfnlYzgMzXk/3sfdd8utuoUQzcP7n5dxffcNgRHnE/59t0Zv7557
vKxe7eTiiysZPFjuW9NamLlt8d85EUdJMcl33FLv9Q45xGL8eFi/3sHTT8vw6pYihY1oUnPn2tMc
+nzwxL92knXndVhOJyUPTgOnzOsu9s1/2wRCHTpxC1P44tnvWLBATuMLIZqWY+sWku+6FcvjwX/z
7Y3aVigEt93m5cknPRx6aJhJk6R7vrWpuOgSgsf0xrtgPt5X5tV7vbvugrQ0i4ce8lJQ0IwBil9J
YSOazLx5LkaOhKQkeHlOAX1njsG5YT3lY68m3L1HtMMT8SI5mdIHH8ZFmOeM0dx2rSVTQAshmk4o
RMpfLsGxcyelkyZjdurc4E2VlMCoUYk89ZSH3/8+zAsvlOPzNWGsIjY4HJQ88hhmcgopN1yDc/V3
9VotMxOuvz5AUZHBQw/JCISWIIWNaLSKCrjrLi/jxyeSmgrzn/mFAVPOxrtgPsFj++C/8dZohyji
THDAQMpHXUIPaxVTSy5jzF8SCMqsqUKIJpB039/wfLSCirOGUnHpXxq0DdO0O/P69k3iv/91MXBg
iIULy+jYUa6raa3CBx9KySOPY5SVkXrpSIyS4nqtd+mlQTp1Mnn6aTc//SSddM1NChvRKN9952DQ
IB8zZng4+GCTD2ev5YTbT8Gz4n0CQ86m8KXXkO4r0RCl9z1A5bF9+DMvMPjz+5k8WXq7hBCN41m8
CN+/pxL6XRdK/zWtQdM7r1zp4LTTfIwfn0h+vsENNwSYNauclJRmCFjElMohZ1E27hpca9eQcs24
es3l7PXCXXcFCAYN7r47QaZ/bmZS2IgG2bLF4KabvJwyMIHC1dt46rjpfJ3Tn8POPBSX/p6yMeMo
nvl/kJgY7VBFvPJ6KX5mDsH2nbiXu9j62ALmz5frbYQQDeOdN5fUKy/DSkig+KlZWCmp+7X+1q0G
48YlMGRIEl984WTo0CArVvi55ZZKXHJoOmD475xI5fF98b7xOr4pk+u1zllnhTj++BBvveVi4UL5
sDQnaV1RP2VluFe8z9ZlP7D9vTWg1zLB2sAMfsFLJXwYed0JJ1B8wcUEhv8pquGK1sHKyaFk9guk
nX4Ks8pHccHVr3DIISdyxBH1u1GaEEJQWkrKbTeS8OLzmMkplDw+k/AR3fdrEwsWuLj22gRKSgx6
9AgzeXKA3r1l5rMDkstF8YxnyBhyCkkPPQBOJ2U33bbXVQwDHnqogn79krj1Vi99+4bIyGiheA8w
UtiIOpUXB8mf8zYJr73CQV+9QULITzpwGGBiUJaai3FwdwLtOxDseSSBocPJOvJwAjtKoh26aEXC
hx9B6VPPknzRSF4KnMXN5z5JuxXDycyMdmRCiJhlWTi/+xZWLCNj5lO4fv6JYM9eFM94BvN3Xeq9
mUAAJk3yMnOmB5/P4h//qGDkyKBM8nmAs3JzKfzPG6SfcwZJ//g7OByU3bD3qaC7dLG46aZK7r3X
y6RJXqZOldnzmoMUNgKwL4RctcrB22+7+HqVwaGfv8TVOyfSkzUArKULr3nOxTzySNSZv6PXiIPw
pici908ULaHy5EEUv/o63hHn8a/8S3j05M2c/r/x5OREOzIhRNT4/TjX/Yxzw3qcG9fj2LwZx/Zt
OLZvx7nmB5ybfwHA6XBQNuYq/HdNAo+n3pvfudPgoosS+fRTJ0qFmTmzAqXkbLGwmR06UvifhaQP
PYOkKZMxKirw33rnXm9tMXZsJfPnu3j+eQ+nnRZi0CA569fUpLA5wG3ebPDvf3t47TUXO3Y4GMjb
/JMb6ckqQoaLd7texi+DR5M1qCd/6m7hleu3RZSE+hxHeMkS/IOHc9WmO3j/qBW0+fBxyEqPdmhC
iBbi/EHjWfoWnneW4v5oBUYd0yWa2dlUDBtBwvBz2HXU8ViZWfu1n7VrDf78Zx/r1jkYOjTIQw9V
kJTUFO9AtCZmx072mZuhQ/A9/CCuzz+l+LGZWLm5tb7e7YaHH67gjDN8XHllIm+8UUa3blIsNyUp
bA5QW7caTJ3qYfZsN5WVBodnbOK1jtdx3MaXsQyDiuHn4b/5dg4/6HccDoBM4yGiz/r9YZjvL+Wr
QWPpu/MNyo7ohuPOCZhXXiE3gBWitQqH8SxeROKMR/F8tOLXh4M9ehLqdRThTp0xO3Ui3K49Zm5b
zDa5kJAAQEJOCtZ+Do/+4AMnl16aSEGBwfXXB7jllsqGTJ4mDhBmx04ULH2XlGvG4n3rTTJP+iPF
jz1JsN+AWl/fvbvJtGkVXHFFIqNGJbJ4cRk5OfIdq6lIYXOAsSx47jk3Eyd68fsNftexkmeOmcYJ
Sybh2FhC8KhjKHngX3JDTRGzHB3bkbNqPo+cMY+RX95M1qSbKX9qBqGrxlJx/oVIt6oQrURlJQlz
Z+ObNhXnhnX2Q/1PomLYCCoHnFxnr3hDWRY8/bSbO+/0Yhjwr39VcOGFcgMtsW9WRibFz71A4oxH
SfrbBNJHnE1g8OnwjymQ+9sbwJ59dogffwzwwANeLrookRdfLCN1/ybpE3WQ6Z4PIOvXG5x7biI3
3ZSA0wlzxr2DTjmafq/eCC4nJf98mMI3lkpRI2Key20wYtF5TLl4NU9wBcamTaTcdiNZR3YjacLt
uL76sl73FxBCxKBQCO8Lc8g8/ihSbroWx/atlI+6hPz3VlI0bz6B8y9s8qKmsBCuvjqB225LICPD
4tVXy6WoEfvHMCi/cjyFi94m2Ps4vIsXQY8epIwfg+uLz36Tk264oZIRI4J89pmTs87ysXWrnBZs
ClLYHAAsC+bOddG/fxLvvefighPXsa7/SC54bCDu776m/IJR5K/4nIqLLgGHfCREfHC5YMqzubif
fpjuKeuYxASKSxz4pv+bjJNPJOOPR+P75/04flob7VCFEPURDuN96QUy+h5D6jVjcWzdQtkVV7Lr
k68pffBhwuqwJt+lZcFLL7k4/vgk5s1z07NnmKVLy+jTRy7qFg0T6nkkha8vpmjOPDjiCBLmzSVj
0AAyTuxN4rSpONavA+wpoB95pIJLLqnku++cnHGGjx9/lO9gjSUt2Mrt2mVw6aUJ/PWviWQZ+Xw2
8Dpmf3wYGa8/T+jw7hQsXErp1EexsrOjHaoQDTJkSIh5/0vmfwPuIjf0C2cznw/an4uxYSNJD9xH
Vp9epA8eQMJTMzCKCqMdrhCipmBwd0Fz1V9wblhvn6H5+Ev8kx9o8rMzAGVlMGeOm5NP9nHVVYn4
/QZ33hlg4cIy2reXs72ikQyDylMGw5dfUvT8S1ScPQznzz+RfM8Eso7pQcYJx5I06S4SVn7A/ff6
ue22ABs3Ojj1VB+vvipXiTSGYcXIcI0dO0piI5CInJwUdsTx/VgsC155xcWECV48O7fw93aPcEHx
DFylRYTbd8B/8+0ERpxPU98uOd7bLVqk3RqmZrstX+7knnu8rFrlJJkSJhzxMhe75pDz1TIM08Ty
+agYfh7ll15B+PAjohh5dO3t85aTkyLjIeoQrTwV68eHhsZnFBWSMOv/SJw5HefmX7BcLirOv5Cy
a2/E7PTb6xIaG1tBASxb5mLJEhdvv+2iuNjA4bAYMiTEhAkBOnVq+V9va/3dtpR4is8oyMe74DU8
SxfjWf4uRrl9wwwzLZ3KkwbyQeYQLpg7nO1lKYwaVck99wTw+VouvlhUV3x7y1NS2NQh1n/Ze/PT
Twa33eIh9L+PuNL5JOdZL+A0Q5jZ2ZSNv47yS6/4dcaYphbP7RZN0m4NU1u7mSa8+aaLRx/18Omn
9kxpJ3b9hXsOeYbjVj2J+5cNAFQOGEjZtTcS7HM8B9qUR1LYNIwUNrXbr/gsC/dHK/C++Dze1/6D
w1+K5Uui/IKRlI+5CrPzQU0WV0EBfP99Cm++WckHHzj55hsHlmV/vNu3NznvvCAXXRSkXbvoff1o
Vb/bKIjb+MrL8Xyw3J66fOlbODdtBCDsTWRJwpk8XnQh3x80iIemhendu/mGRcZr+0lh0wCx/suu
zQ/fhlk06SvS313A+bxARzYBEFKHUX7leCqG/6nZCpoq8dhusUDarWH21W4rVzqYPt3Dm2+6CIcN
UpNC3H30a4za9Qg53ywHIHhsH8quvo7KUwYdMNeYSWHTMK29sAmHQWsHn33m5KuvHOTnGxQVGQSD
kJoKaWkWubkmnTpZdO5s0rmzSYcOFu3a7SO+UAj3Jx/jWfoW3gXzcUauMQh36Ej56MupuGg0VnpG
o2IvLIQ1axx8/bWTVascfP65k++/3z0FvMdjcfTRYfr1C3PqqSG6dTNjoj8j1o/9El/j1Cs+y8L5
3bd4F76G99WXcP38EwBbaMszXIL/zxdz+eR2JCdHKb4oksKmCcX6LxvA2LaNouXfsGHBN3hXfkj3
/OWkUApAIDEN85yzCJz7J4J9T2yxHul4aLdYJO3WMPVtt61bDWbPdjN7tpvNm+3i5czsD5iU+Hd6
bXwDgFBXRdlVfyUwbASt/U60Utg0TGssbIJBeP99JwsWuFi0yEV+/v4V906nRceOBm3bhmjXzqJN
G4u81FIO83/OQVs/pt2GlbT5bjkev319WzjBR8FJZ5N/1kjKj+2Lw+XYIz2FwxAK2UtZmUF5Ofj9
BiUlBqWlUFhoUFBgkJ9vsH27wdatDjZtMti5c8+4fT6Lo44KM3Cgi+7dyzj66DCJiY1uriYX68d+
ia9x9js+y8K16gu88+bimvvir383yz0DqbhwFD0nno6R2HQd1PHafo0ubJRSjwCjgO3AJVrrFdWe
GwQ8BmQAj2qt79rXOrWJtcImO9tuzOaqB0wTduww2LLFYNs2u1espMTA79+9Qwcm6eWbySpeR3rB
epK2ryN951rSdvxEduEa0oM799jmem9XKv7Yj9xRAwgOPLnZz87UJtb/SGKVtFvD7G+7mSZ8+KGT
l192sWCBm+JigyP4mluc/+R883lcVohAciaBc4YRvuB8Qkcd0yqHqbXGwqY156mmPj6YJnzxhYNX
XnEzf77r16IgN9dkwIAwRx8dplevMG3bWqSmWrjdUFJiFxVbtjjY8LNJ/uodlP24BWvdJhJ3bCKz
+Ge68gOH8T2d2bDH/tbTiYUM4Q3OYBkDqKDpKgyv16JdO4uDDzY5+GCTbt3C9Oxp0rWridMZ+8dW
ia9xWnV85eUYr86n+MHn6LLpAwCKHOlsOm4Ybcechtm/X6O/58Vr+zWqsFFKnQwsAfoAY4CjtNY9
I88ZwAbgJWARsBToBWTXtU5dWjJhVFbC+vUO1qxxsHatwYYNDjZutHt9CgoMSksNKstC5LGFzp4t
tHdsobN3Cx3c28hyFpLhLCbNKMbrDOFwOXC4DCyvl0pfGsHENAK+dPyJ2ZR4MinxZFEQSmF7eQrb
ylLZts3Bzm0mu7abJIRKySSfTPLJYwsd2ERHNtKJDfyOn+nMerxU/ib+IC7WcRBrvd3Y3q4HKX88
HDWyJzlHtm+pJqxTrP+RxCppt4ZpTLsFg7BypZO333bxzjtOSlZv5mqmMYpZ5LEVgF2+Dmw75DhC
vfuQfkpPkrq2w8xpA273nhuzLIySYoyCAhw7d+DYsQPH9m0YBfk4Cgsxigox/KUQNjFM014lORkz
JQUrJQUzpw1mm1zMnFzM3FzM3LY051Wjra2waY15qrqcnBR2bCmwP1+7duLI34WRn49RWoLh99tL
OASGgWUY4HJjJSfbS0oKZmo6Wyoy+GpDBss+SWPhsjQ2b/cAkJ1tcvbZIc4+s5Le3QpxlhZjFBbi
2LEdx/ZtOLZtw7FtC87Nm3Fs3YxjyxYc27ZihGsf91+RlUdR7qFszu3JurxjWZPVm1+MDgQqHQQC
9pmYcBiCQQPT5Nelqv/A4bD/vFwui8RESEy08PkgNdUiJcUiLQ0yMizS0y3atjVJS9t730OsH1sl
vsY5UOLb9t4a9G1zOe6H2bRjCwABl4+dPfqR3K8n9PoDoSO627mjZn6qzrLA78eRvwtHQT4ZZgVF
G7fiKC7GKCmxE6Nl5ynL6cJKSrKX5BSsrCzMTHuxMjPB6ax7P02kuQqbe4FRWuvOSqnhwMtAltY6
Xyl1CPAjcJLWeplSqgSYAGTVtU5d+2lMwvj+ewdffOHANI3IAdMuXsyyAAetWkC4sJRAmUlJkUlp
QYhAcSVugvgoI5lSUighnUJynbvIcewk29xBZnhHQ8NpEhWp2fizO1OSfRDFWQdRkt2ZyvadCXbq
gvuQjhx0iKNZxls2VqwfZGKVtFvDNGW75efbhc4nH4Jz2TKO+3EOA8JLyWHPM6MmBqXuDHA4cBgW
DkwSAsU4rKa9wNNMTcPMycHKyMTMysJKS7e/qCYlY/l8WB4veNxYbo+dYBwOLLebyoGnYuXk7HXb
rbCwifk85Vi/DveK9+3C1jQjY66CGMEQBIMYFeUY5eUYZX6MkhKMokK7KC4swLVrJ1ZBAUYTDh0P
OdzgcuF0WHY8weA+t2+5XJht8zDz2hHOa4eZ1w6zQweSu3WlIDWbcJeDsVJi6/bpsX5slfga50CL
b/1PJv+d/AXexW9wWvB1FD/85jVl3nTKkrKxXG4MLBK8JolGwO58Ky6us1Nif1iGgZWRgZmVbeeo
9HSs1DSs1FSsRB9WYiJWog/cLiyXC1zu3XnK6STY90TMDh33uZ+GFDb1mes3FyiK/FwQ+bctkB95
jhrP52Gf7q9rnSY3blwC33zz28pxKIuYyKh6b8cyDazUdMysbOhwOBWZ2Zht2mLmtsVsE+lRTUvH
70yh2EqluNxNeZlFhd+ksjiAo6QYZ0kRbn8BvrJ8Est24ivLxxcuITFcSkKwFI/XwHA6sBwO+0tK
egZmRgZWdg7hdu0x23cg3K49VVVLUmTJa6K2EkLULjMTBg8OM3gwMOlEQqETWf2Dwdvv/oT53kck
/vgtCQVbSfFvJTO4EwMLCwMTB0V0o4AM8slkBzlspS3bacOUp5NJyEvHSk+3e7wc9oEd08Twl2KU
lOAoLrLP8vzaO75197JzJ8a6n/crEZWNvRr/pMnN11CxKebzVPIdN+Ndsni/1rGcTqz0dMjNJah+
j5WVjZmVjZmVaX+ZSE3jxTfS+c+SNEK4MLAwsPBQSQoldqedo4gOyUV0ycinQ1I+bZL9ZHj8OMr9
EA4TcjjAsItiKzUVKyUVKy3Nzndtcu2ziXl5hNu2s+93VssEG8k5KYRi+MulEK1F5y4OLn3qKCor
j2Llykk8M38HgY+/ImfDl3Qp/5Y2bCcnsIOcwA5chLAwqDAMEvM8mLltsQ7pipmaipWZhZmZia99
W0pcCfbffUoqeD1YhgMMAyMUxCgrs88IlxRj5O/CsSsfx66dGLt22mePd+3EWLvm15EI9VVxzjBK
nni2WdooZu4ClJHhw+Vq2GmtuXPhs8/s423VaWyvFxKMM/j+q5dIcVeQlOIgJV03tfAAAA9mSURB
VN2JM9EDHo/9oqQku4BIToa0NIyMDAyn89e7ltY1cjGzQVEeOHJyUqIdQlySdmuY5my3vDygXw+g
x6+PWZY9jWx+vr0UFkIgYC/uSsgNQ44JHTpA3sAmCMKyoLjY3pnfD6Wl9lJZaS+BwO4zAIBv0CB8
9WgT+bztv8bkKR5/FJYvt5NUpOcSt3v34vPtXlJTISMDIzkZIzLOylPHZs/5M/iW2JtzuSAxEVJS
7CUvD9q0aZERIzH9eYrl2EDia6wDNb6hQ2Ho0M5AZ+BMdu2C7dvtVLG+wE4NlZWgFGQfWfd2Gh2d
ado5qaDAzlXl5fYdcMvK7CFUVUtVnjJNEgYMIKGe7bK/7VefwmYLkB75uer29JurPQeQHhnHnBV5
rmIv69SqoKCsPvHWKjcXTj+9jiePGwRAkH10w1lA/u4YYv30ZqySdmsYabeGiWa7paXZy97saLIR
rQ5IzraX+tyEfR9tso+haA2IL+piPk+RkgNnDK//6yuACnuWy319zk89te7N5DfL+ac9xfLxK5Zj
A4mvsSS+PWVn20tNdeWipovPAF+mvdRXPfa7l6Foda5Tn3kd3wY6KqX6AEOAT4CAUipBa/0T8BNw
FnAa4MO+MPM362itC+uxLyGEEGJ/SZ4SQgix78JGa70ceAh7NpkjgXHAm8ALkZdcgZ0U/g+4Q2v9
bR3rCCGEEE1O8pQQQgiQG3TWKdZPb8YqabeGkXZrGGm3hmlts6K1lNZyH5umFsvxxXJsIPE1lsTX
OPEa397y1P7dYlgIIYQQQgghYpAUNkIIIYQQQoi4J4WNEEIIIYQQIu5JYSOEEEIIIYSIe1LYCCGE
EEIIIeKeFDZCCCGEEEKIuCeFjRBCCCGEECLuSWEjhBBCCCGEiHtS2AghhBBCCCHinhQ2QgghhBBC
iLgnhY0QQgghhBAi7klhI4QQQgghhIh7hmVZ0Y5BCCGEEEIIIRpFztgIIYQQQggh4p4UNkIIIYQQ
Qoi4J4WNEEIIIYQQIu5JYSOEEEIIIYSIe1LYCCGEEEIIIeKeFDZCCCGEEEKIuCeFjRBCCCGEECLu
uaIdQCxRSqUAs4CBwC/AWK31MqVUL+A5oBPwEnCF1lpuAFSNUmoc8C9grtZ6dOQxabd6UEo9AowC
tgOXaK1XRDmkmKWUGgY8DXypte6vlOoMvAgcDrwDnK+1Lo9mjLFGKeUEngSGA4XATcDHSLvFtFjP
R3Uc89cBnau9bKzWenpLxxaJJS5yklJqInB3tYc+1lr3iVI4e4jl3KSUGg08U+2hbVrrtlEK51ex
nqNqie9doF+1l0zRWt8ahbiaLE/JGZs93QAcid2InwKPRx6fBqwGTsT+Iz87KtHFKKXUZcA4YEeN
p6Td9kEpdTIwHhgEvA88Ft2IYlekraYCm6s9PBkIAz2BPsCYKIQW60YB5wG9gbnYSU3aLfbFbD7a
yzEf4EogJbLMbMm4qsRhTnqf3W02IMqxAHGTmzawu926RDmWmM9RdcQH8Hd2t+OElo4rosnylBQ2
e3oKOEFrvQHYBOQppbzAccCbWutVwA/EyIEnhnwKHAvsrHpA2q3e+gMbtdYrgUXAH5RSmdENKWZt
AHphf5aq9Afe1lqvBVYin7HavAn8QWv9PbAOSAKGIu0W62I5H/3mmF9NQGtdGllCLRxXlXjLSeFq
bRYrZ077E/u5yarWbmXRDobYz1G1xQdQWa0dK6MQFzRhnpKhaNVorTcCKKUOxq4M3wGysQvAosjL
CoC8qAQYoyJJAqVU9Yel3eonlz3bCKAtkB+dcGKX1voH+M3nrGb7HdbCYcU8rfU2YJtSKgu4BfgS
OAJpt5gWy/mojmN+lauVUncDXwFjtNZbWzI2iMucdKhS6ivAAu7QWi+MdkDER27KUEp9DKQC/9Ra
PxXNYGI9R9URH8BwpdQo7IJinNZat3BoTZqnDtjCRin1LHBxjYevwO6ZWApUANe1cFgxr65201pH
ZciBEGLfItdrLAZygBHAh9GNSFQXy/loP4/5L2N/OVoBvA7cg/0+YiW+qKoj1puAV7CvL7gemKOU
ahtDZ25i1RpgHjAdGAbMUEotjZzhFPW3GLvgfx2YDfwbOCUagTRVnjpgCxvgr0DNC6TKgf8CbqCf
1nqdUsqDPcYvPfKabODzFosy9tTWbkW1vG4H0m71sYU92wh+O/5V1K1m+0nb1aCUMoA5wKHAyVrr
T5VS0m6xJZbzUX2P+Witb6z6WSn1PvD7ZoyrSjzlpFpjrSpilFIvAqOB9thf3KMppnOT1vp97Gt/
UEr5gduBrtjDrWJJTB9rtdb3V/2slFoMjIxGHE2Zpw7YwkZrXUSNg59S6gbsi5ROBDYrpZIBP7Ac
OEMp9QX2H86NHKDqaLdMpVR7wAOkKKUOwe61k3bbt7eBu5RSfYAhwCda68IoxxSTIr05udhjbxMj
n7P/AqcqpWZhX3R4VxRDjFXDgDOxL8z8JnJck3aLIbGcj/bjmL8d+7h/P/aZm+OABc0Z237Gt44o
56Q6Yn1G2WODzsWezCCf2PhyHtO5SSk1CbgQe9bAYUAQ+C7KMcV0jqolvkOxz5C8AUzBbssvoxRe
k+UpmTxgT0MAJ/ABUBJZOmP3shyCPcZ5OvZFTmK3a4AfsXvnhkV+7oC02z5prZcDD2EPOTkSeyYf
Ubvh2J+tk7EvDP4RO/mawGeRn6M6xjpGDYn8+yK7j2vSbrEvlvNRbcf8TOBa7Jm0VmGfDZkYhdjq
ii9Wc9I92GeS1mAXsX+O4gXcv4qD3PQI9kXw3wGXY09HHe2zIbGeo2rG9wP273Vw5OcS7L+daGiy
PGVYltxWRAghhBBCCBHf5IyNEEIIIYQQIu5JYSOEEEIIIYSIe1LYCCGEEEIIIeKeFDZCCCGEEEKI
uCeFjRBCCCGEECLuHbD3sRGNo5Q6CPgZGKu1nl7t8b7Ae8AArfW7kbnI7wP6Y9+DIQF4Wms9rdo6
g7HnJ3dhT2+6GrhOa72zZd7N/lFKWdg3zRsJOLXWjZq+MdJGbwKXAL9gT2P5eyAEpAAPaK1fbFTQ
v93n5UBfrfXoptxute2/DDyhtV7SHNsXQoh9kTwleWof25c81QrJGRvRGD9iH+SquwTQ1f7/JPaN
s3pqrY/DvgHUiMgBC6VUD+Bx4DKtdW/gGOx56ec1c+yNprV+trHJImIKMFtrvQa4HijTWvfVWvcH
zgHuiCSVeDIGeCwO4xZCtC6SpyRP1UXyVCskZ2xEY2wGEpRSh2utv1VK+YATgI8AIndT7gt00Vqb
AFrrfKXUeOw73c4EbgamaK2/jzxvKaWmAI/V3Fmkl20KEAB8wDit9edKqWcjsXTHvpv0U1rrB5RS
ScATQEfsnqvntNaPK6VGY9+QysC+8dhs7DtUD4g8drLW2q+U+ht2ggPYBIzUWgerxTMRcGmt71RK
DQDujqwfBK7QWv+slLofOCkS8y/AxVrrQLVttMG+adZ1kYcyse+UbWitLa31RqCHUsqplNoMHKO1
/iWy7o/AWZH39mDkXzcwXmv9hVLqXey7CPeKxDAG+2ZcGyPtVRXDOuybYnUBbgLe11p3qOU9hrBv
JjcASAZGa62/qeM97lJKLcS+cdrUmr9LIYRoIZKnJE9JnjqAyBkb0VizgEsjPw/HvkuxGfl/T+DL
6gdZAK31V0BG5GB5OPBJjedNrXVRLfvKxh5ScBLwMHB7tee6aK3PBE4F7og8dg1QqLU+EfuAdotS
qkvkuaOBi4BTgAnAUq318dgHvVOUUi6gDDhBa/1HIB0YVFsDRBLldGCY1rofMA34p1IqA7gKOE5r
fQLwKpBbY/WBwHvV7jT9MHZv4M9KqZlKqRFKKY/WOozdOzg8ss+jgCKt9WpgDnBlpOdsHHYirlIa
iSkZ+2DfT2t9WqQtq/tRaz2itvdXjRP4JrKfx4G/7eM9LsVOzEIIEU2SpyRPSZ46QEhhIxrrReBP
kQPsaOxepSp+9v4ZM4Ew9oGoPrZiH4iXA7ey50HvXQCt9XogVSnlBHpjH7TQWpcDn2L3fAF8GumR
2hSJ8f3I45uANK11KBLbe0qp/2Env5oH2SpHAHnAq5HepxuBHK11AfAW8D+l1A3ACq31hhrrdsTu
mSIS5wagB/AnYE1kW18rpVKxE8O5kZeeB8yOJF0FPBXZ98OR91/V7isi/x4CrNNa74r8f1mNOFZQ
P29F/v0A6LaP97geOKie2xVCiOYieUrylOSpA4QUNqJRIhdOfg5cBuRprT+t9vQ3QE+llLf6Okqp
bsC2yLpfA3+suV2lVJ9adjcLuD/Ss3VHjedCNf5vANZeHtvj9ZEE8evrlFJ/xO7hOzXSk/ReLfFU
CQAbtNb9I8sJkRjRWp+LfZob7INqz71sB6VUYmS9lVrr+4E+wA7sYQefAG2UUnnAMGBuZN+Bavvu
r7U+tGpIBVDVw2awu4cSfpukq15Xs808Nf5fdcz4tS339z0KIURLkjwFSJ6SPHWAkMJGNIVZ2DPK
zK3+oNZ6HfA28GBVz0ykR2ca9uwyAA8ANyil/lC1nlLqRuDeWvaTC3wb6eUaAXhreU11HxE5LR8Z
x3wU8Fk931Muds+RXynVGfvAXdf+fgCylVJHRPZ1olLqL0qpLkqp67TW32utH8Q+/f2HGutuxO4N
q/IO9tCDKsnYPXA/Rf7/Anbb/aC13hYZCrFOKXV6ZN9dlVITaolxLdBFKZWulDLYPSa7pmIgUynl
i7TziTWePynyb1/gq328x87Aujr2I4QQLUnylOQpyVMHAJk8QDSFBdgXP86p5bnLgYnAl0opP/ZF
g09orZ8H0FqvVkoNAx6N9JgFgS+wZ1mpaQr2AXU98A9gllLq2r3ENQ14IjIkwAv8TWu9zr5WdJ+W
YCey94FvI+9hglKq5qlxtNblSqmR2KfZKyIP/wV7uEAvpdRKoAQoACbVWP2/wENKKXdkjPefgYeV
UmOACiARu/fvy8jr52BPM1o9qVwEPKKUuhW7fa+vJcYCpdRk7B69n7EP5L46Xvcs9nCINdi/i+p6
KaXGAhmR/e7tPZ4MLK65DyGEiALJU5KnJE8dAAzLqnlGTwjRkpRSjwKrtNZPRDuWvVGR+yLUGA5R
12uzgI+BXlrrkmYPTgghRLORPCXihQxFEyL6bgFGKaUOjnYgTWgG9jSnkiyEECL+SZ4ScUHO2Agh
hBBCCCHinpyxEUIIIYQQQsQ9KWyEEEIIIYQQcU8KGyGEEEIIIUTck8JGCCGEEEIIEfeksBFCCCGE
EELEvf8Hc5Dn1nAZ8YIAAAAASUVORK5CYII=
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Model-comparison">Model comparison<a class="anchor-link" href="#Model-comparison">&#182;</a></h2><p>There are clearly similar issues with the Student-t fit as with the Gaussian fit.  We can get a better sense of whether the Student-t model has improved by comparing them directly.  First, we define a revised plotting function to compare the models.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[20]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">compare_models</span><span class="p">(</span><span class="n">train_data</span><span class="p">,</span> <span class="n">test_data</span><span class="p">,</span> <span class="n">models</span><span class="p">,</span> <span class="n">axkwargs</span> <span class="o">=</span> <span class="kc">None</span><span class="p">):</span>
    <span class="sd">&quot;&quot;&quot;Compare the fits of the various models against the data</span>
<span class="sd">    </span>
<span class="sd">    models is a list of dictionaries</span>
<span class="sd">    models[i] = {&#39;train_data&#39;:train_data, &#39;test_data&#39;:test_data, &#39;name&#39;:name, &#39;color&#39;:color}</span>
<span class="sd">    axkwargs is a list of dictionaries with keyword properties for each axis.&quot;&quot;&quot;</span>
    <span class="n">fig</span><span class="p">,</span> <span class="n">ax</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">(</span><span class="n">nrows</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span> <span class="n">ncols</span> <span class="o">=</span> <span class="mi">2</span><span class="p">,</span> <span class="n">figsize</span> <span class="o">=</span> <span class="p">(</span><span class="mi">16</span><span class="p">,</span><span class="mi">7</span><span class="p">))</span>
    <span class="n">sns</span><span class="o">.</span><span class="n">kdeplot</span><span class="p">(</span><span class="n">train_data</span><span class="p">,</span> <span class="n">color</span> <span class="o">=</span> <span class="s1">&#39;b&#39;</span><span class="p">,</span><span class="n">ax</span> <span class="o">=</span> <span class="n">ax</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">label</span> <span class="o">=</span> <span class="s1">&#39;Training data&#39;</span><span class="p">)</span>
    <span class="k">for</span> <span class="n">model</span> <span class="ow">in</span> <span class="n">models</span><span class="p">:</span>
        <span class="n">sns</span><span class="o">.</span><span class="n">kdeplot</span><span class="p">(</span><span class="n">model</span><span class="p">[</span><span class="s1">&#39;train_data&#39;</span><span class="p">],</span><span class="n">color</span> <span class="o">=</span> <span class="n">model</span><span class="p">[</span><span class="s1">&#39;color&#39;</span><span class="p">],</span><span class="n">ax</span> <span class="o">=</span> <span class="n">ax</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">label</span> <span class="o">=</span> <span class="n">model</span><span class="p">[</span><span class="s1">&#39;name&#39;</span><span class="p">])</span>
    <span class="n">ax</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">legend</span><span class="p">()</span>
    <span class="k">if</span> <span class="n">axkwargs</span><span class="p">:</span>
        <span class="n">ax</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="o">**</span><span class="n">axkwargs</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>

    <span class="n">sns</span><span class="o">.</span><span class="n">kdeplot</span><span class="p">(</span><span class="n">test_data</span><span class="p">,</span> <span class="n">color</span> <span class="o">=</span> <span class="s1">&#39;b&#39;</span><span class="p">,</span><span class="n">ax</span> <span class="o">=</span> <span class="n">ax</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="n">label</span> <span class="o">=</span> <span class="s1">&#39;Test data&#39;</span><span class="p">)</span>
    <span class="k">for</span> <span class="n">model</span> <span class="ow">in</span> <span class="n">models</span><span class="p">:</span>
        <span class="n">sns</span><span class="o">.</span><span class="n">kdeplot</span><span class="p">(</span><span class="n">model</span><span class="p">[</span><span class="s1">&#39;test_data&#39;</span><span class="p">],</span><span class="n">color</span> <span class="o">=</span> <span class="n">model</span><span class="p">[</span><span class="s1">&#39;color&#39;</span><span class="p">],</span><span class="n">ax</span> <span class="o">=</span> <span class="n">ax</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="n">label</span> <span class="o">=</span> <span class="n">model</span><span class="p">[</span><span class="s1">&#39;name&#39;</span><span class="p">])</span>
    <span class="k">if</span> <span class="n">axkwargs</span><span class="p">:</span>
        <span class="n">ax</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="o">**</span><span class="n">axkwargs</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>And we can use this to compare the models and data below.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[21]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">models</span> <span class="o">=</span> <span class="p">[{</span><span class="s1">&#39;train_data&#39;</span><span class="p">:</span><span class="n">train_samples</span><span class="p">[</span><span class="s1">&#39;Y_obs&#39;</span><span class="p">][:,</span><span class="mi">0</span><span class="p">],</span> <span class="s1">&#39;test_data&#39;</span><span class="p">:</span><span class="n">train_samples</span><span class="p">[</span><span class="s1">&#39;Y_obs&#39;</span><span class="p">][:,</span><span class="mi">0</span><span class="p">],</span> <span class="s1">&#39;name&#39;</span><span class="p">:</span><span class="s1">&#39;Gaussian&#39;</span><span class="p">,</span> <span class="s1">&#39;color&#39;</span><span class="p">:</span> <span class="s1">&#39;red&#39;</span> <span class="p">},</span> 
         <span class="p">{</span><span class="s1">&#39;train_data&#39;</span><span class="p">:</span><span class="n">train_samples_student</span><span class="p">[</span><span class="s1">&#39;Y_obs&#39;</span><span class="p">][:,</span><span class="mi">0</span><span class="p">],</span> <span class="s1">&#39;test_data&#39;</span><span class="p">:</span><span class="n">train_samples_student</span><span class="p">[</span><span class="s1">&#39;Y_obs&#39;</span><span class="p">][:,</span><span class="mi">0</span><span class="p">],</span> <span class="s1">&#39;name&#39;</span><span class="p">:</span><span class="s1">&#39;Student-T&#39;</span><span class="p">,</span> <span class="s1">&#39;color&#39;</span><span class="p">:</span> <span class="s1">&#39;green&#39;</span> <span class="p">}]</span>
<span class="n">axkwargs</span> <span class="o">=</span> <span class="p">[</span>
    <span class="p">{</span><span class="s1">&#39;title&#39;</span> <span class="p">:</span> <span class="s1">&#39;Training period&#39;</span><span class="p">,</span> <span class="s1">&#39;xlabel&#39;</span><span class="p">:</span> <span class="s1">&#39;Sverdrups&#39;</span><span class="p">,</span> <span class="s1">&#39;ylabel&#39;</span><span class="p">:</span> <span class="s1">&#39;Probability&#39;</span><span class="p">},</span>
    <span class="p">{</span><span class="s1">&#39;title&#39;</span> <span class="p">:</span> <span class="s1">&#39;Testing period&#39;</span><span class="p">,</span> <span class="s1">&#39;xlabel&#39;</span><span class="p">:</span> <span class="s1">&#39;Sverdrups&#39;</span><span class="p">,</span> <span class="s1">&#39;ylabel&#39;</span><span class="p">:</span> <span class="s1">&#39;Probability&#39;</span><span class="p">}]</span>
<span class="n">compare_models</span><span class="p">(</span><span class="n">train_data</span><span class="o">=</span><span class="n">moc_anomalies_train</span><span class="p">,</span> <span class="n">test_data</span> <span class="o">=</span> <span class="n">moc_anomalies_test</span><span class="p">,</span> 
               <span class="n">models</span> <span class="o">=</span> <span class="n">models</span><span class="p">,</span> <span class="n">axkwargs</span> <span class="o">=</span> <span class="n">axkwargs</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

<div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 id="Conclusion">Conclusion<a class="anchor-link" href="#Conclusion">&#182;</a></h2><p>This comparison shows that the Student-t fit has improved the fit over the Gaussian model in both the training and test periods.  The presence of the extreme negative values in 2009/2010 will always lead to problems when trying to fit a symmetrical distribution to the data.</p>
<p>The question then is whether corresponding extreme positive values can occur but the sampling period has not been long enough to observe them, or whether such extreme negative values are indicative that the ocean circulation is non-stationary and undergoing significant shifts in time.</p>
<p>This workbook shows an example of fitting models to a dataset.  The next workbook will show how Bayesian inference can be used to account for uncertainty in time-series forecasting.</p>

</div>
</div>
</div>
    </div>
  </div>
</body>

 


</html>
