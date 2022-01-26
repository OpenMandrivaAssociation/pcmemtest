# Debug package is empty and rpmlint rejects build
%define _enable_debug_packages %{nil}
%define debug_package %{nil}

Summary:	A stand alone memory test for x86 architecture systems
Name:		pcmemtest
Version:	1.5
Release:	1
License:	GPLv2
Group:		System/Kernel and hardware
Url:		http://www.memtest.org
Source0:	https://codeload.github.com/martinwhitaker/pcmemtest/tar.gz/refs/tags/v%{version}#/%{name}-%{version}.tar.gz
Source1:	%{name}.rpmlintrc
Source2:	20_pcmemtest
BuildRequires:	gcc binutils
ExclusiveArch:	%{ix86} %{x86_64}

%description
PCMemTest is thorough, stand alone memory test for x86 architecture
systems. BIOS based memory tests are only a quick check and often
missfailures that are detected by PCMemTest.

%prep
%autosetup -p1

%build
%setup_compile_flags 
%ifarch %{ix86}
cd build32
%else
cd build64
%endif
%make_build LD=/usr/bin/ld.bfd

%install
%ifarch %{ix86}
cd build32
%else
cd build64
%endif
mkdir -p %{buildroot}/boot
install -m644 memtest.{bin,efi} -D %{buildroot}/boot/

install -p -m755 %{SOURCE2} -D %{buildroot}%{_sysconfdir}/grub.d/20_pcmemtest

%files
/boot/memtest.efi
/boot/memtest.bin
%{_sysconfdir}/grub.d/20_pcmemtest
