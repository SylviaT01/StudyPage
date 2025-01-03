import React from "react";
import { Parallax } from "react-parallax";

const About = () => {
  return (
    <div className="bg-gray-50">
      {/* Sidebar */}


      {/* Main Content */}
      <main className="w-full p-8">
        <div className="header">
          <Parallax
            className="w-full h-[calc(100vh-5rem)] object-cover brightness-[.6]"
            bgImage="https://plus.unsplash.com/premium_photo-1723622412015-c4a9b4ef46b8?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
            strength={225}
          >
            <div style={{ height: 500 }}>
              <p className="text-center absolute top-[50%] left-[50%] -translate-x-[50%] -translate-y-[50%] uppercase font-extralight text-white text-8xl">
                StudyPage
              </p>
            </div>
          </Parallax>
        </div>

        <div className="wrapper">
          <div className="my-8 text-center">
            <p className="tracking-widest font-semibold uppercase text-xl p-5 text-black">
              StudyPage - Empowering Your Learning Journey!
            </p>
            <p className="text-2xl px-[20rem] pb-5 font-extralight">
              Unlock your potential and achieve academic success with StudyPage - where learning is not just a task, but an inspiring experience.
            </p>
            <p className="px-[7rem] pb-2 text-xl font-light">
              Welcome to StudyPage, your ultimate destination for comprehensive study resources. Our journey started with a mission: to provide students, educators, and lifelong learners with the tools they need to excel in their academic endeavors.
              We believe in fostering a community of knowledge and growth, where everyone has access to expert guidance, useful tips, and relevant study materials.
              Your feedback and suggestions matter to us. They inspire us to enhance our platform and continuously innovate, ensuring that we meet the evolving needs of our users. We are committed to supporting your learning journey every step of the way.
              Whether you're preparing for exams, exploring new learning strategies, or looking for academic assistance, StudyPage is here to help you succeed. Thank you for being a part of StudyPage. We are excited to support you in achieving your educational goals! 📚
            </p>
          </div>
        </div>

        <div className="bg-gray-100 py-16">
          <div className="text-center mb-12">
            <p className="text-3xl font-semibold text-gray-800">Our Core Values</p>
            <p className="text-lg text-gray-600 mt-4">
              At StudyPage, we are guided by values that drive our commitment to providing a high-quality learning experience for all.
            </p>
          </div>
          <div className="max-w-screen-xl mx-auto px-4 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <div className="bg-white shadow-md rounded-lg p-6 text-center">
              <p className="text-2xl font-bold text-gray-600">Empowerment</p>
              <p className="text-gray-600 mt-4">
                We believe in empowering students with the tools and resources they need to achieve academic success and reach their full potential.
              </p>
            </div>
            <div className="bg-white shadow-md rounded-lg p-6 text-center">
              <p className="text-2xl font-bold text-gray-600">Collaboration</p>
              <p className="text-gray-600 mt-4">
                We foster a collaborative learning environment where students, educators, and learners support each other in their educational journeys.
              </p>
            </div>
            <div className="bg-white shadow-md rounded-lg p-6 text-center">
              <p className="text-2xl font-bold text-gray-600">Innovation</p>
              <p className="text-gray-600 mt-4">
                We continuously innovate to offer the best study tools, resources, and strategies, adapting to the ever-changing educational landscape.
              </p>
            </div>
            <div className="bg-white shadow-md rounded-lg p-6 text-center">
              <p className="text-2xl font-bold text-gray-600">Accessibility</p>
              <p className="text-gray-600 mt-4">
                We strive to make learning accessible to everyone, regardless of their location or background, by providing inclusive resources.
              </p>
            </div>
            <div className="bg-white shadow-md rounded-lg p-6 text-center">
              <p className="text-2xl font-bold text-gray-600">Integrity</p>
              <p className="text-gray-600 mt-4">
                We operate with integrity and transparency, ensuring that students and educators can trust the resources and information we provide.
              </p>
            </div>
            <div className="bg-white shadow-md rounded-lg p-6 text-center">
              <p className="text-2xl font-bold text-gray-600">Continuous Growth</p>
              <p className="text-gray-600 mt-4">
                We are committed to continuous learning and growth, both for our platform and for the students we serve, adapting to their needs.
              </p>
            </div>
          </div>
        </div>
      </main>
    </div>
  );
};

export default About;
