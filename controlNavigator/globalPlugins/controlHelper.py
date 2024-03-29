﻿# -*- coding: UTF-8 -*-
# ControlHelper main implementation file
# Written by: Yukio Nozawa <personal@nyanchangames.com>
# Released under GPL(See ../COPYING.txt for license)

import itertools

import api
import browseMode
import config
import globalPluginHandler
import eventHandler
from controlTypes import *
import speech
import tones
from globalCommands import commands
from scriptHandler import executeScript

FOCUS_MODE=0
BROWSE_MODE=1

controlNames={}
controlNames[ROLE_UNKNOWN]=u"サポートされていないコントロール"
controlNames[ROLE_WINDOW]=u"ウィンドウ"
controlNames[ROLE_TITLEBAR]=u"タイトルバー"
controlNames[ROLE_PANE]=u"ペイン"
controlNames[ROLE_DIALOG]=u"ダイアログ"
controlNames[ROLE_CHECKBOX]=u"チェックボックス"
controlNames[ROLE_RADIOBUTTON]=u"ラジオボタン"
controlNames[ROLE_STATICTEXT]=u"テキスト"
controlNames[ROLE_EDITABLETEXT]=u"編集可能なテキスト"
controlNames[ROLE_BUTTON]=u"ボタン"
controlNames[ROLE_MENUBAR]=u"メニューバー"
controlNames[ROLE_MENUITEM]=u"メニュー項目"
controlNames[ROLE_POPUPMENU]=u"ポップアップメニュー"
controlNames[ROLE_COMBOBOX]=u"コンボボックス"
controlNames[ROLE_LIST]=u"リスト"
controlNames[ROLE_LISTITEM]=u"リストアイテム"
controlNames[ROLE_GRAPHIC]=u"画像"
controlNames[ROLE_HELPBALLOON]=u"ヘルプバルーン"
controlNames[ROLE_TOOLTIP]=u"ツールチップ"
controlNames[ROLE_LINK]=u"リンク"
controlNames[ROLE_TREEVIEW]=u"ツリービュー"
controlNames[ROLE_TREEVIEWITEM]=u"ツリービューアイテム"
controlNames[ROLE_TAB]=u"タブ"
controlNames[ROLE_TABCONTROL]=u"タブコントロール"
controlNames[ROLE_SLIDER]=u"スライダー"
controlNames[ROLE_PROGRESSBAR]=u"プログレスバー"
controlNames[ROLE_SCROLLBAR]=u"スクロールバー"
controlNames[ROLE_STATUSBAR]=u"ステータスバー"
controlNames[ROLE_TABLE]=u"テーブル"
controlNames[ROLE_TABLECELL]=u"テーブルセル"
controlNames[ROLE_TABLECOLUMN]=u"テーブル列"
controlNames[ROLE_TABLEROW]=u"テーブル業"
controlNames[ROLE_TABLECOLUMNHEADER]=u"テーブル列ヘッダー"
controlNames[ROLE_TABLEROWHEADER]=u"テーブル行ヘッダー"
controlNames[ROLE_FRAME]=u"フレーム"
controlNames[ROLE_TOOLBAR]=u"ツールバー"
controlNames[ROLE_DROPDOWNBUTTON]=u"ドロップダウンボタン"
controlNames[ROLE_CLOCK]=u"時計"
controlNames[ROLE_SEPARATOR]=u"セパレータ"
controlNames[ROLE_FORM]=u"フォーム"
controlNames[ROLE_HEADING]=u"見出し"
controlNames[ROLE_HEADING1]=u"見出しレベル1"
controlNames[ROLE_HEADING2]=u"見出しレベル2"
controlNames[ROLE_HEADING3]=u"見出しレベル3"
controlNames[ROLE_HEADING4]=u"見出しレベル4"
controlNames[ROLE_HEADING5]=u"見出しレベル5"
controlNames[ROLE_HEADING6]=u"見出しレベル6"
controlNames[ROLE_PARAGRAPH]=u"段落"
controlNames[ROLE_BLOCKQUOTE]=u"引用"
controlNames[ROLE_TABLEHEADER]=u"テーブルヘッダー"
controlNames[ROLE_TABLEBODY]=u"テーブルボディー"
controlNames[ROLE_TABLEFOOTER]=u"テーブルフッター"
controlNames[ROLE_DOCUMENT]=u"ドキュメント"
controlNames[ROLE_ANIMATION]=u"アニメーション"
controlNames[ROLE_APPLICATION]=u"アプリケーション"
controlNames[ROLE_BOX]=u"ボックス"
controlNames[ROLE_GROUPING]=u"グループボックス"
controlNames[ROLE_PROPERTYPAGE]=u"プロパティページ"
controlNames[ROLE_CANVAS]=u"カンバス"
controlNames[ROLE_CAPTION]=u"キャプション"
controlNames[ROLE_CHECKMENUITEM]=u"チェックメニューアイテム"
controlNames[ROLE_DATEEDITOR]=u"日付コントロール"
controlNames[ROLE_ICON]=u"アイコン"
controlNames[ROLE_DIRECTORYPANE]=u"ディレクトリペーン"
controlNames[ROLE_EMBEDDEDOBJECT]=u"埋め込みオブジェクト"
controlNames[ROLE_ENDNOTE]=u"エンドノート"
controlNames[ROLE_FOOTER]=u"フッター"
controlNames[ROLE_FOOTNOTE]=u"フットノート"
controlNames[ROLE_GLASSPANE]=u"グラスペーン"
controlNames[ROLE_HEADER]=u"ヘッダー"
controlNames[ROLE_IMAGEMAP]=u"イメージマップ"
controlNames[ROLE_INPUTWINDOW]=u"入力ウィンドウ"
controlNames[ROLE_LABEL]=u"ラベル"
controlNames[ROLE_NOTE]=u"ノート"
controlNames[ROLE_PAGE]=u"ページ"
controlNames[ROLE_RADIOMENUITEM]=u"ラジオメニューアイテム"
controlNames[ROLE_LAYEREDPANE]=u"レイヤードペーン"
controlNames[ROLE_REDUNDANTOBJECT]=u"リダンダントオブジェクト"
controlNames[ROLE_ROOTPANE]=u"ルートペーン"
controlNames[ROLE_EDITBAR]=u"エディットバー"
controlNames[ROLE_TERMINAL]=u"ターミナル"
controlNames[ROLE_RICHEDIT]=u"リッチエディット"
controlNames[ROLE_RULER]=u"ルーラー"
controlNames[ROLE_SCROLLPANE]=u"スクロールペーン"
controlNames[ROLE_SECTION]=u"セクション"
controlNames[ROLE_SHAPE]=u"シェイプ"
controlNames[ROLE_SPLITPANE]=u"スプリットペーン"
controlNames[ROLE_VIEWPORT]=u"ビューポート"
controlNames[ROLE_TEAROFFMENU]=u"ティアオフメニュー"
controlNames[ROLE_TEXTFRAME]=u"テキストフレーム"
controlNames[ROLE_TOGGLEBUTTON]=u"トグルボタン"
controlNames[ROLE_BORDER]=u"ボーダー"
controlNames[ROLE_CARET]=u"キャレット"
controlNames[ROLE_CHARACTER]=u"キャラクター"
controlNames[ROLE_CHART]=u"チャート"
controlNames[ROLE_CURSOR]=u"カーソル"
controlNames[ROLE_DIAGRAM]=u"ダイアグラム"
controlNames[ROLE_DIAL]=u"ダイアル"
controlNames[ROLE_DROPLIST]=u"ドロップダウンリスト"
controlNames[ROLE_SPLITBUTTON]=u"スプリットボタン"
controlNames[ROLE_MENUBUTTON]=u"メニューボタン"
controlNames[ROLE_DROPDOWNBUTTONGRID]=u"ドロップダウングリッド"
controlNames[ROLE_MATH]=u"数学"
controlNames[ROLE_EQUATION]=u"数式"
controlNames[ROLE_GRIP]=u"グリップ"
controlNames[ROLE_HOTKEYFIELD]=u"ホットキー入力"
controlNames[ROLE_INDICATOR]=u"インジケーター"
controlNames[ROLE_SPINBUTTON]=u"スピンボタン"
controlNames[ROLE_SOUND]=u"サウンド"
controlNames[ROLE_WHITESPACE]=u"ホワイトスペース"
controlNames[ROLE_TREEVIEWBUTTON]=u"ツリービューボタン"
controlNames[ROLE_IPADDRESS]=u"IPアドレス"
controlNames[ROLE_DESKTOPICON]=u"デスクトップアイコン"
controlNames[ROLE_ALERT]=u"アラート"
controlNames[ROLE_INTERNALFRAME]=u"内部フレーム"
controlNames[ROLE_DESKTOPPANE]=u"デスクトップペーン"
controlNames[ROLE_OPTIONPANE]=u"オプションペーン"
controlNames[ROLE_COLORCHOOSER]=u"色選択"
controlNames[ROLE_FILECHOOSER]=u"ファイル選択"
controlNames[ROLE_FILLER]=u"フィラー"
controlNames[ROLE_MENU]=u"メニュー"
controlNames[ROLE_PANEL]=u"パネル"
controlNames[ROLE_PASSWORDEDIT]=u"パスワード入力"
controlNames[ROLE_FONTCHOOSER]=u"フォント選択"
controlNames[ROLE_LINE]=u"行"
controlNames[ROLE_FONTNAME]=u"フォント名"
controlNames[ROLE_FONTSIZE]=u"フォントサイズ"
controlNames[ROLE_BOLD]=u"ボールド"
controlNames[ROLE_ITALIC]=u"イタリック"
controlNames[ROLE_UNDERLINE]=u"アンダーライン"
controlNames[ROLE_FGCOLOR]=u"フォアグラウンドカラー"
controlNames[ROLE_BGCOLOR]=u"バックグラウンドカラー"
controlNames[ROLE_SUPERSCRIPT]=u"スーパースクリプト"
controlNames[ROLE_SUBSCRIPT]=u"サブスクリプト"
controlNames[ROLE_STYLE]=u"スタイル"
controlNames[ROLE_INDENT]=u"インデント"
controlNames[ROLE_ALIGNMENT]=u"アラインメント"
controlNames[ROLE_ALERT]=u"アラート"
controlNames[ROLE_DATAGRID]=u"データグリッド"
controlNames[ROLE_DATAITEM]=u"データアイテム"
controlNames[ROLE_HEADERITEM]=u"ヘッドアイテム"
controlNames[ROLE_THUMB]=u"サム"
controlNames[ROLE_CALENDAR]=u"カレンダーコントロール"
controlNames[ROLE_VIDEO]=u"ビデオコントロール"
controlNames[ROLE_AUDIO]=u"オーディオコントロール"
controlNames[ROLE_CHARTELEMENT]=u"チャート要素"
controlNames[ROLE_DELETED_CONTENT]=u"削除済みコンテンツ"
controlNames[ROLE_INSERTED_CONTENT]=u"追加済みコンテンツ"

controlGuides={}
controlGuides[ROLE_UNKNOWN]=u"おそらく、読み上げに対応していません。"
controlGuides[ROLE_WINDOW]=u""
controlGuides[ROLE_TITLEBAR]=u""
controlGuides[ROLE_PANE]=u""
controlGuides[ROLE_DIALOG]=u""
controlGuides[ROLE_CHECKBOX]=u"チェックの状態を切り替えるには、スペースキーを押します。"
controlGuides[ROLE_RADIOBUTTON]=u"上下矢印キーを押して、一つの項目を選択します。"
controlGuides[ROLE_STATICTEXT]=u""
controlGuides[ROLE_EDITABLETEXT]={
	"focus": u"テキストを編集するには、そのまま入力します。前後のコントロールに移動するには、タブキー、または、シフト+タブキーを押します。この領域を抜けて、周りの文章を読むには、インサートキー+スペースキーを押してから、上下の矢印キーを押します。",
	"browse": u"テキストを編集するには、スペースキーを押してから入力します。前後のコントロールに移動するには、タブキー、または、シフト+タブキーを押します。周りの文章を読むには、上下の矢印キーを押します。"
}
controlGuides[ROLE_BUTTON]=u"このボタンを押すには、スペースキーを押します。"
controlGuides[ROLE_MENUBAR]=u""
controlGuides[ROLE_MENUITEM]=u"上下左右の矢印キーで項目を選択します。決定するには、エンターキーを押します。なにも選択せずにメニューを閉じるには、エスケープキーを押します。"
controlGuides[ROLE_POPUPMENU]=u"上下の矢印キーで項目を選択します。決定するには、エンターキーを押します。"
controlGuides[ROLE_COMBOBOX]=u"上下の矢印キーで項目を選択します。"
controlGuides[ROLE_LIST]=u"上下の矢印キーで項目を選択します。"
controlGuides[ROLE_LISTITEM]=u"上下の矢印キーで項目を選択します。"
controlGuides[ROLE_GRAPHIC]=u""
controlGuides[ROLE_HELPBALLOON]=u""
controlGuides[ROLE_TOOLTIP]=u""
controlGuides[ROLE_LINK]=u"このリンクをクリックするには、エンターキーを押します。次のリンクやボタンに移動するには、タブキーを押します。ここからテキストを読むには、下矢印キーで読み進めるか、インサートキーを押しながら、Aキーを押します。"
controlGuides[ROLE_TREEVIEW]=u"上下の矢印キーで項目を選択します。アイテムを展開するには右矢印キーを使い、折りたたむには左矢印キーを押します。"
controlGuides[ROLE_TREEVIEWITEM]=u""
controlGuides[ROLE_TAB]=u""
controlGuides[ROLE_TABCONTROL]=u"左右の矢印キーで、タブを切り替えます。また、コントロールキーを押しながらタブキーを押すことでも、順番に切り替えられます。"
controlGuides[ROLE_SLIDER]=u"上下の矢印キーで、値を調整します。"
controlGuides[ROLE_PROGRESSBAR]=u""
controlGuides[ROLE_SCROLLBAR]=u""
controlGuides[ROLE_STATUSBAR]=u""
controlGuides[ROLE_TABLE]=u"テーブルのなかを上下左右に移動するには、コントロールキーとオルトキーを押しながら、上下左右の矢印キーを押します。"
controlGuides[ROLE_TABLECELL]=u"テーブルのなかを上下左右に移動するには、コントロールキーとオルトキーを押しながら、上下左右の矢印キーを押します。"
controlGuides[ROLE_TABLECOLUMN]=u"テーブルのなかを上下左右に移動するには、コントロールキーとオルトキーを押しながら、上下左右の矢印キーを押します。"
controlGuides[ROLE_TABLEROW]=u"テーブルのなかを上下左右に移動するには、コントロールキーとオルトキーを押しながら、上下左右の矢印キーを押します。"
controlGuides[ROLE_TABLECOLUMNHEADER]=u"テーブルのなかを上下左右に移動するには、コントロールキーとオルトキーを押しながら、上下左右の矢印キーを押します。"
controlGuides[ROLE_TABLEROWHEADER]=u"テーブルのなかを上下左右に移動するには、コントロールキーとオルトキーを押しながら、上下左右の矢印キーを押します。"
controlGuides[ROLE_FRAME]=u""
controlGuides[ROLE_TOOLBAR]=u""
controlGuides[ROLE_DROPDOWNBUTTON]=u"メニュー項目を表示するには、エンターキーを押します。"
controlGuides[ROLE_CLOCK]=u"現在時刻は、{インサートキーを押しながらファンクション12キーを押すと、いつでも確認できます。"
controlGuides[ROLE_SEPARATOR]=u""
controlGuides[ROLE_FORM]=u""
controlGuides[ROLE_HEADING]=u"次の見出しに移動するには、hキーを押します。前の見出しに移動するには、shiftキーを押しながら、hキーを押します。"
controlGuides[ROLE_HEADING1]=u""
controlGuides[ROLE_HEADING2]=u""
controlGuides[ROLE_HEADING3]=u""
controlGuides[ROLE_HEADING4]=u""
controlGuides[ROLE_HEADING5]=u""
controlGuides[ROLE_HEADING6]=u""
controlGuides[ROLE_PARAGRAPH]=u"文章を読むには、上下左右の矢印キーを押します。自動的に読み進めるには、インサートキーを押しながら、Aキーを押します。"
controlGuides[ROLE_BLOCKQUOTE]=u""
controlGuides[ROLE_TABLEHEADER]=u""
controlGuides[ROLE_TABLEBODY]=u""
controlGuides[ROLE_TABLEFOOTER]=u""
controlGuides[ROLE_DOCUMENT]=u"内容を読むには、上下矢印キーを押して読み進めるか、{インサートキーを押しながら、Aキーを押します。"
controlGuides[ROLE_ANIMATION]=u""
controlGuides[ROLE_APPLICATION]=u""
controlGuides[ROLE_BOX]=u""
controlGuides[ROLE_GROUPING]=u""
controlGuides[ROLE_PROPERTYPAGE]=u""
controlGuides[ROLE_CANVAS]=u""
controlGuides[ROLE_CAPTION]=u""
controlGuides[ROLE_CHECKMENUITEM]=u"このメニュー項目は、確定するたびにチェック状態が切り替わります。"
controlGuides[ROLE_DATEEDITOR]=u""
controlGuides[ROLE_ICON]=u"オルトキーを押しながらタブキーを押すことで、アクティブなウィンドウを巡回します。オルトキーを話すと、その時点で選んでいたウィンドウが選択されます。"
controlGuides[ROLE_DIRECTORYPANE]=u""
controlGuides[ROLE_EMBEDDEDOBJECT]=u"ここでエンターキーを押すと、オブジェクトを操作できるかもしれません。"
controlGuides[ROLE_ENDNOTE]=u""
controlGuides[ROLE_FOOTER]=u""
controlGuides[ROLE_FOOTNOTE]=u""
controlGuides[ROLE_GLASSPANE]=u""
controlGuides[ROLE_HEADER]=u""
controlGuides[ROLE_IMAGEMAP]=u""
controlGuides[ROLE_INPUTWINDOW]=u""
controlGuides[ROLE_LABEL]=u""
controlGuides[ROLE_NOTE]=u""
controlGuides[ROLE_PAGE]=u""
controlGuides[ROLE_RADIOMENUITEM]=u""
controlGuides[ROLE_LAYEREDPANE]=u""
controlGuides[ROLE_REDUNDANTOBJECT]=u""
controlGuides[ROLE_ROOTPANE]=u""
controlGuides[ROLE_EDITBAR]=u""
controlGuides[ROLE_TERMINAL]=u"ターミナルに入力するには、そのまま入力します。出力を読むには、{インサートキーを押しながら、上下矢印キーを押します。"
controlGuides[ROLE_RICHEDIT]=u""
controlGuides[ROLE_RULER]=u""
controlGuides[ROLE_SCROLLPANE]=u""
controlGuides[ROLE_SECTION]=u""
controlGuides[ROLE_SHAPE]=u""
controlGuides[ROLE_SPLITPANE]=u""
controlGuides[ROLE_VIEWPORT]=u""
controlGuides[ROLE_TEAROFFMENU]=u""
controlGuides[ROLE_TEXTFRAME]=u""
controlGuides[ROLE_TOGGLEBUTTON]=u""
controlGuides[ROLE_BORDER]=u""
controlGuides[ROLE_CARET]=u""
controlGuides[ROLE_CHARACTER]=u""
controlGuides[ROLE_CHART]=u""
controlGuides[ROLE_CURSOR]=u""
controlGuides[ROLE_DIAGRAM]=u""
controlGuides[ROLE_DIAL]=u""
controlGuides[ROLE_DROPLIST]=u""
controlGuides[ROLE_SPLITBUTTON]=u""
controlGuides[ROLE_MENUBUTTON]=u"メニューを表示するには、エンターキーを押します。その後、上下の矢印キーで項目を選択できます。前後のコントロールに移動するには、タブキー、または、シフト+タブキーを押します。"
controlGuides[ROLE_DROPDOWNBUTTONGRID]=u""
controlGuides[ROLE_MATH]=u""
controlGuides[ROLE_EQUATION]=u""
controlGuides[ROLE_GRIP]=u""
controlGuides[ROLE_HOTKEYFIELD]=u""
controlGuides[ROLE_INDICATOR]=u""
controlGuides[ROLE_SPINBUTTON]=u"上下矢印キーを押して、値を調整します。"
controlGuides[ROLE_SOUND]=u""
controlGuides[ROLE_WHITESPACE]=u""
controlGuides[ROLE_TREEVIEWBUTTON]=u""
controlGuides[ROLE_IPADDRESS]=u""
controlGuides[ROLE_DESKTOPICON]=u""
controlGuides[ROLE_ALERT]=u""
controlGuides[ROLE_INTERNALFRAME]=u""
controlGuides[ROLE_DESKTOPPANE]=u""
controlGuides[ROLE_OPTIONPANE]=u""
controlGuides[ROLE_COLORCHOOSER]=u""
controlGuides[ROLE_FILECHOOSER]=u""
controlGuides[ROLE_FILLER]=u""
controlGuides[ROLE_MENU]=u""
controlGuides[ROLE_PANEL]=u""
controlGuides[ROLE_PASSWORDEDIT]=u"編集するには、そのまま入力します。ここに入力した内容は、音声で読み上げられません。"
controlGuides[ROLE_FONTCHOOSER]=u""
controlGuides[ROLE_LINE]=u""
controlGuides[ROLE_FONTNAME]=u""
controlGuides[ROLE_FONTSIZE]=u""
controlGuides[ROLE_BOLD]=u""
controlGuides[ROLE_ITALIC]=u""
controlGuides[ROLE_UNDERLINE]=u""
controlGuides[ROLE_FGCOLOR]=u""
controlGuides[ROLE_BGCOLOR]=u""
controlGuides[ROLE_SUPERSCRIPT]=u""
controlGuides[ROLE_SUBSCRIPT]=u""
controlGuides[ROLE_STYLE]=u""
controlGuides[ROLE_INDENT]=u""
controlGuides[ROLE_ALIGNMENT]=u""
controlGuides[ROLE_ALERT]=u""
controlGuides[ROLE_DATAGRID]=u""
controlGuides[ROLE_DATAITEM]=u""
controlGuides[ROLE_HEADERITEM]=u""
controlGuides[ROLE_THUMB]=u""
controlGuides[ROLE_CALENDAR]=u""
controlGuides[ROLE_VIDEO]=u""
controlGuides[ROLE_AUDIO]=u""
controlGuides[ROLE_CHARTELEMENT]=u""
controlGuides[ROLE_DELETED_CONTENT]=u""
controlGuides[ROLE_INSERTED_CONTENT]=u""

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def __init__(self):
		super(GlobalPlugin, self).__init__()

	def script_navigateControl(self, gesture):
		self.trigger()

	def checkNvdaMode(self):
		focus = api.getFocusObject()
		vbuf = focus.treeInterceptor
		if not vbuf:
			# #2023: Search the focus and its ancestors for an object for which browse mode is optional.
			for obj in itertools.chain((api.getFocusObject(),), reversed(api.getFocusAncestors())):
				if obj.shouldCreateTreeInterceptor:
					continue
				try:
					obj.treeInterceptorClass
				except:
					continue
				break
			else:
				return
			# Force the tree interceptor to be created.
			obj.shouldCreateTreeInterceptor = True
			ti = treeInterceptorHandler.update(obj)
			if not ti:
				return
			if focus in ti:
				# Update the focus, as it will have cached that there is no tree interceptor.
				focus.treeInterceptor = ti
				# If we just happened to create a browse mode TreeInterceptor
				# Then ensure that browse mode is reported here. From the users point of view, browse mode was turned on.
				if isinstance(ti,browseMode.BrowseModeTreeInterceptor) and not ti.passThrough:
					browseMode.reportPassThrough(ti,False)
					braille.handler.handleGainFocus(ti)
			return

		if not isinstance(vbuf, browseMode.BrowseModeTreeInterceptor):
			return
		# Toggle browse mode pass-through.
		return FOCUS_MODE if vbuf.passThrough else BROWSE_MODE

	def trigger(self):
		role=api.getNavigatorObject().role
		if isinstance(controlGuides[role],dict):
			g=controlGuides[role]["browse"] if self.checkNvdaMode()==BROWSE_MODE else controlGuides[role]["focus"]
		else:
			g=controlGuides[role]
		#end which guide messages? if any
		s=u"現在、%s上にいます。%s" % (controlNames[role], g)
		speech.speakMessage(s)

	__gestures = {
		"kb:f1": "navigateControl",
	}
