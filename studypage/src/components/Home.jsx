import React, { useEffect } from "react";
import { Link } from "react-router-dom";
import homeVideo from './assets/homeVideo.mp4';
import AOS from "aos";
import "aos/dist/aos.css";

export default function Home() {
  useEffect(() => {
    AOS.init();
    if (Notification.permission === 'default') {
      Notification.requestPermission();
    }
  }, []);
  return (
    <div className="homepage-container">
      <section className="bg-gray-900 flex flex-col lg:flex-row items-center justify-between px-10 py-16">
        <div className="lg:w-1/2 space-y-6">
          {/* <h4 className="text-yellow-500 uppercase font-medium" data-aos="flip-up" data-aos-duration="1000" data-aos-delay="0">Study Central</h4> */}
          <h1 className="text-5xl lg:text-6xl text-white font-bold" data-aos="flip-up" data-aos-duration="1000" data-aos-delay="0">
            DESIGNING THE FUTURE <span className="text-yellow-500">TODAY</span>
          </h1>
          <p className="text-gray-400 text-lg">
            Your one-stop platform for all study resources. Learn, Grow, Succeed! Unlock endless opportunities and achieve your academic goals.
          </p>
          <Link to="/services">
              <button className="bg-yellow-500 hover:bg-yellow-600 mt-10 text-white font-semibold py-3 px-6 rounded-md shadow-md">
                Request Service
              </button>
            </Link>
        </div>
        <div className="md:w-1/2 relative lg:w-1/2 mt-8 lg:mt-0">
          <div className="bg-orange-800 w-full h-full absolute -z-10 rounded-md translate-x-6 translate-y-6"></div>
          <video
            className="rounded-md shadow-lg w-full h-full object-cover"
            autoPlay
            loop
            muted
          >
            <source
              src={homeVideo}
              type="video/mp4"
            />
            Your browser does not support the video tag.
          </video>
        </div>
      </section>


      <section className="py-12 px-4 md:px-8 bg-gray-50">
        <div className="max-w-screen-lg mx-auto text-center">
          {/* Heading */}
          <h2 className="text-4xl font-bold text-gray-900 mb-6">
            Why Choose <span className="text-orange-600">StudyPage?</span>
          </h2>
          <p className="text-lg text-gray-700 mb-12 max-w-2xl mx-auto leading-relaxed">
            At <span className="font-semibold text-orange-600">StudyPage</span>, we offer curated study materials, expert guidance, and practical tips to help you achieve academic success. Prepare for exams or explore new learning techniques with resources tailored just for you.
          </p>

          {/* Cards */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {/* Card 1 */}
            <div className="p-6 border rounded-lg shadow-lg bg-red-300 transform transition-transform hover:-translate-y-2 hover:shadow-2xl">
              <div className="text-orange-600 text-4xl mb-4">
                <i className="fas fa-book-open"></i>
              </div>
              <h3 className="text-2xl font-semibold text-gray-800 mb-4">
                Comprehensive Guides
              </h3>
              <p className="text-gray-600 leading-relaxed">
                Access in-depth study guides and materials on a variety of subjects.
              </p>
            </div>

            {/* Card 2 */}
            <div className="p-6 border rounded-lg shadow-lg bg-green-300 transform transition-transform hover:-translate-y-2 hover:shadow-2xl">
              <div className="text-orange-600 text-4xl mb-4">
                <i className="fas fa-lightbulb"></i>
              </div>
              <h3 className="text-2xl font-semibold text-gray-800 mb-4">
                Expert Tips
              </h3>
              <p className="text-gray-600 leading-relaxed">
                Learn from experts with practical tips to boost your study efficiency.
              </p>
            </div>

            {/* Card 3 */}
            <div className="p-6 border rounded-lg shadow-lg bg-orange-300 transform transition-transform hover:-translate-y-2 hover:shadow-2xl">
              <div className="text-orange-600 text-4xl mb-4">
                <i className="fas fa-clock"></i>
              </div>
              <h3 className="text-2xl font-semibold text-gray-800 mb-4">
                24/7 Access
              </h3>
              <p className="text-gray-600 leading-relaxed">
                Get access to all resources anytime, anywhere, on any device.
              </p>
            </div>
          </div>
        </div>
      </section>

      <section className="bg-gray-50 py-12 px-6 md:px-20">
        <div className="max-w-7xl mx-auto flex flex-col md:flex-row items-center gap-10">
          {/* Left Content */}
          <div className="md:w-1/2">
            <h4 className="text-orange-600 font-semibold uppercase mb-2 tracking-wider">
              Your One-Stop Study Platform
            </h4>
            <h2 className="text-4xl font-bold text-gray-900 mb-4 leading-tight">
              Hire Experts to Work on Your Project
            </h2>
            <p className="text-gray-600 mb-6 leading-relaxed">
              Whether you are a student or a professional, we have a vast network
              of proficient experts ready to assist you. From academic tasks to
              complex business projects, our platform connects you with the right
              expert to ensure success.
            </p>
            <ul className="space-y-4 mb-8">
              <li className="flex items-center">
                <span className="mr-3 text-orange-600 text-xl">✓</span>
                <span className="text-gray-700">Expert Assistance on Any Project</span>
              </li>
              <li className="flex items-center">
                <span className="mr-3 text-orange-600 text-xl">✓</span>
                <span className="text-gray-700">Qualified and Proficient Experts</span>
              </li>
              <li className="flex items-center">
                <span className="mr-3 text-orange-600 text-xl">✓</span>
                <span className="text-gray-700">Flexible Project Categories</span>
              </li>
              <li className="flex items-center">
                <span className="mr-3 text-orange-600 text-xl">✓</span>
                <span className="text-gray-700">Guaranteed Quality and Timely Delivery</span>
              </li>
            </ul>

            <Link to="/services">
              <button className="bg-yellow-500 hover:bg-yellow-600 text-white font-semibold py-3 px-6 rounded-md shadow-md">
                Request Service
              </button>
            </Link>
          </div>

          {/* Right Image */}
          <div className="md:w-1/2 relative">
            <div className="bg-orange-800 w-full h-full absolute -z-10 rounded-md translate-x-6 translate-y-6"></div>
            <img
              src="https://img.freepik.com/free-photo/concentrated-black-european-male-student-with-beard-preparing-examination-test-sitting-university-canteen-eating-sandwich-searching-information-internet-using-laptop_273609-7496.jpg?t=st=1734513170~exp=1734516770~hmac=a7b2db547492f1eaa7e7254d2ebff9b68342048b96a0c6c9ff6a9f7d047cd9e0&w=740"
              alt="Study interaction"
              className="rounded-md shadow-lg"
            />
          </div>


        </div>
      </section>
    </div>
  );
}
