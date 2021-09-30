import Nav from './Nav'

const Layout = ( { children } ) => {
    return (
        <div className="flex bg-blue-200">
            <Nav />
            <div className="w-10/12 flex bg-gray-300">
                <main className="w-full h-screen overflow-scroll flex justify-center">
                    {children}
                </main>
            </div>
        </div>
    )
}

export default Layout;