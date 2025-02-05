import { createContext, useEffect, useState, useContext } from "react";
import { useNavigate } from "react-router-dom";

export const UserContext = createContext();


const fetchWithAuth = async (url, options = {}) => {
  let token = localStorage.getItem("token");
  options.headers = {
    ...options.headers,
    Authorization: `Bearer ${token}`,
  };

  let response = await fetch(url, options);

  if (response.status === 401) {
    const refreshToken = localStorage.getItem("refresh_token");
    const refreshResponse = await fetch("https://backendstudypage.onrender.com/refresh", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${refreshToken}`,
      },
    });

    if (refreshResponse.ok) {
      const refreshData = await refreshResponse.json();
      localStorage.setItem("token", refreshData.access_token);

      options.headers["Authorization"] = `Bearer ${refreshData.access_token}`;
      response = await fetch(url, options);
    } else {
      localStorage.removeItem("token");
      localStorage.removeItem("refresh_token");
    }
  }

  return response;
};
export const useUserContext = () => useContext(UserContext);
export const UserProvider = ({ children }) => {
  
  const nav = useNavigate();
  const [authToken, setAuthToken] = useState(
    () => localStorage.getItem("token") || null
  );
  const [currentUser, setCurrentUser] = useState(null);
  const [loading, setLoading] = useState(true);

  const fetchCurrentUser = async () => {
    if (authToken) {
      try {
        const response = await fetchWithAuth(
          "https://backendstudypage.onrender.com/current_user",
          {
            method: "GET",
            headers: {
              "Content-Type": "application/json",
            },
          }
        );
        const data = await response.json();
        if (response.ok) {
          setCurrentUser(data);
          if (data.is_admin) {
            nav("/admin/dashboard");
          } else {
            nav("/");
          }
        } else {
          console.error("Failed to fetch current user:", data.message);
          handleLogout();
        }
      } catch (error) {
        console.error("Error fetching current user:", error);
        handleLogout();
      }
    }
    setLoading(false);
  };
  useEffect(() => {
    fetchCurrentUser();
  }, [authToken]);

  const signup = (username, email, phone_number = '', password) => {
    fetch("https://backendstudypage.onrender.com/register", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username,
        email,
        phone_number,
        password,
      }),
    })
      .then((res) => res.json())
      .then((res) => {
        if (res.success) {
          nav("/login");
          alert(res.success);
        } else if (res.error) {
          alert(res.error);  
        } else {
          alert("Something went wrong");
        }
      })
      .catch((error) => {
        console.error("Error during signup:", error);
        alert("Something went wrong");
      });
  };


  const login = (email, password) => {
    fetch("https://backendstudypage.onrender.com/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        email,
        password,
      }),
    })
      .then((res) => res.json())
      .then((res) => {
        if (res.access_token) {
          setAuthToken(res.access_token);
          localStorage.setItem("token", res.access_token);
          localStorage.setItem("refresh_token", res.refresh_token);
          console.log("Logged in token:", res.access_token);
          nav("/");
          alert("Login success");
        } else if (res.error) {
          alert(res.error);
        } else {
          alert("Invalid password or username");
        }
      });
  };
  
  

  const handleLogout = () => {
    setAuthToken(null);
    setCurrentUser(null);
    localStorage.removeItem("token");
    localStorage.removeItem("refresh_token");
    nav("/login");
  };

  const logout = () => {
    fetchWithAuth("https://backendstudypage.onrender.com/logout", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((res) => res.json())
      .then((res) => {
        if (res.success) {
          handleLogout();
        } else {
          alert("Something went wrong");
        }
      });
  };

  const contextData = {
    currentUser,
    setCurrentUser,
    setAuthToken,
    signup,
    login,
    logout,
    authToken,
    loading,
  };

  return (
    <UserContext.Provider value={contextData}>{children}</UserContext.Provider>
  );
};
