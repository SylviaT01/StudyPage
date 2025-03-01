import React from "react";
import classNames from "classnames";

const MessageBubble = ({ message, activeUser }) => {
  // Parse the attachments properly
  const parseAttachments = () => {
    if (!message.attachments || !message.attachments.length) return [];
    
    try {
      // If it's a stringified JSON array (as shown in your console log)
      if (typeof message.attachments[0] === 'string' && message.attachments[0].startsWith('[')) {
        return JSON.parse(message.attachments[0]);
      }
      // If it's already an array of attachment URLs
      return message.attachments;
    } catch (error) {
      console.error("Error parsing attachments:", error);
      return [];
    }
  };

  const attachments = parseAttachments();

  const isSender =
    activeUser &&
    message &&
    (
      (activeUser.client_name && activeUser.client_name !== message.sender) ||
      (activeUser.isAdmin && activeUser.client && message.sender === activeUser.client)
    );

  const bubbleClass = classNames(
    "p-4 mb-3 rounded-2xl max-w-lg break-words shadow-sm transition-all duration-200",
    {
      "bg-gradient-to-br from-blue-500 to-blue-600 text-white self-end rounded-br-sm": !isSender,
      "bg-gradient-to-br from-gray-700 to-gray-800 text-white self-start rounded-bl-sm": isSender,
    },
    {
      "ml-auto": !isSender,
      "mr-auto": isSender,
    }
  );

  const renderMessageContent = () => {
    if (attachments && attachments.length > 0) {
      return (
        <div className="space-y-2">
          {attachments.map((attachment, index) => (
            attachment.endsWith(".png") || attachment.endsWith(".jpg") ? (
              <div key={index} className="relative group">
                <img
                  src={attachment}
                  alt={`Attachment ${index + 1}`}
                  className="w-48 h-48 object-cover rounded-lg transition-transform duration-200 hover:scale-105 cursor-pointer"
                  onClick={() => window.open(attachment, "_blank")}
                />
                <div className="absolute inset-0 bg-black bg-opacity-0 group-hover:bg-opacity-20 transition-all duration-200 rounded-lg" />
              </div>
            ) : (
              <a
                key={index}
                href={attachment}
                target="_blank"
                download={isSender ? attachment.split("/").pop() : undefined}
                rel="noopener noreferrer"
                className={classNames(
                  "flex items-center space-x-2 p-2 rounded-lg transition-colors duration-200",
                  {
                    "hover:bg-blue-600": !isSender,
                    "hover:bg-gray-600": isSender,
                  }
                )}
              >
                <svg
                  className="w-5 h-5"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
                  />
                </svg>
                <span className="underline">{attachment.split("/").pop()}</span>
              </a>
            )
          ))}
          <p className={classNames(
            "whitespace-pre-wrap text-sm leading-relaxed",
            { "text-white": !isSender, "text-gray-200": isSender }
          )}>
            {message.content}
          </p>
        </div>
      );
    }

    return (
      <p className={classNames(
        "whitespace-pre-wrap text-sm leading-relaxed",
        { "text-white": !isSender, "text-gray-200": isSender }
      )}>
        {message.content}
      </p>
    );
  };

  return (
    <div className={bubbleClass}>
      {renderMessageContent()}
      <p className="text-xs text-gray-400 mt-2 opacity-75">
        {new Date(message.timestamp).toLocaleString()}
      </p>
    </div>
  );
};

export default MessageBubble;





// import React from "react";
// import classNames from "classnames";

// const MessageBubble = ({ message, activeUser }) => {
//   const isSender =
//     activeUser &&
//     message &&
//     (
//       (activeUser.client_name && activeUser.client_name !== message.sender) ||
//       (activeUser.isAdmin && activeUser.client && message.sender === activeUser.client)
//     );

//   const bubbleClass = classNames(
//     "p-3 mb-2 rounded-2xl max-w-md break-words shadow-sm transition-all duration-200",
//     {
//       "bg-gradient-to-br from-blue-500 to-blue-600 text-white self-end rounded-br-sm": !isSender,
//       "bg-gradient-to-br from-gray-700 to-gray-800 text-white self-start rounded-bl-sm": isSender,
//     },
//     {
//       "ml-auto": !isSender,
//       "mr-auto": isSender,
//     }
//   );

//   const renderMessageContent = () => {
//     if (message.attachments && message.attachments.length > 0) {
//       return (
//         <div className="space-y-2">
//           {message.attachments.map((attachment, index) => (
//             attachment.endsWith(".png") || attachment.endsWith(".jpg") ? (
//               <div key={index} className="relative group">
//                 <img
//                   src={attachment}
//                   alt={`Attachment ${index + 1}`}
//                   className="w-36 h-36 object-cover rounded-lg transition-transform duration-200 hover:scale-105 cursor-pointer"
//                   onClick={() => window.open(attachment, "_blank")}
//                 />
//                 <div className="absolute inset-0 bg-black bg-opacity-0 group-hover:bg-opacity-20 transition-all duration-200 rounded-lg" />
//               </div>
//             ) : (
//               <a
//                 key={index}
//                 href={attachment}
//                 target={!isSender ? "_blank" : undefined}
//                 download={isSender ? attachment.split("/").pop() : undefined}
//                 rel={!isSender ? "noopener noreferrer" : undefined}
//                 className={classNames(
//                   "flex items-center space-x-2 p-2 rounded-lg transition-colors duration-200",
//                   {
//                     "hover:bg-blue-600": !isSender,
//                     "hover:bg-gray-600": isSender,
//                   }
//                 )}
//               >
//                 <svg
//                   className="w-5 h-5"
//                   fill="none"
//                   stroke="currentColor"
//                   viewBox="0 0 24 24"
//                   xmlns="http://www.w3.org/2000/svg"
//                 >
//                   <path
//                     strokeLinecap="round"
//                     strokeLinejoin="round"
//                     strokeWidth={2}
//                     d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
//                   />
//                 </svg>
//                 <span className="underline">{attachment.split("/").pop()}</span>
//               </a>
//             )
//           ))}
//           <p className={classNames(
//             "whitespace-pre-wrap text-xs leading-snug",
//             { "text-white": !isSender, "text-gray-200": isSender }
//           )}>
//             {message.content}
//           </p>
//         </div>
//       );
//     }

//     return (
//       <p className={classNames(
//         "whitespace-pre-wrap text-xs leading-snug",
//         { "text-white": !isSender, "text-gray-200": isSender }
//       )}>
//         {message.content}
//       </p>
//     );
//   };

//   return (
//     <div className={bubbleClass}>
//       {renderMessageContent()}
//       <p className="text-xs text-gray-400 mt-2 opacity-75">
//         {new Date(message.timestamp).toLocaleString()}
//       </p>
//     </div>
//   );
// };

// export default MessageBubble;