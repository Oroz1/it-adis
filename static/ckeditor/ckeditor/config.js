/**
 * @license Copyright (c) 2003-2021, CKSource - Frederico Knabben. All rights reserved.
 * For licensing, see https://ckeditor.com/legal/ckeditor-oss-license
 */

CKEDITOR.editorConfig = function( config ) {
	config.language = 'ru';
	config.startupMode = 'source'; // режим Источник
	config.toolbar = 'MyToolbar'; // пользовательская панель
	config.indentClasses = ["ul-grey", "ul-red", "text-red", "ul-content-red", "circle", "style-none", "decimal", "paragraph-portfolio-top", "ul-portfolio-top", "url-portfolio-top", "text-grey"];
	config.protectedSource.push(/<(style)[^>]*>.*<\/style>/ig);
	config.protectedSource.push(/<(script)[^>]*>.*<\/script>/ig);// разрешить теги
	config.protectedSource.push(/<(iframe)[^>]*>.*<\/iframe>/ig);
	config.protectedSource.push(/<(input)[^>]*>/ig);
	config.extraAllowedContent = 'iframe [*]{*}(*);';
	config.allowedContent = true;
	config.allowedContentRules = true;
};
	