// import React, { useContext } from 'react';
// import { Link } from 'react-router-dom';
// import { UserContext } from './contexts/userContext';
// import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
// import { faUser, faCommentDots } from '@fortawesome/free-solid-svg-icons';

// export const NavBar = () => {
//     const { authToken, currentUser } = useContext(UserContext);
//     console.log('adminauthtoken', authToken);
//     console.log('this is the user',currentUser)

//     // Determine account link
//     const accountLink = authToken
//         ? currentUser?.is_admin
//             ? "/admin/dashboard"
//             : "/userprofile/dashboard"
//         : "/login";

//     // Determine chat link
//     const chatLink = currentUser?.is_admin ? "/adminchat" : "/chat";

//     return (
//         <nav className="flex justify-between items-center px-10 py-6 bg-gray-900">
//             <div className="container mx-auto flex justify-between items-center">
//                 <Link
//                     to="/"
//                     className="text-yellow-500 font-bold text-2xl"
//                 >
//                     Study<span className="text-white">Page</span>
//                 </Link>
//                 <div className="flex items-center space-x-8">
//                     <Link
//                         to="/"
//                         className="text-white hover:text-yellow-400 cursor-pointer"
//                     >
//                         Home
//                     </Link>
//                     <Link
//                         to="/services"
//                         className="text-white hover:text-yellow-400 cursor-pointer"
//                     >
//                         Services
//                     </Link>
//                     <Link
//                         to="/expertspage"
//                         className="bg-transparent py-1 px-2 transition ease-in-out hover:-translate-y-1 hover:scale-110 duration-300 hover:underline"
//                         currentUser={currentUser}
//                     >
//                         Our Experts
//                     </Link>
//                     <Link
//                         to="/about"
//                         className="text-white hover:text-yellow-400 cursor-pointer"
//                     >
//                         About
//                     </Link>
//                 </div>
//                 <div className="flex gap-4">
//                     <Link to={accountLink} className="text-white hover:text-yellow-400 cursor-pointer flex items-center text-xs">
//                         <FontAwesomeIcon icon={faUser} className="text-lg" />
//                         <span className="ml-1">{authToken ? 'My Account' : 'Login'}</span>
//                     </Link>

//                     <Link
//                         to={{
//                             pathname: chatLink, // Dynamic path based on user role
//                         }}
//                         state={{ authToken }} // Pass authToken in state
//                         className="text-gray-700 hover:text-blue-700 flex items-center text-xs"
//                     >
//                         <FontAwesomeIcon icon={faCommentDots} className="text-lg text-blue-700" />
//                     </Link>
//                 </div>
//             </div>
//         </nav>
//     );
// };

import React, { useContext } from 'react';
import { Link } from 'react-router-dom';
import { UserContext } from './contexts/userContext';
import { useSocket } from './contexts/SocketContext';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { 
  faUser, 
  faCommentDots, 
  faCircle 
} from '@fortawesome/free-solid-svg-icons';

export const NavBar = () => {
    const { authToken, currentUser } = useContext(UserContext);
    const { unreadCounts } = useSocket();

    // Calculate total unread messages
    const totalUnreadMessages = Object.values(unreadCounts).reduce((sum, count) => sum + count, 0);
    console.log('totalUnreadMessages', totalUnreadMessages);

    // Determine account link
    const accountLink = authToken
        ? currentUser?.is_admin
            ? "/admin/dashboard"
            : "/userprofile/dashboard"
        : "/login";

    // Determine chat link
    const chatLink = currentUser?.is_admin ? "/adminchat" : "/chat";

    return (
        <nav className="flex justify-between items-center px-10 py-6 bg-gray-900">
            <div className="container mx-auto flex justify-between items-center">
                <Link
                    to="/"
                    className="text-yellow-500 font-bold text-2xl"
                >
                    Study<span className="text-white">Page</span>
                </Link>
                <div className="flex items-center space-x-8">
                    <Link
                        to="/"
                        className="text-white hover:text-yellow-400 cursor-pointer"
                    >
                        Home
                    </Link>
                    <Link
                        to="/services"
                        className="text-white hover:text-yellow-400 cursor-pointer"
                    >
                        Services
                    </Link>
                    <Link
                        to="/expertspage"
                        className="bg-transparent text-white py-1 px-2 transition ease-in-out hover:-translate-y-1 hover:scale-110 duration-300 hover:underline"
                        currentUser={currentUser}
                    >
                        Our Experts
                    </Link>
                    <Link
                        to="/about"
                        className="text-white hover:text-yellow-400 cursor-pointer"
                    >
                        About
                    </Link>
                </div>
                <div className="flex gap-4">
                    <Link 
                        to={accountLink} 
                        className="text-white hover:text-yellow-400 cursor-pointer flex items-center text-xs"
                    >
                        <FontAwesomeIcon icon={faUser} className="text-lg" />
                        <span className="ml-1">
                            {authToken ? 'My Account' : 'Login'}
                        </span>
                    </Link>

                    <Link
                        to={chatLink}
                        state={{ authToken }}
                        className="text-gray-700 hover:text-blue-700 flex items-center text-xs relative"
                    >
                        <FontAwesomeIcon 
                            icon={faCommentDots} 
                            className="text-lg text-blue-700" 
                        />
                        {totalUnreadMessages > 0 && (
                            <div className="absolute -top-2 -right-2 flex items-center justify-center">
                                <FontAwesomeIcon 
                                    icon={faCircle} 
                                    className="text-red-500 text-sm" 
                                />
                                <span className="absolute text-white text-xs font-bold">
                                    {totalUnreadMessages > 99 ? '99+' : totalUnreadMessages}
                                </span>
                            </div>
                        )}
                    </Link>
                </div>
            </div>
        </nav>
    );
};