#!/usr/bin/env osascript -l JavaScript

// on run {phoneNumber, textMessage}
//     tell application "Messages"
//         set targetService to 1st service whose service type = iMessage
//         set targetBuddy to buddy phoneNumber of targetService
//         send textMessage to targetBuddy
//     end tell
// end run

function sendText(phoneNumber, textMessage) {
    console.log(phoneNumber, textMessage);
    var messages = Application("Messages");
    var targetService = messages.services().find(function (e) { return e.serviceType() === "iMessage"; });

    var targetBuddy;
    try {
        targetBuddy = targetService.buddy().find(function (e) { return e.handle() == phoneNumber; });
    } catch (err) {
        throw "Buddy not in contacts.";
    }

    messages.send(textMessage, {"to": targetBuddy});
}

function run(argv) {
    var phoneNumber = argv[0];
    var textMessage = argv[1];

    if (phoneNumber.length === 10) {
        phoneNumber = "+1" + phoneNumber;
    }

    sendText(phoneNumber, textMessage);
}
