Summary: Python interface to PostgresSQL 
Name: python-PyGreSQL
Release: 1
Version: 2.2
Copyright: See description
Group: Applications/Databases/Interfaces
Group(pl): Aplikacje/Bazy Danych/Interfejsy
Source: PyGreSQL-2.2.tgz
Source1: python-Makefile.pre.in
Source2: Setup.in.PyGreSQL
URL: http://www.druid.net/pygresql
BuildRoot:	/tmp/%{name}-%{version}-root
Summary(pl): Interfejs pomiêdzy Pythonem a bazami danych PostgresSQL 

%description
This package provides access to PostgresSQL data from Python

Written by D'Arcy J.M. Cain, darcy@druid.net
Based heavily on code written by Pascal Andre, andre@chimay.via.ecp.fr.
Copyright (c) 1995, Pascal ANDRE (andre@via.ecp.fr)    

See /usr/doc/python-PyGreSQL-2.2 for the full Copyright notice.

%description -l pl
Ten pakiet zapewnia dostêp do baz danych PostgreSQL z poziomu skryptow Pythona.

Autor: D'Arcy J.M. Cain, darcy@druid.net
Opartte na kodzienapisanym przez Pascala Andre, andre@chimay.via.ecp.fr.
Copyright (c) 1995, Pascal ANDRE (andre@via.ecp.fr)

Pene info na temat praw autorskich znajduje siê w /usr/doc/python-PyGreSQL-2.2

%prep
%setup -n PyGreSQL-2.2
cp $RPM_SOURCE_DIR/python-Makefile.pre.in ./Makefile.pre.in
cp $RPM_SOURCE_DIR/Setup.in.PyGreSQL Setup.in

%build
make -f Makefile.pre.in boot
make

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/
make prefix=$RPM_BUILD_ROOT/usr install
install -m 644 pg.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/
install -m 644 pgext.py $RPM_BUILD_ROOT%{_libdir}/python1.5/site-packages/

%files
%defattr(644,root,root,755)
%doc README README.linux tutorial Announce ChangeLog
%attr(755,root,root) %{_libdir}/python1.5/site-packages/_pgmodule.so
%attr(755,root,root) %{_libdir}/python1.5/site-packages/pgext.py
%attr(755,root,root) %{_libdir}/python1.5/site-packages/pg.py
