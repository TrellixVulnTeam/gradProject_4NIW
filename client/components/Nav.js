import Link from 'next/link'

const Nav = () => {
    return (
        <nav className="w-3/12">
            <ul className="h-screen items-center bg-black text-white text-lg">
                <li className="hover:bg-gray-400 p-6">
                    <Link href='/'>Home</Link>
                </li>
                <li className="hover:bg-gray-400 p-6">
                    <Link href='/about'>About</Link>
                </li>
                <li className="hover:bg-gray-400 p-6">
                    <Link href='/profile/page/1'>Profiles</Link>
                </li>
                <li className="hover:bg-gray-400 p-6">
                    <Link href='/topics'>Topics</Link>
                </li>
            </ul>
        </nav>
    )
}

export default Nav;