import QtQuick 2.2
import QtQuick.Window 2.2
import QtQuick.Controls 2.0
import PokerGamePanel 1.0
import QtQuick.Layouts 1.3

Window {
    id:app_window
    visible:true
    width:600
    height:400
    flags: Qt.FramelessWindowHint

    property var bet_value : 1
    property int max_bet : 500
    property point pos

    function check_and_fix_maxbet() {
        if(bet_value > max_bet) {
            bet_value = max_bet
        }
        if(bet_value > gp.current_credit) {
            bet_value = gp.current_credit
        }
    }

    Page {
        anchors.fill: parent
        header: ToolBar {
            id : toolbar
            RowLayout {
                anchors.fill: parent
                Label {
                    id: title
                    text: qsTr("Python games for education. A Practice of Qt and QML.")
                    Layout.fillWidth: true
                    Layout.leftMargin: 10
                    Layout.alignment: Qt.AlignLeft

                    MouseArea {
                        anchors.fill: parent
                        propagateComposedEvents: true
                        onPressed: { pos = Qt.point(mouse.x, mouse.y) }
                        onPositionChanged: {
                            var diff = Qt.point(mouse.x - pos.x, mouse.y - pos.y)
                            app_window.x += diff.x
                            app_window.y += diff.y
                        }
                    }
                }
                Text {
                    text: "<a href=\"https://github.com/KouOuchi/PokerGame\">?</a>"
                    onLinkActivated: {
                        Qt.openUrlExternally(link)
                    }
                    Layout.alignment: Qt.AlignRight
                }
                ToolButton {
                    id:back_cancel
                    text: "Quit"
                    onClicked: app_window.close()
                    Layout.alignment: Qt.AlignRight
                }
            }
        }

        PokerGamePanel {
            id:gp
            anchors.rightMargin: 10
            anchors.leftMargin: 10
            anchors.bottomMargin: 10
            anchors.topMargin: 10
            anchors.fill: parent

            ColumnLayout {
                anchors.fill: parent

                RowLayout {
                    Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                    Image {
                        id: image0
                        width: 100
                        height: 100
                        fillMode: Image.PreserveAspectFit
                    }

                    Image {
                        id: image1
                        width: 100
                        height: 100
                        fillMode: Image.PreserveAspectFit
                    }

                    Image {
                        id: image2
                        width: 100
                        height: 100
                        fillMode: Image.PreserveAspectFit
                    }

                    Image {
                        id: image3
                        width: 100
                        height: 100
                        fillMode: Image.PreserveAspectFit
                    }

                    Image {
                        id: image4
                        width: 100
                        height: 100
                        fillMode: Image.PreserveAspectFit
                    }
                }

                Label {
                    id:status
                    font.family: "Impact"
                    Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                    text:gp.current_status
                }

                RowLayout {
                    Layout.alignment: Qt.AlignHCenter | Qt.AlignVCenter
                    GridLayout {
                        rows:2
                        columns:2
                        Layout.preferredWidth: 70
                        Label {
                            id: bet
                            text: qsTr("Bet")
                        }
                        Label {
                            id: betbox
                            Layout.alignment: Qt.AlignRight
                            text: bet_value
                            Layout.leftMargin:20
                        }
                        Label {
                            id: label
                            text: qsTr("Credit")
                        }

                        Label {
                            id:credit
                            Layout.alignment: Qt.AlignRight
                            text: gp.current_credit
                            Layout.leftMargin:20
                        }
                    }

                    TopToolButton {
                        button_icon_alternative_text:"1"
                        button_text: qsTr("Bet +1")
                        onButton_clicked: {
                            bet_value += 1
                            check_and_fix_maxbet()
                        }
                        enabled: gp.current_credit > 0
                    }
                    TopToolButton {
                        button_icon_alternative_text:"10"
                        button_text: qsTr("Bet +10")
                        onButton_clicked: {
                            if(bet_value === 1) {
                                bet_value = 10
                            }

                            bet_value += 10
                            check_and_fix_maxbet()
                        }
                        enabled: gp.current_credit > 0
                    }
                    TopToolButton {
                        button_icon_alternative_text:"100"
                        button_text: qsTr("Bet +100")
                        onButton_clicked: {
                            if(bet_value === 1) {
                                bet_value = 100
                            }

                            bet_value += 100
                            check_and_fix_maxbet()
                        }
                        enabled: gp.current_credit > 0
                    }
                    TopToolButton {
                        id: cancel_vet
                        button_icon_alternative_text:"X"
                        button_text: qsTr("Clear")
                        onButton_clicked: {
                            bet_value = 1
                        }
                        enabled: gp.current_credit > 0
                    }
                    TopToolButton {
                        id: roundButton
                        Layout.alignment: Qt.AlignRight | Qt.AlignVCenter
                        scale: 1.5
                        button_icon_alternative_text:"!!!"
                        button_text: qsTr("Start")
                        onButton_clicked: {
                            // start poker
                            gp.draw_start(bet_value)

                            // fill image source
                            image0.source = gp.get_hand(0)
                            image1.source = gp.get_hand(1)
                            image2.source = gp.get_hand(2)
                            image3.source = gp.get_hand(3)
                            image4.source = gp.get_hand(4)

                            check_and_fix_maxbet()
                        }
                        enabled: gp.current_credit > 0
                    }
                }
            }
        }
    }
}
