import Router from "next/router";

const Pagination = ({ currentPage, prevPage, nextPage, lastPage }) => {
  // TODO: error on page 2

  console.log("bruh", prevPage, nextPage, lastPage);

  if (currentPage === "1") {
    return (
      <div className="mb-6 flex justify-center">
        <div className="mb-6">
          <div className="flex w-full mt-6">
            <div>
              <nav className="flex">
                <a className="px-2 py-2 border border-gray-300 bg-white rounded-l-md hover:bg-gray-50">
                  {currentPage}
                </a>
                <a
                  onClick={() => Router.push(`/profile/page/${nextPage}`)}
                  className="px-2 py-2 border border-gray-300 bg-white hover:bg-gray-50"
                >
                  {nextPage}
                </a>
                <span className="px-4 py-2 border border-gray-300 bg-white text-sm font-medium text-gray-700">
                  ...
                </span>
                <a
                  onClick={() => Router.push(`/profile/page/${lastPage}`)}
                  className="px-2 py-2 border border-gray-300 bg-white hover:bg-gray-50"
                >
                  {lastPage}
                </a>
                <a
                  onClick={() => Router.push(`/profile/page/${nextPage}`)}
                  className="px-2 py-2 rounded-r-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    className="h-6 w-6"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth={2}
                      d="M9 5l7 7-7 7"
                    />
                  </svg>
                </a>
              </nav>
            </div>
          </div>
        </div>{" "}
      </div>
    );
  } else if (currentPage === lastPage) {
    return (
      <div className="mb-6 flex justify-center">
        <div className="mb-6">
          <div className="flex w-full mt-6">
            <div>
              <nav className="flex">
                <a
                  onClick={() => Router.push(`/profile/page/${prevPage}`)}
                  className="px-2 py-2 rounded-l-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    className="h-6 w-6"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth={2}
                      d="M15 19l-7-7 7-7"
                    />
                  </svg>
                </a>
                <a
                  onClick={() => Router.push(`/profile/page/1`)}
                  className="px-2 py-2 border border-gray-300 bg-white hover:bg-gray-50"
                >
                  1
                </a>
                <a
                  onClick={() => Router.push(`/profile/page/2`)}
                  className="px-2 py-2 border border-gray-300 bg-white hover:bg-gray-50"
                >
                  2
                </a>
                <span className="px-4 py-2 border border-gray-300 bg-white text-sm font-medium text-gray-700">
                  ...
                </span>
                <a className="px-2 py-2 rounded-r-md border border-gray-300 bg-white hover:bg-gray-50">
                  {lastPage}
                </a>
              </nav>
            </div>
          </div>
        </div>{" "}
      </div>
    );
  } else {
    return (
      <div className="mb-6 flex justify-center">
        <div className="mb-6">
          <div className="flex w-full mt-6">
            <div>
              <nav className="flex">
                <a
                  onClick={() => Router.push(`/profile/page/${prevPage}`)}
                  className="px-2 py-2 rounded-l-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    className="h-6 w-6"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth={2}
                      d="M15 19l-7-7 7-7"
                    />
                  </svg>
                </a>
                <a className="px-2 py-2 border border-gray-300 bg-white hover:bg-gray-50">
                  {currentPage}
                </a>
                <a
                  onClick={() => Router.push(`/profile/page/${nextPage}`)}
                  className="px-2 py-2 border border-gray-300 bg-white hover:bg-gray-50"
                >
                  {nextPage}
                </a>
                <span className="px-4 py-2 border border-gray-300 bg-white text-sm font-medium text-gray-700">
                  ...
                </span>
                <a
                  onClick={() => Router.push(`/profile/page/${lastPage}`)}
                  className="px-2 py-2 border border-gray-300 bg-white hover:bg-gray-50"
                >
                  {lastPage}
                </a>
                <a
                  onClick={() => Router.push(`/profile/page/${nextPage}`)}
                  className="px-2 py-2 rounded-r-md border border-gray-300 bg-white text-sm font-medium text-gray-500 hover:bg-gray-50"
                >
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    className="h-6 w-6"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth={2}
                      d="M9 5l7 7-7 7"
                    />
                  </svg>
                </a>
              </nav>
            </div>
          </div>
        </div>
      </div>
    );
  }
};

export default Pagination;
