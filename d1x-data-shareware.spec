Summary:	Shareware version of Descent data for d1x
Summary(pl.UTF-8):   Wersja shareware danych Descenta dla d1x
Name:		d1x-data-shareware
Version:	1.2
Release:	2
License:	distributable if unmodified
Group:		X11/Applications/Games
Vendor:		Parallax Software Corporation
Source0:	ftp://pyropilots.org/pub/d1x/d1swdf.tar.gz
# Source0-md5:	8112d6127a7a81a36735f5a9c3175ec2
URL:		http://www.interplay.com/descent/
Requires:	d1x-shareware
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Shareware version of Descent 1.2 data for d1x.

%description -l pl.UTF-8
Wersja shareware danych z Descenta 1.2 dla d1x.

%prep
%setup -q -n d1shar

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/d1x

install descent.* $RPM_BUILD_ROOT%{_datadir}/d1x

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ORDERFRM.TXT README README.TXT REFCARD.TXT
%{_datadir}/d1x/*
